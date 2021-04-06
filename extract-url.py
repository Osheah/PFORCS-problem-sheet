# program to extract the urls from an access.log file
# the program should store the urls as a string in a list
# extra store the urls as a dictonary object in the list with the resource parameter names and values separated out

# helen o'shea
# 20210301
import re
fileName = '../hospfcs2021/week07/sampleAccess.log'
fileName2 = '../hospfcs2021/week07/access.log'
#fileName2 = 'access.log'
# to run this file download splunk tutorial data and extract the file and put the file in the same directory as this code and comment out fileName2 and remove the comment from the second fileName2 

regex= r'\s/.+?\s'
#regexV1 = '/[A-Za-z0-9\.\?=-]+&[A-Za-z0-9]+=[A-Z-0-9&A-Z=]+'
urlOutput = 'urlOutput.txt'
with open(fileName) as accessLog:
  with open(urlOutput, 'w') as output:
    for line in accessLog:
      urls = re.findall(regex, line)
      output.write(urls[0].strip()+'\n')
      print(urls[0].strip())



#209.160.24.63 - - [08/Feb/2021:18:22:16] "GET /product.screen?productId=WC-SH-A02&JSESSIONID=SD0SL6FF7ADFF4953 HTTP 1.1" 200 3878 "http://www.google.com" "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.46 Safari/536.5" 349
