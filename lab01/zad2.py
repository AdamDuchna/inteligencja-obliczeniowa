import math
import random
v1=[3, 8, 9, 10, 12]
v2=[8, 7, 7, 5, 6]
sumV=[]
scalV=[]
v1_length=0
v2_length=0
random_v=[]
for i in range(len(v2)):
    sumV.append(v1[i]+v2[i])
print(sumV)

for j in range(len(v2)):
    scalV.append(v1[j]*v2[j])
print(scalV)

for k in range(len(v1)):
    v1_length+=math.pow(v1[k],2)
    v2_length+=math.pow(v2[k],2)
print(math.sqrt(v1_length),math.sqrt(v2_length))

for u in range(50):
    random_v.append(random.randint(1,100))
print(random_v)
mean = sum(random_v)/50
stdev=0
max= max(random_v)
min = min(random_v)
for p in random_v:
    stdev+=math.pow(p-mean,2)
stdev=stdev/49
print(max,min,mean,stdev)

normal_v=[]
for b in random_v:
    normal_v.append(b-min/max-min)

print(normal_v)