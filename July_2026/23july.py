def sort012(arr):
    c0 =[]
    c1=[]
    c2=[]

    for i in arr:
        if i == 0:
            c0.append(i)
        elif i ==1:
            c1.append(i)

        else:
            c2.append(i)

    return c0+c1+c2

arr=[0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1]
print(sort012(arr))

def duplicates(arr):
    seen=set()
    dup=set()

    for i in arr:
        if i in seen:
            dup.add(i)
        seen.add(i)

    return list(dup)

arr=[2, 3, 1, 2, 3,1,2,3,4,5,6,7,8,9,9,9]
print(duplicates(arr))

def findrep_mis(arr):
    seen = set(arr)
    sub=set()
    rep=set()
    mis=set()
    for i in range(1,len(arr)):
        if i not in seen:
            mis.add(i)
    

    for i in arr:
        if i in sub:
            rep.add(i)
        sub.add(i)
    
            
    arr[:]= list(rep|mis)
    return arr

arr=[1, 3, 3]
print(findrep_mis(arr))

def checkDuplicatesWithinK(arr, k):
    seen=set()

    for i,num in enumerate(arr):
        if num in seen:
            return True
        seen.add(num)
        if i>=k:
            seen.remove(arr[i-k])
    return False

arr=[6, 8, 4, 1, 8, 5, 7]
print(checkDuplicatesWithinK(arr,3))

