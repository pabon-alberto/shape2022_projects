def factorial(n):
    if (n == 1):
        return 1
    return factorial(n-1)*n

# print(factorial(5))

def fib(k):
    if k == 1 or k == 2:
        return 1
    return fib(k-1) + fib(k-2)


def fib(k, cache):
    if k == 1 or k == 2:
        return 1

    if k in cache:
        return(cache[k])
    result = fib(k-1, cache) + fib(k-2, cache)
    cache[k] = result
    return result

cache = []
print(fib(40, cache))