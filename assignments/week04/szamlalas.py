negativ = 0
paros = 0

while True:
    szam = int(input("adj meg szamokat"))

    if szam == 0:
        break
    if szam < 0:
        negativ += 1
    if szam % 2 == 0:
        paros += 1
print("neg szamok:", negativ)
print("paros szamok:", paros)