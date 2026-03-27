def fordit(n):
    if n < 10:
        print(n, end="")
    else:
        print(n % 10, end="")
        fordit(n // 10)

n = int(input("Adj meg egy szamot: "))
fordit(abs(n))
print()