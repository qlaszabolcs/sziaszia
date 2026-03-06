n = int(input("hany szamot olvasol be? "))

legnagyobb = 0
hely = 0

for i in range(n):
    szam = int(input("adj meg egy szamot: "))

    if i == 0 or szam > legnagyobb:
        legnagyobb = szam
        hely = i

print("a legnagyobb szam:", legnagyobb)
print("az indexe:", hely)