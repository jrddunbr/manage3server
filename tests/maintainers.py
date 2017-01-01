maintainers = {}

import simplejson as json

try:
    maintainersfilecontents = ""
    maintainersfile = open('users/maintainers.json','r')
    for line in maintainersfile:
        maintainersfilecontents = maintainersfilecontents + line
    try:
        maintainers = json.loads(maintainersfilecontents)
    except:
        print("Parse?")
except:
    print("Ack")

for server in maintainers["server"]:
    print (server)
    for person in maintainers["server"][server]:
        print ("  " + person)
        for items in maintainers["server"][server][person]:
            print("    " + items + ": " + maintainers["server"][server][person][items])
