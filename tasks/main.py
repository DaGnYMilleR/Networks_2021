import subprocess
import sys
import re
import json
import requests
from beautifultable import BeautifulTable

ip_regexp = re.compile('(\\d+\\.){3}\\d+')


def get_traceroute(hostname):
    tracert = subprocess.Popen(["tracert", hostname], stdout=subprocess.PIPE,
                               stderr=subprocess.STDOUT)
    return tracert.stdout.readline


def get_as_info(hostname):
    for line in iter(get_traceroute(hostname), ""):
        if not line:
            break
        l = line.decode('utf-8', errors='ignore').strip()
        ip = ip_regexp.search(l)
        if not ip or not l[0].isdigit():
            continue

        yield get_as_info_by_ip(ip.group(0))


def get_as_info_by_ip(ip):
    req = requests.get(f"http://ipinfo.io/{ip}/json")
    return json.loads(req.text)


def get_table(as_info):
    table = BeautifulTable()
    table.columns.header = ['№', 'IP', 'AS', 'COUNTRY']
    for i, x in enumerate(as_info):
        try:
            table.rows.append([i, x['ip'], x['org'], x['country']])
        except KeyError:
            table.rows.append([i, x['ip'], '*', '*'])
    return table


if __name__ == '__main__':
    try:
        host = sys.argv[1]
    except IndexError:
        raise ValueError(f"Enter hostname")

    print(get_table(get_as_info(host)))
