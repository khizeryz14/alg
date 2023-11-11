def mergeSort(arr):
    if len(arr) > 1:
        leftArr = arr[:len(arr)//2]
        rightArr = arr[len(arr)//2:]
        #Split the array into two halves
        leftArr = mergeSort(leftArr)
        rightArr = mergeSort(rightArr)
        #Recursively split till broken into single element
        return merge(leftArr, rightArr)
        #Calls merge function to merge back the divided elements
    else:
        return arr #Base case

def merge(leftArr, rightArr):
    merged = []
    i, j = 0, 0

    
    while i < len(leftArr) and j < len(rightArr):
        if leftArr[i] <= rightArr[j]:
            merged.append(leftArr[i])
            i += 1
        else:
            merged.append(rightArr[j])
            j += 1
        #Comparision between two halves; storing smaller element first

    merged += leftArr[i:]
    merged += rightArr[j:]
    return merged #Returns a single sorted array


myArray = [3, 4, 6, 2, 9, 11, 7, 1]
print(mergeSort(myArray))
