
def getPair(arr):
    pair =[]
    seen = set()
    created = set()

    for i in arr:
        target = -i
        if target in seen :
            n= abs(i)
            
            if (-n,n) not in created:
                pair.append([-n,n])
                created.add((-n,n))
        
        seen.add(i)

    pair.sort()
    return pair

a=[2, -2, 2, -2,0,0]
print(getPair(a))
