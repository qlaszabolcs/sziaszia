n = int(input("Hány számot szeretnél beolvasni? "))
osszeg = 0
i = 0
while i < n:
    szam = int(input("Adj meg egy számot: "))

    if szam > 0:
        osszeg = osszeg + szam
    i = i + 1
print("A pozitív számok összege:", osszeg)