
def minJumps(arr):
    n = len(arr)
    if arr[0] == 0:
        return -1
    maxReach = 0
    currReach = 0
    jump = 0
    for i in range(n):
        maxReach = max(maxReach, i + arr[i])

        if maxReach >= n - 1:
            return jump + 1

        # Increment the Jump as we reached the
        # Current Reachable index
        if i == currReach:

            # If Max reach is same as current index
            # then we can not jump further
            if i == maxReach:
                return -1

            # If Max reach > current index then increment
            # jump and update current reachable index
            else:
                jump += 1
                currReach = maxReach

    return -1

def getMinDiff(arr , k):

    new = []

    for i in range(len(arr)):
        if i < k -1:
            new.append(arr[i] + k)

        else:
            if arr[i] - k <0:
                continue
            else:
                new.append(arr[i] -k)

    print(new)

    dif = max(new) - min(new)
    print(dif)

    ans = arr[-1] - arr[0]

    for i in range(len(arr) -1):

        new_max = max(arr[i] + k , arr[-1] - k)
        new_min = min(arr[0] + k , arr[i+1] - k)

        if new_min <0:
            continue


        ans = min( ans, new_max - new_min)

    print(ans)

arr=[1,5,8,10]
k = 2
getMinDiff(arr,k)