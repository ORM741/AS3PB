def factorial(a):
    res = 1
    for i in range (1, a + 1):
        res = i * res
    return res

a = int(input())
fac = factorial(a)
print (fac)