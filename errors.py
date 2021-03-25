# an error controled function that takes in a list and index and returns the average upto and including the index paramater in the list. Use error control and meaningful logging. Test the code either in another moduele or in this module
# helen o'shea
# 20210325

import logging
logging.basicConfig(level=logging.DEBUG)

aList = [1, 2, 3, 4, 5, 90, 67, 38, 28, 41]
toIndex = 10.5

# check if aList has valid content
def checkList(aList):
  checkListVal = True
  for i in aList:
    if isinstance(i, str):
      print("The list contains a string and is invalid")
      checkListVal = False
  return checkListVal    

def checkIndex(toIndex):
  checkIndexVal = True
  if type(toIndex)== str:
    print("The value cannot be a string")
    checkIndexVal = False
  elif type(toIndex) != int:
    print("the toIndex value must be a non negative integer")    
    checkIndexVal = False
  elif toIndex < 0:
    print("The index cannot be negative")
    checkIndexVal = False
  elif toIndex > len(aList):
    print("The toIndex is longer that the list length\nenter a value with the length of the list")  
    checkIndexVal = False
  return checkIndexVal  
  
  

def averageTo(aList, toIndex):
  # adapted from https://www.geeksforgeeks.org/python-sectional-subset-sum-in-list/
  sumToIndex = [sum(aList[x : toIndex+1])
   for x in range(0, len(aList), toIndex+1)]
  avgToIndex = sumToIndex[0]/(toIndex+1)  
  return avgToIndex



if __name__ =='__main__':
  # test cases
  '''
  return0 = 1
  return1=1.5
  return2=2
  return3=2.5
  return4=3
  return5= 17.5
  assert averageTo(aList, 0) == return0
  assert averageTo(aList, 1) == return1
  assert averageTo(aList, 2) == return2
  assert averageTo(aList, 3) == return3
  assert averageTo(aList, 4) == return4
  assert averageTo(aList, 5) == return5
  '''
  checkListVal = checkList(aList)
  checkIndexVal = checkIndex(toIndex)
  #print(checkListVal)
  #print(checkIndexVal)
  if checkListVal == True and checkIndexVal ==True:
    print(averageTo(aList, toIndex))
  else:
    print("check your inputs")  

  


