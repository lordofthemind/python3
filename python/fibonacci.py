def fibo(f):
    a = 0
    b = 1
    if f == 1:
        print(a)
    elif f == 2:
        print(a, b)
    else:
        print(a, b, end = " ")
        for i in range(f-2):
            c = a+b
            a = b
            b = c
            print(b ,end=" ")


fibo(5)
