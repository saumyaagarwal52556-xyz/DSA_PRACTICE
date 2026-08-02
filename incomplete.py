# def longestSubarray(arr,k):
#     a=0
#     sum=0
#     sub =[]
#     size=[]
#     while a<= len(arr):
#         for i in range(a,len(arr)):
#             sum += arr[i]
#             sub.append(arr[i])
#             if sum >k and a<i:
#                 sum -=arr[a]
#                 sub.pop(a)
#             if sum == k :
#                 size.append(len(sub))
#                 print(sub)
#                 sub.clear()

#                 break
#         a+=1
#         print(size)

# arr=[10,5,2,7,1,-10]
# print(longestSubarray(arr,15))

def minjumps(arr):
    if len(arr)<=1:
        return 0
    if arr[0] ==0:
        return -1
    jump =0
    n=len(arr)
    index=0
    max= arr[0]

    while index >=0:
        number = arr[index]
        if number ==0:
            return -1
        
        if index+number+1 >=n:
            jump+=1
            return jump
        else:
            for j in range(index,index+number+1):
                
                if max < arr[j]:
                    max= arr[j]

        index+=max
        jump+=1
        
    return -1

arr=[3, 1, 1, 1, 10, 1]
print(minjumps(arr))
            