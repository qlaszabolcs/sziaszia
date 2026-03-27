def lnko(a, b):
    if b == 0:
        return a
    return lnko(b, a % b)

a = int(input("adj meg egy szamot: "))
b = int(input("adj meg egy masik szamot: "))

print(lnko(a, b))