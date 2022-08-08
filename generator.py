import pandas as pd
import random

data= pd.read_csv("avrage.csv")

dataStrong= pd.read_csv("avrageStrong.csv")


numbers = [0,0,0,0,0,0]
sampleMassDistStrong = (dataStrong.avrage[0], dataStrong.avrage[1], dataStrong.avrage[2], dataStrong.avrage[3], dataStrong.avrage[4], dataStrong.avrage[5], dataStrong.avrage[6])
# assume sum of bias is 1


sampleMassDist = (data.avrage[0],
data.avrage[1]
,data.avrage[2]
,data.avrage[3]
,data.avrage[4]
,data.avrage[5]
,data.avrage[6]
,data.avrage[7]
,data.avrage[8]
,data.avrage[9]
,data.avrage[10]
,data.avrage[11]
,data.avrage[12]
,data.avrage[13]
,data.avrage[14]
,data.avrage[15]
,data.avrage[16]
,data.avrage[17]
,data.avrage[18]
,data.avrage[19]
,data.avrage[20]
,data.avrage[21]
,data.avrage[22]
,data.avrage[23]
,data.avrage[24]
,data.avrage[25]
,data.avrage[26]
,data.avrage[27]
,data.avrage[28]
,data.avrage[29]
,data.avrage[30]
,data.avrage[31]
,data.avrage[32]
,data.avrage[33]
,data.avrage[34]
,data.avrage[35]
,data.avrage[36]
)

def rollStrong(massDist):
    randRoll = random.random() # in [0,1]
    sum = 0
    result = 1
    for mass in massDist:
        sum += mass
        if randRoll < sum:
            return result
        result+=1

def roll(massDist):
    randRoll = random.random()
    sum = 0
    result = 1
    for mass in massDist:
        sum += mass
        if randRoll < sum:
            return result
        result+=1


def generator():
    for z in range(14):
        num = roll(sampleMassDist)
        for x in range(6):
            while(num in numbers):
                num = roll(sampleMassDist)
            numbers[x] = num
        numbers.sort()
        print(z+1,") ",numbers," ",rollStrong(sampleMassDistStrong))


"""if you want to see how many iterations it will be needed to guess the lottery numbers.. enter them here: and remove this line <---
num = [11, 12, 13, 16, 34, 36]
def test(array):
    total =0
    numbers = [0, 0, 0, 0, 0, 0]
    num = roll(sampleMassDist)
    while (numbers != array):
        for x in range(6):
            while(num in numbers):
                num = roll(sampleMassDist)
            numbers[x] = num
        numbers.sort()


        print( numbers, " ", rollStrong(sampleMassDistStrong))
        total += 1
    return total

print(test(num))

"""
