"""
A file named hosts holds hostnames and IP addresses
in format: hostname=ip
Write a program that reads the file and takes
a list of hostnames in sys.argv
Program should print the IP addresses of the hosts requested
"""
import sys

hosts = {}

with open("hosts", "r") as f:
    for line in f:        
        if not "=" in line: continue
        (hostname, ip) = line.rstrip().split('=')
        hosts[hostname] = ip

for hostname in sys.argv[1:]:
    if hosts.has_key(hostname):
        print "Found: %s => %s" % (hostname, hosts[hostname])
    else:
        print "No IP found for %s" % hostname




