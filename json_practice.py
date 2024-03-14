import json

data = '''
{
    "name" : "chuck",
    "phone": {
        "type": "intl",
        "number" : "408 123123"
    },
    "email": {
        "hide": "yes"
    }
}
'''

info = json.loads(data)
print('Name: ', info['name'])
print('Phone: ', info['phone']['number'])