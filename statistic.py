import csv
import os

import pandas as pd
fields = ['Numbers', 'Total', 'StrongNumber','Total']#csv titles
path_to_file = "sum.csv"
df = pd.read_csv(path_to_file)
groups = df.groupby(['one', 'two', 'three', 'four', 'five', 'six', 'strong'])
one = df.pivot_table(index = ['one'], aggfunc ='size')
two = df.pivot_table(index = ['two'], aggfunc ='size')
three = df.pivot_table(index = ['three'], aggfunc ='size')
four = df.pivot_table(index = ['four'], aggfunc ='size')
five = df.pivot_table(index = ['five'], aggfunc ='size')
six = df.pivot_table(index = ['six'], aggfunc ='size')
strong = df.pivot_table(index = ['strong'], aggfunc ='size')
sumAllNumbers = int(one.append(two).append(three).append(four).append(five).append(six).sum())
print(sumAllNumbers)
numbers = []
one1 = []
two2 = []
three3 = []
four4 = []
five5 =[]
six6 = []
for i in range(1,38):
    try:
        one1.append(int(one[i]))
    except:
        one1.append( 0 )
    try:
        two2.append(int(two[i]))
    except:
        two2.append( 0 )
    try:
        three3.append(int(three[i]))
    except:
        three3.append( 0 )
    try:
        four4.append(int(four[i]))
    except:
        four4.append( 0 )
    try:
        five5.append(int(five[i]))
    except:
        five5.append( 0 )
    try:
        six6.append(int(six[i]))
    except:
        six6.append( 0 )
    numbers.append(one1[i-1]+two2[i-1]+three3[i-1]+four4[i-1]+five5[i-1] + six6[i-1])
"""test = one.append(two).append(three).append(four).append(five).append(six)"""
print(numbers[:])
"""
def checker():
    if (os.path.exists("statistic.csv")): # If the file exists, the exists() function returns True. Otherwise, it returns False.
        updateList()
    else:
        firstUse()"""


with open("statistic.csv", 'w', newline='') as csvfile:  # edit the info from the text file to a new csv file
    sumWriter = csv.writer(csvfile)
    sumWriter.writerow(fields)
    for i in range(1, 38):
        if (i<8):
            try:
                row = [i, numbers[i], i, strong[i]]
            except:
                row = [i, numbers[i], '', '']

        else:
            try:
                row = [i, numbers[i], "", ""]
            except:
                row = [i, 0 , "", ""]
        df = pd.DataFrame(row)
        sumWriter.writerow(df[0])
csvfile.close()