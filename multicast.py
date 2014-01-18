import socket
import struct
from lxml import etree

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.bind(('', 22600))
mreq = struct.pack("=4sl", socket.inet_aton("224.192.32.19"), socket.INADDR_ANY)

sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)

while True:
	xmltree = sock.recv(10240)
	root = etree.XML(xmltree)
	print xmltree
