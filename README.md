# arp-scan
This is a very simple Python ARP scanner. It uses Python 3. It can be used to determine available devices on a network. 

The script takes two arguments. 
1. Your network interface (`ens33` or `eth0`)
2. The IP or IP address range you would like to scan (`192.168.10.15` or `192.168.10.0/24`)

An example: 

```python3 arp-scan.py ens33 192.168.217.0/24```

Example expected output (different based on online devices on your network):

```
[*] Scanning...

[*] IP - MAC
192.168.217.1 - 00:50:56:c0:00:08
192.168.217.2 - 00:50:56:f7:37:a2
192.168.217.142 - 00:0c:29:76:96:d6
192.168.217.147 - 00:0c:29:bd:c1:63
192.168.217.254 - 00:50:56:e8:cd:79

[*] Scan Complete. Duration: 0:00:28.120490
```
