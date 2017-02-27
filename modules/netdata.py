import socket
import os

def run(**args):

   print("[*] In netdata module.")
   ipaddress = socket.gethostbyname(socket.gethostname())
   fqdn = socket.getfqdn(ipaddress)
   hostname = socket.gethostname()
   netdata = (ipaddress, hostname, fqdn)
   return str(netdata)

