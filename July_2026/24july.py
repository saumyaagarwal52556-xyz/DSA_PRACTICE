def firstSearch(arr, k):
    #using binary search
    left=0
    right=len(arr)-1
    result = -1
    while left<=right:
        mid = (left+right) //2
        if k<arr[mid]:
            right = mid-1
        elif k >arr[mid]:
            left = mid+1
        else:
            result= mid
            right = mid-1
    return result
arr=[1 ,1, 1, 2, 2, 3, 3, 3, 3, 3, 3, 4, 4, 4, 5, 5 ]
print(firstSearch(arr,3))

def search(arr, x):
    for i,num in enumerate(arr):
        if num == x:
            return i
    return -1

arr=[10,8,30,4,5]
print(search(arr,20))

def perfectsum(arr,target):
    sub=[]
    size=[]
    a=0
    sum=0
    while a<len(arr):
        for i in arr:
            sum +=i
            sub.append(i)
            if sum> target:
                break
            if sum== target:
                print(sub)
                size.append(len(sub))
                sub.clear()
                break
        a+=1
    return len(size)
arr=[5,2,3,10,6,8]
print(perfectsum(arr,10))
