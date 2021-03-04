# program to extract the urls from an access.log file
# extra: program to store the urls as a dict object with the resources and parameter names and values seperated out.
# the program should store the urls as a string in a list
# extra store the urls as a dictonary object in the list with the resource parameter names and values separated out

# helen o'shea
# 20210301

import re
import json
fileName = '../hospfcs2021/week07/sampleAccess.log'
fileName2 = '../hospfcs2021/week07/access.log'
regex = r'("\w+\s/)(?P<resourse>[a-z\.]+)\?(?P<IdType>[a-zA-Z]+)=(?P<Id>[A-Z0-9-]+)&JSESSIONID=(?P<JSESSIONID>[A-Za-z0-9]+)'
urlOutput = 'urlOutput.json'
with open(fileName) as accessLog:
  with open(urlOutput, 'w') as output:
    for line in accessLog:      
      urls = re.search(regex, line)
      json.dump({'resourses':urls.group('resourse'), 'parameters':{ 'idType':urls.group('IdType'), 'Id':urls.group('Id'), 'JSESSIONID': urls.group('JSESSIONID')} }, output, indent=2)


#209.160.24.63 - - [08/Feb/2021:18:22:16] "GET /product.screen?productId=WC-SH-A02&JSESSIONID=SD0SL6FF7ADFF4953 HTTP 1.1" 200 3878 "http://www.google.com" "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.46 Safari/536.5" 349

## to do comments, try n except , get it to work on full access log 
