def cube(n):
    i = 1
    dct = {}
    for i in range(1,n+1):
        dct[i] = i**3
    return dct
print(cube(5))
        
