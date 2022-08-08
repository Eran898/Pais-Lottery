import pandas as pd
import csv
import re
import os.path
import time
import wget as wget

fields = ['id', 'date', 'one','two','three','four','five','six', 'strong']#csv titles
urlAll = 'https://paisapi.azurewebsites.net/lotto'#
urlRecent = 'https://paisapi.azurewebsites.net/lotto/recent'#

def urlById(num , num2):# This function return the url address of the missing lottery Ids
    result = "https://paisapi.azurewebsites.net/lotto/byID/"+ str(num) + "/" + str(num2)
    return result


def deleteFiles():
    recent_path = "recent"
    if os.path.isfile(recent_path):
        os.remove(recent_path)
        print("The recent file deleted..")
    lotto_path = "lotto"
    if os.path.isfile(lotto_path):
        os.remove(lotto_path)
        print("The lotto file deleted..")


def checker():
    if (os.path.exists("dict.txt")): # If the file exists, the exists() function returns True. Otherwise, it returns False.
        updateList()
    else:
        firstUse()


def updateDict(x):
    with open("dict.txt", 'a', newline='') as dictfile: # edit the info from the text file to a new csv file
        dictfile.write(x+'\n')
    dictfile.close()

def inDict(x):
    flag = True
    with open("dict.txt", 'r', newline='') as dictfile:
        for match in dictfile:
            if (int(x) == int(match)) :
                flag = True
            else:
                flag = False
        return flag
    dictfile.close()

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
            numbers[0] = numbers[0].replace('r', '')
            numbers[0] = numbers[0].replace('s', '')
            numbers[0] = numbers[0].replace('[', '')
            numbers[5] = numbers[5].replace(']', '')
            rows = [id, date, numbers[0], numbers[1], numbers[2], numbers[3], numbers[4], numbers[5], strong]
            df = pd.DataFrame(rows)
            updateDict(rows[0])
            sumWriter.writerow(df[0])
    print("New list crated...")
    f.close()

def updateList():
    f = open(wget.download(urlRecent),"r")
    content = f.read()
    for match in re.finditer("_id", content):
        id = content[int(match.start())+5:int(match.start())+5+4]
        if (inDict(id) == False):# The lottery Id not on the dictionary list
            with open("dict.txt", 'r', newline='') as dictfile:
                last_id = dictfile.readlines()[-1]
                if(int(id)-1 == int(last_id)):
                    url = urlById(id,id)
                else:
                    url = urlById(int(last_id)+1 , id)
        else:
            return
    f.close()
    f = open(wget.download(url), "r")
    content = f.read()
    for match in re.finditer("_id", content):
        id = content[int(match.start()) + 5:int(match.start()) + 5 + 4]
        with open("sum.csv", 'a', newline='') as csvfile:  # edit the info from the text file to a new csv file
            sumWriter = csv.writer(csvfile)
            date = content[int(match.start()) + 88:int(match.start()) + 88 + 23]
            strong = content[int(match.start()) + 129:int(match.start()) + 130]
            numbers = content[int(match.start()) - 20:int(match.start()) - 2]
            numbers = numbers.split(",")
            numbers[0] = numbers[0].replace(':[', '')
            numbers[0] = numbers[0].replace('"', '')
            numbers[0] = numbers[0].replace('s"', '')
            numbers[0] = numbers[0].replace('r', '')
            numbers[0] = numbers[0].replace('s', '')
            numbers[0] = numbers[0].replace('[', '')
            numbers[5] = numbers[5].replace(']', '')
            rows = [id, date, numbers[0], numbers[1], numbers[2], numbers[3], numbers[4], numbers[5], strong]
            df = pd.DataFrame(rows)
            updateDict(rows[0])
            sumWriter.writerow(df[0])
    print("The list has been updated...")
    f.close()

