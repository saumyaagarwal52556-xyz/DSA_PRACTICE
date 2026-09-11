def stockBuySell(arr):
    if not arr:
        return 0
    maxi = 0
    mini = arr[0]
    for i in range(len(arr)):
        mini = min(mini,arr[i])
        curr= arr[i] - mini
        maxi = max(maxi,curr)
    return maxi
arr=[7, 1, 5, 3, 6, 4]

print(stockBuySell(arr))
