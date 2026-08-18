def factorial(num):
    if num ==0 or num == 1 :
        return [1]
    fact = 1
    arr=[]
    for i in range(2,num+1):
        fact *= i
    print(fact)
    while fact != 0:
        arr.append(fact %10)
        fact //=10

    arr.reverse()
    return arr

num = 5
print(factorial(num))



def subArray(arr):
    seen = {0}
    current = 0
    for i in arr:
        current += i
        if current in seen:
            return True

        seen.add(current)

    return False

    #failed case 
    # if len(arr) ==0:
    #     return False
    # if 0 in arr:
    #     return True

    # sum = arr[0]
    # maxA = max(arr)
    # minA = min(arr)
    # print(maxA,minA)
    # index = 0
    
    # for i in range(1,len(arr)):
    #     sum += arr[i]

    #     if sum == 0:
    #         return True

    #     if sum + minA ==0 :
    #         return True

    #     if sum >maxA:
    #         sum -= arr[index]
    #         index += 1
    
    # return False

arr=[-3,2,3,1,6] 
print(subArray(arr))

def rearrange(arr):

    #problem time complexity
    # arr.sort()
    # if len(arr) <=1:
    #     return arr
    # index =0
    # while index <len(arr):
    #     arr.insert(index,arr[len(arr) - 1])
    #     arr.pop()
    #     index +=2
    # return arr


    #problem space complexity O(n**2)
    # n=len(arr)
    # mid = len(arr) // 2  
    # max=[]  
    # min=[]  

    # for i in range(n):
    #     if i < mid:
    #         min.append(arr[i])
    #     else:
    #         max.append(arr[i])
    
    # arr.clear()

    # for i in range(mid):
    #     arr.append(max[len(max)-1 -i])
    #     arr.append(min[i])
    # if len(arr) != n:
    #     arr.append(max[0])
    
    # return arr

#correct solution but has space complexity O(n)

    if len(arr) <=1:
        return arr
    arr.sort()
    start = 0
    end = len(arr) -1
    a = arr.copy()
    for i in range(len(arr)):
        if i%2 ==0:
            arr[i] = a[end]
            end -=1
        else:
            arr[i] = a[start]
            start +=1
        i+=1
    return arr
   

arr= [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110]

print(rearrange(arr))