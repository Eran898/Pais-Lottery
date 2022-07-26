import pandas as pd
import csv
import re
import os.path
import time
import wget as wget

fields = ['id', 'date', 'one','two','three','four','five','six', 'strong']#csv titles
urlAll = 'https://paisapi.azurewebsites.net/lotto'#
urlRecent = 'https://paisapi.azurewebsites.net/lotto/recent'#
urlById = 'https://paisapi.azurewebsites.net/lotto/byID/3200/3210'



def checker():
    if (os.path.exists("dict.csv")): # If the file exists, the exists() function returns True. Otherwise, it returns False.
        updateList()
    else:
        firstUse()


def updateDict(x):
    with open("dict.txt", 'a', newline='') as dictfile: # edit the info from the text file to a new csv file
        dictfile.write(x+'\n')
    dictfile.close()

def inDict(x):
    with open("dict.txt", 'r', newline='') as dictfile:
        for match in dictfile:
            if x == match :
                return True
            else:
                return False
    dictfile.close()

def specificDownload(x):
        csvfile = open("dict.txt", 'r')
        reader = csv.DictReader(csvfile)
        all_lines = list(reader)
        last_line = all_lines[-1]
        f = open(wget.download(urlById+last_line+"//"+x), "r")
        content = f.read()
        for match in re.finditer("_id", content):
            id = content[int(match.start()) + 5:int(match.start()) + 5 + 4]
            date = content[int(match.start()) + 88:int(match.start()) + 88 + 23]
            strong = content[int(match.start()) + 129:int(match.start()) + 130]
            numbers = content[int(match.start()) - 20:int(match.start()) - 2]
            numbers = numbers.split(",")
            numbers[0] = numbers[0].replace(':[', '')
            numbers[0] = numbers[0].replace('"', '')
            numbers[0] = numbers[0].replace('s"', '')
            numbers[0] = numbers[0].replace('s', '')
            numbers[0] = numbers[0].replace('[', '')
            numbers[5] = numbers[5].replace(']', '')
            print(id)
            print(date)
            print(strong)
            print(numbers)
            rows = [id, date, numbers[0], numbers[1], numbers[2], numbers[3], numbers[4], numbers[5], strong]
            df = pd.DataFrame(rows)
        csvfile.close()
        f.close()

def firstUse():
    f = open(wget.download(urlAll),"r")  # open the text file with all the lottory info url: https://paisapi.azurewebsites.net/lotto
    content = f.read()
    time.sleep(2)
    flag = True
    with open("dict.txt", 'w', newline='') as dictfile: # edit the info from the text file to a new csv file
        csvwriter = csv.writer(dictfile)
        # writing the fields
    for match in re.finditer("_id", content):
        with open("sum.csv", 'a', newline='') as csvfile:  # edit the info from the text file to a new csv file
            sumWriter = csv.writer(csvfile)
            while(flag):
                sumWriter.writerow(fields)
                flag = False
            id = content[int(match.start())+5:int(match.start())+5+4]
            date = content[int(match.start())+88:int(match.start())+88+23]
            strong = content[int(match.start())+129:int(match.start())+130]
            numbers = content[int(match.start())-20:int(match.start())-2]
            numbers = numbers.split(",")
            numbers[0] = numbers[0].replace(':[', '')
            numbers[0] = numbers[0].replace('"', '')
            numbers[0] = numbers[0].replace('s"', '')
            numbers[0] = numbers[0].replace('s', '')
            numbers[0] = numbers[0].replace('[', '')
            numbers[5] = numbers[5].replace(']', '')
            print(id)
            print(date)
            print(strong)
            print(numbers)
            rows = [id, date, numbers[0], numbers[1], numbers[2], numbers[3], numbers[4], numbers[5], strong]
            df = pd.DataFrame(rows)
            updateDict(rows[0])
            sumWriter.writerow(df[0])
    f.close()

def updateList():
    f = open(wget.download(urlRecent),"r")
    content = f.read()
    for match in re.finditer("_id", content):
        id = content[int(match.start())+5:int(match.start())+5+4]
        if (inDict(id) == False):
            with open("sum.csv", 'a', newline='') as csvfile:  # edit the info from the text file to a new csv file
                sumWriter = csv.writer(csvfile)
                date = content[int(match.start()) + 88:int(match.start()) + 88 + 23]
                strong = content[int(match.start()) + 129:int(match.start()) + 130]
                numbers = content[int(match.start()) - 20:int(match.start()) - 2]
                numbers = numbers.split(",")
                numbers[0] = numbers[0].replace(':[', '')
                numbers[0] = numbers[0].replace('"', '')
                numbers[0] = numbers[0].replace('s"', '')
                numbers[0] = numbers[0].replace('s', '')
                numbers[0] = numbers[0].replace('[', '')
                numbers[5] = numbers[5].replace(']', '')
                print(id)
                print(date)
                print(strong)
                print(numbers)
                rows = [id, date, numbers[0], numbers[1], numbers[2], numbers[3], numbers[4], numbers[5], strong]
                df = pd.DataFrame(rows)
                updateDict(rows[0])
                sumWriter.writerow(df[0])
    f.close()

