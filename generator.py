import random
print(random.sample(range(1, 36), 6),",",(random.sample(range(1, 7), 1)))
import random
numbers = [0,0,0,0,0,0]
sampleMassDistStrong = (0.149140893, 0.137457045, 0.15532646, 0.135395189, 0.142268041, 0.143642612, 0.136769759)
# assume sum of bias is 1
def rollStrong(massDist):
    randRoll = random.random() # in [0,1]
    sum = 0
    result = 1
    for mass in massDist:
        sum += mass
        if randRoll < sum:
            return result
        result+=1

sampleMassDist = (0.029476616,
0.027271672
,0.027735871
,0.025646977
,0.026459325
,0.028896368
,0.025879076
,0.030288964
,0.026691424
,0.028664268
,0.030521063
,0.030985262
,0.028548219
,0.024950679
,0.027155623
,0.027155623
,0.027735871
,0.026343275
,0.025879076
,0.029244517
,0.028664268
,0.027619821
,0.027271672
,0.026227225
,0.030405013
,0.029476616
,0.027271672
,0.029012417
,0.028896368
,0.027619821
,0.026227225
,0.025995126
,0.02808402
,0.026807474
,0.02808402
,0.026807474
)
# assume sum of bias is 1
def roll(massDist):
    randRoll = random.random() # in [0,1]
    sum = 0
    result = 1
    for mass in massDist:
        sum += mass
        if randRoll < sum:
            return result
        result+=1

for z in range(12):
    num = roll(sampleMassDist)
    for x in range(6):
        while(num in numbers):
            num = roll(sampleMassDist)
        numbers[x] = num
    numbers.sort()
    print(z+1,") ",numbers," ",rollStrong(sampleMassDistStrong))



sample = (0.1, 0.1, 0.5, 0.1, 0.1, 0.1)
# assume sum of bias is 1
def rollsample(massDist):
    randRoll = random.random() # in [0,1]
    sum = 0
    result = 1
    for mass in massDist:
        sum += mass
        if randRoll < sum:
            return result
        result+=1
print(rollsample(sample))