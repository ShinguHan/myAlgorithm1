# Always recursive is confused

import time

#0,1,1,2,3,5
#1,2,3,4,5,6
def fib1(n):
    if n<=1:
        return n
    
    return fib1(n-1)+fib1(n-2)

def fib2(n):
    if n<=1:
        return n
    
    s = [0] * n
    s[1] = 1

    for i in range(2, n):
        s[i] = s[i-1] + s[i-2]

    return s[n-1]


start = time.time()

# result = fib2(3)


end = time.time()
elapsed = end - start
# print(fib1(),fib2(3))


# print(fib1(0))
# print(fib1(1))
# print(fib1(2))
# print(fib1(3))
# print(fib1(4))
# print(fib1(5))

# print(fib2(0))
# print(fib2(1))
# print(fib2(2))
# print(fib2(3))
print(fib2(4))
print(fib2(5))
# print(elapsed, fib2(0),fib2(1),fib2(2),fib2(3),fib2(4))