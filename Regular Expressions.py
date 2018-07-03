#!/usr/bin/python
import re
import urllib.request
with urllib.request.urlopen('http://www.pythonchallenge.com/pc/def/equality.html') as response:
   html = response.read().decode('utf-8')
# line = "Cats are smarter than dogs"
#
# matchObj = re.match( r'(.*) are (.*?) .*', line, re.M|re.I)
#
# if matchObj:
#    print("matchObj.group() : ", matchObj.group())
#    print("matchObj.group(1) : ", matchObj.group(1))
#    print("matchObj.group(2) : ", matchObj.group(2))
# else:
#    print("No match!!")
search_object=re.findall(r'[^A-Z][A-Z]{3}([a-z])[A-Z]{3}[^A-Z]',html,re.M)
for result in search_object: print(result,end='')