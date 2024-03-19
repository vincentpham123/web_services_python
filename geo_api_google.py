import urllib.request, urllib.parse
import json, ssl 

serviceurl = 'https://py4e-data.dr-chuck.net/opengeo?'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

service_url = 'http://py4e-data.dr-chuck.net/opengeo?'
while True:
    address = input('Enter Location: ')

    if len(address)<1: break
    # keep asking until they provide a real address
    address =  address.strip()
    parms = dict()

    parms['q'] = address 

    url = service_url + urllib.parse.urlencode(parms)

    print('Retrieving', url)

    uh = urllib.request.urlopen(url, context = ctx)

    data = uh.read().decode()
    
    # print('Retrieved', len(data), 'characters', data[:20].replace('\n', ' '))
    
    # need to parse into json

    try: 
        js = json.loads(data)
    except:
        js = None 

    if not js or 'features' not in js:
        print(data)
        break
    
    if len(js['features']) == 0:
        print('not found')
        print(data)
        break 
    lat = js['features'][0]['properties']['lat']
    lon = js['features'][0]['properties']['lon']
    
    print(js)
    break

   



