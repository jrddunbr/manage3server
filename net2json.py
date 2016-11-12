from pysnmp.hlapi import *
from time import sleep

DELAY = 1

def getData(ip, port):

    errorIndication, errorStatus, errorIndex, varBinds = next(
        getCmd(SnmpEngine(),
               CommunityData('cacti', mpModel=0),
               UdpTransportTarget((ip, 161)),
               ContextData(),
               ObjectType(ObjectIdentity('IF-MIB', 'ifSpeed', port)),
               ObjectType(ObjectIdentity('IF-MIB', 'ifInOctets', port)),
               ObjectType(ObjectIdentity('IF-MIB', 'ifOutOctets', port)))
    )
    return varBinds

data = getData("128.153.145.251",1)
sleep(DELAY)
data2 = getData("128.153.145.251",1)
print("Speed: " + str(data[0][1]) + " b/s")
up = ((int(data2[1][1]) - int(data[1][1])) * 8 * 100) / (DELAY * int(data[0][1]))
down = ((int(data2[2][1]) - int(data[2][1])) * 8 * 100) / (DELAY * int(data[0][1]))
print("Percent upload used: " + str(up) + "%")
print("Percent download used: " + str(down) + "%")

output = """{
  "data":{
    "network": """

output += """
  }
}"""

#file = open(path, 'w')
#file.write(str(value))
