#For Loop
sum = 0
for i in range(1, 101):
    if i%2 == 0:
        continue
    else:
        sum = sum+i
print(sum)

#While Loop
i = 1
sum2 = 0
while i < 101:
    sum2 += i
    i += 2
print(sum2)

#Array
Fruits = ["Mango", "Banana", "Jack", "Pineapple"]
for i in Fruits:
    print(i)

#function or Method
def addTowNum(a, b):
    return a+b

def subTowNum(a, b):
    return a-b

result = addTowNum(2,5)
result1 = subTowNum(5,5)
print(result)
print(result1)
