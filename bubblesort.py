import random
myList = []
for i in range(10):
    myList.append(random.randint(0, 100))

print("Unsorted list: ")
print (myList)

isSwapped = True
while isSwapped == True:
    isSwapped = False
    for i in range(len(myList)-1):
        if (myList[i] > myList[i+1]):
            temp = myList[i]
            myList[i] = myList[i+1]
            myList[i+1] = temp
            isSwapped = True
print("\nSorted list: ")
print(myList)
