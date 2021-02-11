# week 2 lab 2 programming for cybersecurity gmit
# helen o'shea
#20210127
# program to calculate body mass index i.e. weight km over height in m squared. inputs in km and cm

def getBmi(weight, height):
  height /=100 # change cm to m
  bmi = weight/(height**2)
  output = print('Your height is {} meters and your weight is {} kilograms\nYour BMI is {:.2f}'.format(height, weight, bmi))
  return output

weight = float(input("Enter your weight in kilograms:"))
height = float(input("Enter your height in centimeters:"))
getBmi(weight, height)
print(getBmi(50, 160), getBmi(80, 190)) # test some values