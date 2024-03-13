import xml.etree.ElementTree as ET

data = ''' 
<person>
    <name> Chuck </name>
    <phone type='intl'>
        734 303 4456
    </phone>
    <email hides="yes" /> 
</person>'''

tree = ET.fromstring(data)
print('Name:', tree.find('name').text)
# find looks for the tag name
# this looks for the tag 'Name' and finds the inner text
print('Attr:', tree.find('email').get('hides'))
# finds the email tag and gets the attribute called 'hide'
