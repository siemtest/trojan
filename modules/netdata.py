import socket
import os

def run(**args):

   print("[*] In netdata module.")
   ipaddress = socket.gethostbyname(socket.gethostname())
   fqdn = socket.getfqdn(ipaddress)
   hostname = socket.gethostname()
   return str("IP Address = ", ipaddress, "Host name = ", hostname, "FQDN = ", fqdn)

