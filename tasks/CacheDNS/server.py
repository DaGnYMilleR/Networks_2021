from scapy.layers.dns import DNS, DNSQR, DNSRR
from scapy.layers.inet import IP, UDP
from scapy.all import *
import CacheDNS.config as config
import CacheDNS.cache as cache


class Server:
    def __init__(self, cache):
        self.cache = cache

    def run(self):
        sniff(filter=f'udp port {config.DNS_PORT}', prn=self.handle_udp_packet)

    def handle_udp_packet(self, pkt):
        if self.is_dns_query_packet(pkt):
            self.cache.flush()
            if not self.in_cache(pkt):
                self.request(pkt)
            self.response(pkt)

    @staticmethod
    def is_dns_query_packet(pkt):
        return pkt.haslayer(DNS) and pkt.getlayer(DNS).qr == 0 and pkt[IP].dst == config.DNS_SERVER_IP

    def in_cache(self, pkt):
        qname = pkt[DNSQR].qname.decode('cp1251')
        return qname in self.cache.data.keys()\
               and pkt[DNSQR].qtype in self.cache.data[qname]\
               and float(self.cache.data[qname][pkt[DNSQR].qtype][2]) >= time.time()

    def request(self, pkt):
        ip = IP(dst=config.GOOGLE_DNS_SERVER_IP)
        udp = UDP(dport=53)
        dns = DNS(rd=1, qd=DNSQR(qname=pkt[DNSQR].qname.decode('cp1251'), qtype=pkt[DNSQR].qtype))
        response = sr1(ip / udp / dns)
        if response[DNS].ancount == 0:
            return
        for i in range(response[DNS].ancount):
            rtype = response[DNSRR][i].type
            if rtype in config.RECORD_TYPES:
                data = response[DNSRR][i].rdata
                if type(data) == bytes:
                    rdata = data.decode('cp1251')
                else:
                    rdata = data
                ttl = int(response[DNSRR][i].ttl)
                cache.add_or_update(response[DNSRR][i].rrname.decode(), rtype, [rdata, ttl, time.time() + ttl])
        self.cache.flush()

    def response(self, pkt):
        qname = pkt[DNSQR].qname.decode('cp1251')
        type = pkt[DNSQR].qtype
        data = self.cache.data[qname][type]
        ip = IP(dst=pkt[IP].src)
        udp = UDP(dport=53)
        rdata = data[0]
        ttl = int(data[1])
        dnsRR = DNSRR(rrname=qname, type=type, rdata=rdata, ttl=ttl)
        dns = DNS(id=pkt[DNS].id, qr=1, rd=1, ra=1, qd=pkt[DNS].qd, an=dnsRR)
        print(qname)
        send(ip / udp / dns, verbose=False)


if __name__ == '__main__':
    cache = cache.Cache("cache.txt")
    cache.init()
    try:
        Server(cache).run()
    finally:
        cache.flush()
