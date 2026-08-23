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

#incomplete
# def maxProduct(arr):
#     maxA = arr[0]
#     product = 1

#     for i in set(arr):
#         product *= i
#         print(i,product)

#         if maxA < product: 
#             maxA = product
#             print(f"this executes {maxA}")

#         if product == 0:
#             product = 1
#     print("done")
#     return maxA

# arr = [-2,6,-3,-10,0,2]
# print(maxProduct(arr))