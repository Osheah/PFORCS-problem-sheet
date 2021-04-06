# PFORCS-problem-sheet
# problem sheet for GMIT programming for Cybersecurity 2021
# Introduction
This repository contains the weekly problem sheets for GMIT's certificate in Cybersecurity Operations module programming for cybersecurity 2021 taught by Andrew Beatty. 

## How to run this code
In order to run this code you will need to have python 3 on your system.  Anaconda contains many of the packages that are required so download and install the latest version of [Anaconda](https://www.anaconda.com/products/individual) and update it. 

<code>conda update -all</code>


# Repository Structure
The gitignore file is the basic python one which ignores .git files, python system files and other checkpoints. The standard python [.gitignore](https://github.com/Osheah/PFORCS-problem-sheet/blob/main/.gitignore) files was used in the repository. 

## Semester 1

## Topic 1 Setup of the environment
### Task 1 
1. Introduce myself in teams chat. 
2. Get software on my machine. Create Github account and repository. 
3. Commit and push file to repository 
There was no coding associated with this topic. 

## Topic 2 statements
### Task 2
*Write a program that calculates somebody's Body Mass Index (BMI)*
The code for this can be found in [bmi.py](https://github.com/Osheah/PFORCS-problem-sheet/blob/main/bmi.py)

## Topic 3 state
### Task 3
*Write a program (bitcoin.py) that prints out todays bitcoin price in dollars*
The code for this can be found in [bitcoin.py](https://github.com/Osheah/PFORCS-problem-sheet/blob/main/bitcoin.py)

## Topic 4 Controlling the flow
### Task 4
*Write a program(collatz.py) that takes and input and prints out half the input if even and triple the input plus one if odd. The program should halt when output reaches 1*
The code for this can be found in [collatz.py](https://github.com/Osheah/PFORCS-problem-sheet/blob/main/collatz.py)

## Topic 5 Functions
###  Task 5
*Write a program sqrt.py that takes a positive floating point number input and outputs and approx of its square root via newtons method of square root estimation*
The code for this can be found in [squareroot.py](https://github.com/Osheah/PFORCS-problem-sheet/blob/main/squareroot.py)

## Topic 6 Files
### Task 6
*Write a program that reads in a text file and outputs the number of e's it contains. The program should taek the filename from an argument on the command line eg*
<code>$python es.py moby-dick.txt
116960</code>

The code for this can be found in [es.py](https://github.com/Osheah/PFORCS-problem-sheet/blob/main/es.py)

The text used for input can be found in [mobydick.txt](https://github.com/Osheah/PFORCS-problem-sheet/blob/main/mobydick.txt)
A file used to test the number of e's in a text was created in [es.txt](https://github.com/Osheah/PFORCS-problem-sheet/blob/main/es.txt) 

The mobydick.txt was taken from [gutenberg.org](https://www.gutenberg.org/files/2701/old/moby10b.txt)

##  Topic 7 Regex
### Task 7
The code for this can be found in [extract-url.py](https://github.com/Osheah/PFORCS-problem-sheet/blob/main/extract-url.py)

The task is to write a program that will extract the URLs from an access.log file. The access.log file is not uploaded to this directory. So in order to run this file you will need to download the access.log file from the splunk tutorial data  [tutorialdata.zip](https://docs.splunk.com/images/Tutorial/tutorialdata.zip) and extract the files. 
The particular log file used is in the directory www1 and is called  access.log. Put this file in a directory outside this repository called '../hospfcs2021/week07/access.log' to run the file. 
I did think about uploading the file to github but I thought it would be too big considering all the git versions and also the gitignore ignores log files. 

There is also an extra section that will store the URLs as a dictionary object in the list with the resource and parameter names. This can be found in [extra.py](https://github.com/Osheah/PFORCS-problem-sheet/blob/main/extra.py)


## Topic 8 Plotting
### Task 8
The code for this task can be found in [plottask.py](https://github.com/Osheah/PFORCS-problem-sheet/blob/main/plottask.py). This is a program that displays a plot of the function 
1. f(x) = x 
2. g(x) = x**2 
3. h(x) = x**3

in the range [0, 4] on the one set of axes. The ouput of this can be found in [plottask.jpg](https://github.com/Osheah/PFORCS-problem-sheet/blob/main/plottask.jpg)

## Topic 9 Pandas
### Task 9
The code for this task can be found in [sessions.py](https://github.com/Osheah/PFORCS-problem-sheet/blob/main/sessions.py) 
This is a program that finds which sessionId downloaded the most data. The stages of the code does the following
1. read the access.log into the dataframe
2. set the date time to be the index
3. use regular expressions to extract the session id from the urls and store them in a different column using the apply function
4. user groupby to get the sum of all the data downloaded by each sessionId
5. create a plot
*Extra*
extra marks are given for working out the amount of data each sessionId downloaded in any given day. 


## Topic 10 Errors
### Task 10
The code for this task can be found in [errors.py](https://github.com/Osheah/PFORCS-problem-sheet/blob/main/errors.py). 

The task was to 
*Write a bullet proof function called averageTo(aList, toIndex). The function should take in a list and an index and return the average of the numbers up to and including the toIndex in the aList*


