def countOccurance(arr,k):
    if len(arr) == 0:
        return 0
    n = len(arr) // k 
    print(n)
    num = 0
    dict = {}

    for i in arr:
        if i in dict:
            dict[i] += 1
        else:
            dict[i] = 1

    for key,value in dict.items():
        if value > n:
            num += 1
    print(dict)
    return num

arr= []
k=2
print(countOccurance(arr,k))

from collections import Counter
def isSubsetA(a,b):
    count1 = Counter(a)
    count2 = Counter(b)

    for elements,count in count2.items():
        if count1[elements] < count:
            return False

    return True
    
a=[2,2]
b=[2,2,2]
print(isSubsetA(a,b))