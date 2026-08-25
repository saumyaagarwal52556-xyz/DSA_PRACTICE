
def productExceptSelf(arr):
    product = 1
    zero_count = arr.count(0)
    res = []

    for i in arr:
        if i==0:
            continue
        product *= i
    print(product)
    for num in range(len(arr)):
        if arr[num] == 0:
            res.append(product if zero_count == 1 else 0)        
        else:
            res.append(0 if zero_count>0 else product // arr[num])

    return res

arr=[1,2,0,4]
print(productExceptSelf(arr))

def maxWater(arr):

    left = 0
    right = len(arr) -1
    result = 0

    while left <= right:
        width = right - left
        height = min(arr[left] , arr[right])
        current = width * height

        result = max(result,current)

        if arr[left] <arr[right]:
            left += 1
        else:
            right -= 1

    return result

arr=[50, 20, 20, 20, 20, 100, 20, 20, 20, 20, 50]
print(maxWater(arr))

  