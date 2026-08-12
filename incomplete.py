def longestSubarray(arr,k):
    a=0
    sum=0
    sub =[]
    size=[]
    while a<= len(arr):
        for i in range(a,len(arr)):
            sum += arr[i]
            sub.append(arr[i])
            if sum >k and a<i:
                sum -=arr[a]
                sub.pop(a)
            if sum == k :
                size.append(len(sub))
                print(sub)
                sub.clear()

                break
        a+=1
        print(size)

arr=[10,5,2,7,1,-10]
print(longestSubarray(arr,15))
