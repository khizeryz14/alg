myList = [2,5,9,11,19,23,55,101,123,150]

toFind = int(input("Enter number to be searched: "))

import math
low = 0
high = len(myList)-1

while low <= high:
    mid = math.floor((low+high)/2)
    if myList[mid] == toFind:
        print("Value",toFind,"at position",mid)
        break
    elif myList[mid] > toFind:
        high = mid - 1
    elif myList[mid] < toFind:
        low = mid + 1 

    
            


