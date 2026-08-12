
def findUnion(a,b):
    set1 = set(a)
    set2=set(b)

    return list(set1 | set2)

def intersection(a,b):
    set1 = set(a)
    set2=set(b)

    return list(set1 & set2)

a = [2,2,3,4,5]
b = [1,1,2,3,4]

print(findUnion(a,b))
print(intersection(a,b))

def rotate(arr):

    return arr[len(arr)-1:] + arr[:len(arr)-1]

arr=[1,2,3,4,5,3,4,5,6]

print(rotate(arr))

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


def mergeOverlap(arr):
    if len(arr) == 0:
        return []

    arr.sort()

    merged = [arr[0]]

    for i in range(len(arr) - 1):

        if merged[-1][1] >= arr[i+1][0]:
            merged[-1][1] = max(merged[-1][1] , arr[i+1][1])
            

        else:
            merged.append(arr[i+1])

    print(merged)


arr= [[6, 8], [1, 9], [2, 4], [4, 7]]

mergeOverlap(arr)