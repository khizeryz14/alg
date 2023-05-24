def searchVal(val):
    hash = int(val % 10000)
    if hash < 30:
        return hashMap[hash]    
    else:
        return "Error"



hashMap = [None]*30
myList = [10005, 10009, 10011, 10015, 10001, 10003, 10029, 10019]
for i in myList:
    hash = i % 10000
    hashMap[hash] = i

toFind = int(input("Enter value to find: "))
print(searchVal(toFind))

