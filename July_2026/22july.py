def rotatearr(arr,d):
    
    if len(arr)<=1:
        return arr

    d %= len(arr)
    print(d)
    
    arr[:] = arr[d:]+arr[:d]
    print(arr)
    

arr=[1,2,3,4,5]
rotatearr(arr,2)
