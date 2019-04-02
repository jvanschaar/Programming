import requests
import json

key = None

def load_key():
    fh = open('C:\\Users\\jvansch1\\Documents\\Programming\\meraki_key.py', 'r')
    global key
    key = fh.readline()
    fh.close()

load_key()

def get_networks():
    headers = {'content-type': 'application/json',
               'X-Cisco-Meraki-API-Key': key}
    inv = requests.get('https://api.meraki.com/api/v0/organizations/133277/networks',
                        headers=headers,
                        )

    return inv.json()

def get_admins():
    headers = {'content-type': 'application/json',
               'X-Cisco-Meraki-API-Key': key}
    inv = requests.get('https://api.meraki.com/api/v0/organizations/133277/admins',
                        headers=headers,
                        )

    return inv.json()

def get_orgs():
    headers = {'content-type': 'application/json',
               'X-Cisco-Meraki-API-Key': key}
    inv = requests.get('https://api.meraki.com/api/v0/organizations',
                        headers=headers,
                        )

    return inv.json()

# networks = gprint(images['response'][0]['createdTime'])et_networks()
##networks = json.dumps(get_networks(), indent=4)
##networks = get_networks()
##for network in networks:
    ##print(network['name'])
##admins = json.dumps(get_admins(), indent=4)
##print(admins)

##orgs = json.dumps(get_orgs(), indent=4)
orgs = get_orgs()
for org in orgs:
    print(org['name'])
##print(orgs)
##admins = get_admins()
##for admin in admins:
    ##print(admin['name'])


##print(networks)

##print(networks)
##for network in networks:
    ##print(network['name'])
##print(networks)
# for network in print(images['response'][0]['createdTime'])networks:
#     print(network['name'])
