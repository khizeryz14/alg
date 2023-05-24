myList = [1,3,5,1,2,19,22,13,16,99,24,51]
pos = 0
for k in range(len(myList)):
    smallest  = myList[k]
    for i in range(k,len(myList)):
        if smallest > myList[i]:
            smallest = myList[i]
            pos = i
    temp = myList[pos]
    myList[pos] = myList[k]
    myList[k] = temp

print(myList)
    