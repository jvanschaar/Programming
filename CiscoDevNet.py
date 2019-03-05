import requests

from requests.auth import HTTPBasicAuth

def get_token():
    token = requests.post(
       'https://sandboxdnac.cisco.com/dna/system/api/v1/auth/token',
       auth=HTTPBasicAuth(
           username='devnetuser',
           password='Cisco123!'
       ),
      headers={'content-type': 'application/json'},
      verify=False,
    )
    data = token.json()
    return data['Token']
 
def get_inventory(token):
    headers = {'content-type': 'application/json',
               'X-Auth-Token': token}
    inv = requests.get('https://sandboxdnac.cisco.com/dna/intent/api/v1/network-device',
                        headers=headers,
                        verify=False)
    return inv.json()

token = get_token()
inv = get_inventory(token)
print(inv['response'][0]['softwareVersion'])