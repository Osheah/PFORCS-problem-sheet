# program that reads in a text file and outputs the number of e's it contains. The program should take the filename from an argumetn on the command line
# helen o'shea
#20210228

#https://www.tutorialspoint.com/python/python_command_line_arguments.htm


# mobydick.txt taken from https://www.gutenberg.org/files/2701/old/moby10b.txt


#to run this file enter on the cli es.py mobydick.txt or es.py es.txt this will take as an argument to the countEs function the text that appears after the .py extension on the repl cli 
import sys

def countEs():
  with open(sys.argv[1], 'rt') as f: # read in the cli file as an argument with sys.argv
    text = f.read() # read the text file
    countE = text.lower().count('e') # convert the e's to lower case
    return countE  # return the number of es present in the text
#print(sys.argv[1])
print(countEs()) # print out the number of e's



