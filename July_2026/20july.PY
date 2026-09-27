
def maxSubarraySum(arr):
    total = 0
    maximum = float('-inf')
    a=0

    for i in range(a,len(arr)):
        total += arr[i]

        if total > maximum:
            maximum = total

        if total <0:
            total = 0
            

    return maximum


arr=[-2, 1, -3, 4, -1, 2, 1, -5, 4]

print(maxSubarraySum(arr))
