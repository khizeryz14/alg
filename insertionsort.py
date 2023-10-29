myList = [6, 9, 3, 1, 5, 4]

for i in range(1,len(myList)):
    j = i-1
    val = myList[i]
    while j>=0:

        if val < myList[j]:
            myList[j+1] = myList[j]
            myList[j] = val
        else:
            break
        j -= 1

print(myList)



