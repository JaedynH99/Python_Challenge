import urllib.request
from collections import Counter

with urllib.request.urlopen('http://www.pythonchallenge.com/pc/def/ocr.html') as response:
   html = response.read().decode('utf-8')
print(html.find('!'))
html=html[789:]
print(html.find('!'))
for letter in html:
    if letter.isalpha():
        print(letter)
# html=html.replace(')','')
# html.replace('@','')
# html.replace('(','')
# html.replace(']','')
# html.replace('#','')
# html.replace('_','')
# html.replace('[','')
# html=html.replace('}','')
# html=html.replace('&','')
# html=html.replace('!','')
# html=html.replace('+','')
# # html=html.replace(
# counter=Counter(html)
# # print(counter)
# for key in counter.keys():
#     if counter[key]>100:
#         html=html.replace(key,'')
# print(html)