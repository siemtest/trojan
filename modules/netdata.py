import socket
import os

def run(**args):

   print("[*] In netdata module.")
   ipaddress = socket.gethostbyname(socket.gethostname())
   fqdn = socket.getfqdn(ipaddress)
   hostname = socket.gethostname()
   return("IP Address = ", ipaddress, "Host name = ", hostname, "FQDN = ", fqdn)

