# program to read in one of splunks tutorial access.log files and get the sessionId that downloaded the most data and plot it. 
# helen oshea
# 20210319

# for reference i used some of the code from  https://raw.githubusercontent.com/andrewbeattycourseware/pforcs2021/main/code/week09-pandas/pandas-07-readlog.py

''' 
the stages of the task is to 
  1. Read the access.log into a dataframe (see lab)
  2. Set the date time to be the index (you will  need to manipulate this data, see lab)
  3. Use regular expressions to extract the session id from the URLs and store them in a different column (use the apply function, see lab)
  4. Use groupBy to get the sum of all the data downloaded by each sessionId.
  5. Create a plot of this (type of your choice)
  6. extra Work out the amount of data each sessionId downloaded in any given day
'''

# import modules
import pandas as pd
import re
import matplotlib.pyplot as plt

#1 read in the access log (which is in my local github root folder)

path = '../tutorialdata/www1/' #splunk tutorial data files are in the folder above this one on the local machine
fileName = 'access.log'
logFileName= path+fileName
print(logFileName)
# names taken from Andrew Beatty's lab for week9
colNames= colNames= ('ip',
    'dash1', 
    'userId', 
    'time', 
    'url', 
    'status code', 
    'size of response', 
    'referer', 
    'user agent', 
    'dunno'
)
df = pd.read_csv(logFileName, sep=' ', header= None, names=colNames)

print(df)
# 2.remove brackets from time field and set time field as datetime type
df['time'] = df['time'].apply(lambda x: re.search('[\w:/]+', x).group())

#print(df['time']) # just a check

df['time'] = pd.to_datetime(df['time'], format='%d/%b/%Y:%H:%M:%S')

#print (df.dtypes) # just a check

#print(df['time']) # checking
# set the datetime field as the index of the df so it can be resampled
df = df.set_index(['time']) # set the datetime field as the index
print(df.head())

# 3. Use regular expressions to extract the session id from the URLs and store them in a different column (use the apply function, see lab)
regex = r'(?<==)\w*\s' # select the stuff after the JSESSIONID=in the log file

# function from lecture lab
def getNewValue(x):
  newValue = re.search(regex, x).group().strip()
  return newValue
df['sessionId'] = df['url'].apply(getNewValue)

print(df['sessionId']) # just checking

# 4.  Use groupBy to get the sum of all the data downloaded by each sessionId.

# group by sessionId and sum size of response
sumDownloads = df[['size of response','sessionId']].groupby(['sessionId']).sum()
print(sumDownloads)

#5. Create a plot of this (type of your choice)

sumDownloads.plot(title="Sum of Download responses per sessionId", rot='vertical', figsize=(10,20))
plt.show()

# 6. extra Work out the amount of data each sessionId downloaded in any given day
# group by sessionId then resample per day and aggregate with sum
print(df.groupby(df['sessionId']).resample(rule='D').sum())










