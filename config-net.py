#!/usr/bin/python
import os
import subprocess
import yaml
import sys

#---- parse input vars
value=[]
value=str(sys.argv).split(",")

ens=value[1]
ens160=ens.replace("'","").lstrip()

ipv=value[2]
newip=ipv.replace("'","").lstrip()
vlanv=value[3]
newvlan=vlanv.replace("'","").lstrip()

#-------- get mac address for dhcp

ouput = []
result = subprocess.run(["ifconfig -a ens192 | grep ether"], shell=True, stdout=subprocess.PIPE).stdout.decode('utf-8').lstrip()


output = result.split(" ")

mac=output[1]
#print(mac)

with open ("interface-template.yml","r" ) as f:
    data = yaml.load(f, yaml.FullLoader)
    
    data["network"]["ethernets"]["ens192"]["match"]["macaddress"]= mac
    data["network"]["vlans"]["node"]["addresses"]= [newip+"/16"]
    data["network"]["vlans"]["node"]["id"]=int(newvlan)
    data["network"]["ethernets"]["ens160"]["addresses"]=[ens160+"/16"]

with open ("interface-template.yml", "w") as f:
    data1=yaml.dump(data,f,sort_keys=True)


print(mac)


