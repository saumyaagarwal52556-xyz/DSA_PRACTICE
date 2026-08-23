import heapq

def mergeArrays(a, b):
    n=len(a)
    m=len(b)
    new= list(heapq.merge(a,b))
    a[:] = new[:n]
    b[:]= new[-m:]
    print(a,b)
    

a = [2, 4, 7, 10]
b = [2, 3]
mergeArrays(a,b)