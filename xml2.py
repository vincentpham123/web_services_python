import xml.etree.ElementTree as ET

imput = '''
<stuff>
    <users>
        <user x="2">
            <id>001</id>
            <name>Chuck</name>
        </user>
        <user x='7'>
            <id>009</id>
            <name>Brent</name>
        </user>
    </users>
</stuff>
'''

stuff = ET.fromstring(imput)

list = stuff.findall('users/user')

print('User count:', len(list))

