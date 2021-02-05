#write a program that prints out today's bitcoin price in dollars
# helen o'shea
# 20210203
import requests

def getBitcoin():
  url = "https://api.coindesk.com/v1/bpi/currentprice.json"
  req = requests.get(url)
  jsonData = req.json()
  codes = []
  bitcoin = jsonData['bpi']
  for code in bitcoin: # loop through the currencies and put them in a list
    codes.append(code)
  for code in codes: # loop over the list of currencies and pull out the rate_float value
    output =print('The bitcoin price in {} is {:.2f}'.format(code, bitcoin[code]['rate_float'] ))  
  return output
getBitcoin()    # test output



