# program that takes a positive floating point number input and outputs and approx of its square root via newtons method of square root estimation*
# helen o'shea
# 20210219

# newtons formula for square root estimation taken from https://runestone.academy/runestone/books/published/thinkcspy/MoreAboutIteration/NewtonsMethod.html
# newtons method 
# approx = number / 2
# betterApprox = (approx + number/approx)/2

number = float(input("Please enter a positive number: "))
iterations = int(input("Please enter the number of iterations: "))
# this is needed to set the number of iterations- it could be hardcoded or also added in other ways like with a set degree difference in approx/betterApprox values


# function to get approximation of square root using newtons method
def sqrt(number, iterations): 
  approx = number*0.5 # inital approximation is half the number
  
  for i in range(iterations): # compute approximation to required iterations
    betterApprox= 0.5*(approx + number/approx) # new approximation formula
    approx = betterApprox # use the new value for next iteration    
  return betterApprox

print("the approximation of the square root of {} is {} using {} iterations".format(number, sqrt(number, iterations), iterations))


