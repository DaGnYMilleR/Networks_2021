import argparse

parser = argparse.ArgumentParser()
parser.add_argument("host", type=str, help="host")
parser.add_argument("start_port", type=int, help="start port to scan")
parser.add_argument("end_port", type=int, help="end port to scan")
parser.add_argument("-t", type=bool, action="store_true", help="allow tcp, default True")
parser.add_argument("-u", type=bool, action="store_true", help="allow udp, default True")