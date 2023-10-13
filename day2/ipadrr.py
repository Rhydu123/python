import re

ipv4_pattern = r'^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$'
ip_addresses = ["192.168.1.1", "10.0.0.1", "256.0.0.1", "192.168.1", "192.168.1.1.1"]

for ip in ip_addresses:
    if re.match(ipv4_pattern, ip):
        print(ip + " is a valid IPv4 address")
    else:
        print(ip + "is not a valid IPv4 address")

