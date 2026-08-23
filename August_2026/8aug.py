import heapq

def kth_smallest(arr,k):
    

    a = heapq.nsmallest(k,arr)
    print(a)

    print(a[len(a)-1])

arr =[5,5,10,20]
k = 2

kth_smallest(arr,k)
