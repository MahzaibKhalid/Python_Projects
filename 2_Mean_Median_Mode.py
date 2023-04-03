#How we can find the mean
import math
list1=[1,2,3,4,5,6,7,8,9,10]
mean= sum(list1)/len(list1)

print("Mean:",mean)


list2 = [12, 16, 20, 20, 12, 30, 25, 23, 24, 20]
list2.sort()

if len(list2) % 2 == 0:
    m1 = list2[len(list2)//2]
    m2 = list2[len(list2)//2 - 1]
    median = (m1 + m2)/2
else:
    median = list1[len(list2)//2]
print("Median",median)

list3=[12,12,12,12,34,5,67,86,43,55]
frequency ={}

for i in list3:
    frequency.setdefault(i,0)
    frequency[i]+=1
print(frequency.keys())
print(frequency.values())

frequent = max(frequency.values())
for i,j in frequency.items():
    if j == frequent:
        mode = i
        
print(mode)