def segregateElements(arr):
    arr1=[]
    arr2=[]
    for i in arr:
        if i<0:
            arr2.append(i)
        else:
            arr1.append(i)

    arr[:]=arr1+arr2
    print(arr)

arr=[1, -1, 3, 2, -7, -5, 11, 6 ] 
segregateElements(arr)

def majorityElement(arr):
    maj = len(arr)//2
    dup={}
    for i in arr:
        dup[i] =dup.get(i,0) +1

        
    print(dup)
    for key,value in dup.items():
        if value >maj:
            return key
    return -1

arr=[1,1,2, 2]
print(majorityElement(arr))
