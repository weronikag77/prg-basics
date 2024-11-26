import random

#arr3 = [7 for i in range(5)]

arr3 = [

]
for i in range(5):
    arr3.append(7)

print(arr3)

#arr4 = [i for i in range(1,10)]

arr4 = [

]
for i in range(1,10):
    arr4.append(i)

print(arr4)

# arr5 = [i*2 for i in range(1,10)]

arr5 = [

]
for i in range(1,10):
    arr5.append(i*2)

print(arr5)

#arr6 = [random.randint(1,20) for i in range(10)]

arr6 = [

]
for i in range(10):
    arr6.append(random.randint(1,20))

print(arr6)

#arr7 = [[] for i in range(5)]

arr7 = [

]

for i in range(5):
    arr7.append([])

print(arr7)

#arr8 = [[1 for i in range(2)] for j in range(4)]
arr8 = [

]
for j in range(4):
    for i in range(2):
        arr8.append(1)
    

print(arr8)

#arr9 = [[random.randint(1,20) for i in range(3)] for j in range(5)]
arr9 = [

]

for j in range(5):
    for i in range(3):
        arr9.append(random.randint(1,20))

print(arr9)

#15-element array filled with zeros
arr11 = [

]

for i in range(15):
    arr11.append(0)

print(arr11)

#an array with integer values in the range of <1,30>
arr12 = [

]

for i in range(1,31):
    arr12.append(i)

print(arr12)

#20-element array filled with 0 or 1 randomly

arr13 = [

]
for i in range(20):
    arr13.append(random.randint(0,1))

print(arr13)

#two dimensional array with five rows and two columns filled with False


arr14 = []
for i in range(5):
    arr14.append([])
    for j in range(2):
        arr14[i].append(False)

print(arr14)