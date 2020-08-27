def binarySearch(lst, x):
    print("were")
    high = len(lst) - 1
    low = 0 
    mid = 0
    while (low <= high):
        mid = (low+high)//2
        if (lst[mid] > x):
            high =  mid -1
        elif(lst[mid] < x):
            low = mid + 1
        else:
            return mid
    return -1


def binarySearchRecursion(lst, low, high, x):
    if high >= low:
        mid = (high + low)//2
        if lst[mid] == x:
            return mid
        elif (lst[mid] > x):
            binarySearchRecursion(lst, low, mid - 1, x)
        else:
            binarySearchRecursion(lst, mid + 1, high, x)
    else:
        return - 1

result = binarySearch([1,2,3,4,5,6,7,], 3)
print(result)
