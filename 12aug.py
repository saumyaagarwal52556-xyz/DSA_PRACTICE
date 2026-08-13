
def commonelement(a,b,c):

    return sorted(list( set(a) & set(b) & set(c)))

a=[5, 5, 10]
b=[5, 5, 20]
c=[5, 5]
print(commonelement(a,b,c))
