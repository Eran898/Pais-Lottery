import csv
import os

import pandas as pd
fields = ['Numbers', 'Total', 'StrongNumber','Total']#csv titles
fieldsAvrage = ['Numbers', 'avrage']
path_to_file = "sum.csv"
df = pd.read_csv(path_to_file)
data= pd.read_csv("sum.csv")
groups = df.groupby(['one', 'two', 'three', 'four', 'five', 'six', 'strong'])
one = df.pivot_table(index = ['one'], aggfunc ='size')
two = df.pivot_table(index = ['two'], aggfunc ='size')
three = df.pivot_table(index = ['three'], aggfunc ='size')
four = df.pivot_table(index = ['four'], aggfunc ='size')
five = df.pivot_table(index = ['five'], aggfunc ='size')
six = df.pivot_table(index = ['six'], aggfunc ='size')
strong = df.pivot_table(index = ['strong'], aggfunc ='size')
numbers = []
one1 = []
two2 = []
three3 = []
four4 = []
five5 =[]
six6 = []
def updateStatistics():
    sum = 0
    sumStrong = 0
    for j in range (1,38):
        sumall = 0
        for i in range(1,len(data)):
            if(int(data.one[i])==j ):
                sumall +=1
            if (int(data.two[i]) == j):
                sumall += 1
            if (int(data.three[i]) == j):
                sumall += 1
            if (int(data.four[i]) == j):
                sumall += 1
            if (int(data.five[i]) == j):
                sumall += 1
            if (int(data.six[i]) == j):
                sumall += 1
        numbers.insert(j,sumall)




    with open("statistic.csv", 'w', newline='') as csvfile:  # edit the info from the text file to a new csv file
        sumWriter = csv.writer(csvfile)
        sumWriter.writerow(fields)
        for i in range(1, 38):
            if (i<8):
                try:
                    row = [i, numbers[i-1], i, strong[i]]
                    sum = sum + numbers[i-1]
                    sumStrong = sumStrong + strong[i]
                except:
                    row = [i, numbers[i-1], '', '']

            else:
                try:
                    row = [i, numbers[i-1], "", ""]
                    sum = sum + numbers[i-1]
                except:
                    row = [i, 0 , "", ""]
            df = pd.DataFrame(row)
            sumWriter.writerow(df[0])
        csvfile.close()

    with open("avrageStrong.csv", 'w', newline='') as csvfile:  # edit the info from the text file to a new csv file
        sumWriter = csv.writer(csvfile)
        sumWriter.writerow(fieldsAvrage)
        for i in range(1, 8):
            row = [int(i), strong[i]/sumStrong]
            df = pd.DataFrame(row)
            sumWriter.writerow(df[0])
        csvfile.close()

    with open("avrage.csv", 'w', newline='') as csvfile:  # edit the info from the text file to a new csv file
        sumWriter = csv.writer(csvfile)
        sumWriter.writerow(fieldsAvrage)
        for i in range(1, 38):
            row = [i, numbers[i - 1]/sum]
            df = pd.DataFrame(row)
            sumWriter.writerow(df[0])
        csvfile.close()