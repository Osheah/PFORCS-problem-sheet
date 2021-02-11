#write a program that asks user to input any positive integer and outputs the sucessive values of the following. At teach step calculate the next value by current valued halved if even and trippled +1 if odd. The progamme should end if the current value is 1
# helen o'shea
# 20210203

number = int(input("Enter a positive integer: "))


def collatz(number):
  
  while number >1: # stop when 1 is reached
    if number%2==0:      # if the number is even
      print("{:.0f}".format(number), end="\t") # i'm printing this befor ethe division to included the inputed value in the output
      number /= 2 # divide by 2
    else:       # the number is odd
      print("{:.0f}".format(number),end="\t") # i'm printing this before the calculation to include the inputed value i the output
      number =3*number+1 # triple it and add 1
  print("{:.0f}".format(number),end="\t")  # print out the last number which is 1  
collatz(number) 