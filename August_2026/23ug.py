def stockBuySell(arr):
    if not arr:
        return 0
    maxi = 0

    for i in range(1,len(arr)):
        if arr[i] > arr[i-1]:
            maxi += (arr[i] - arr[i-1])
    return maxi

arr=[7, 1, 5, 3, 6, 4]

print(stockBuySell(arr))
