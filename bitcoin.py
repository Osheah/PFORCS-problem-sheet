#write a program that prints out today's bitcoin price in dollars
# helen o'shea
# 20210203
import requests
url = "https://api.coindesk.com/v1/bpi/currentprice.json"
req = requests.get(url)
jsonData = req.json()
bitcoinUSD =jsonData['bpi']['USD']['rate']
bitcoinUSD = float(bitcoinUSD.replace(',','') ) # take out the comma to cast it as float
print('The bitcoin price is ${:.2f}'.format(float(bitcoinUSD)))
