def szamjegy_osszeg(n):
    if n == 0:
        return 0
    return abs(n % 10) + szamjegy_osszeg(n // 10)

n = int(input("Adj meg egy szamot: "))
print(szamjegyek_osszege := szamjegy_osszeg(n))