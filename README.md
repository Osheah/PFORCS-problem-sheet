# PFORCS-problem-sheet
## problem sheet for gmit programming for cybersecurity 2021
# Introduction
This repository contains the weekly problem sheets for GMIT's certificate in Cybersecurity Operations module programming for cybersecurity taught by Andrew Beatty. 
### Semister 1

# Topic 1 Setup of the environmen
## task 1 
* introduce myself in teams chat. Get software on my machine. Create Github account and repo. Commit and push file to repo.*

# Topic 2 statements
## task 2
*Write a program that calculates sombody's Body Mass Index (BMI)*
The code for this can be found in **bmi.py**
# Topic 3 state
## task 3
*Write a program (bitcoin.py) that prints out todays bitcoin price in dollars*
The code for this can be found in **bitcoin.py**

# Topic 4 Controlling the flow
## task4
*Write a program(collatz.py) that takes and input and prints out half the input if even and triple the input plus one if odd. The program should halt when output reaches 1*
The code for this can be found in **collatz.py**

# Topic 5 Functions
##  task5
*Write a program sqrt.py that takes a positive floating point number input and outputs and approx of its square root via newtons method of square root estimation*
The code for this can be found in **sqareroot.py**

# Topic 6 Files
## task6
*Write a program that reads in a text file and outputs the number of e's it contains. The program should taek the filename from an argument on the command line eg*
<code>$python es.py moby-dick.txt
116960</code>
The code for this can be found in **es.py**
The text used for input can be found in **mobydick.txt**
A file used to test the number of e's in a text was created in **es.txt** 

#  Topic 7 Regex
## task7
The code for this can be found in **extract-url.py**
The task is to write a program that will extract the URLs from an access.log file. There is also an extra section that will store the URLs as a dictonary object in the list with the resource and parameter names. This can be found in **extra.py**


# Topic 8 Plotting
## task8
The code for this task can be found in **plotask.py**. This is a program that displays a plot of the function f(x) = x, g(x) = x**2, h(x) = x**3 in the range [0, 4] on the one set of axes. The ouput of this can be found in **plottask.jpg**

# Topic 9 Pandas
# task9
The code for this task can be found in **sessions.py** This is a program that finds which sessionId downloaded the most data. The stages of the code does the following
1. read the access.log into the dataframe
2. set the date time to be the index
3. use regular expressions to extract the session id from the urls and store them in a different column using the apply function
4. user groupby to get the sum of all the data downloaded by each sessionId
5. create a plot
*Extra*
extra marks are given fror working out the amount of data each sessionId downloaded in any given day. 



