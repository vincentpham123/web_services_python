import urllib.request, urllib.parse, urllib.error
import json 
url_1 = 'http://py4e-data.dr-chuck.net/comments_42.json'
url_2 = 'http://py4e-data.dr-chuck.net/comments_1677236.json'


def find_sum_url(url):
    html = urllib.request.urlopen(url).read()
    comment_data = json.loads(html)['comments']

    sum = 0
    for hash in comment_data:
        # each ioone contains a diciton with name and count

        sum += int(hash['count'])
    print(html)
    return sum 

print(find_sum_url(url_1))
print(find_sum_url(url_2))
