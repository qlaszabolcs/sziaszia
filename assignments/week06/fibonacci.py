def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

n = int(input("adj meg egy szamot: "))

print("a fibonacci sorozat", n, ". eleme:", fib(n))