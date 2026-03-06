szamok = [7, -2, 11, 8, -5, 10]

pozitiv = []
paros = []
paratlan = []

for szam in szamok:
    if szam > 0:
        pozitiv.append(szam)

    if szam % 2 == 0:
        paros.append(szam)
    else:
        paratlan.append(szam)

print("pozitiv:", pozitiv)
print("paratlan:", paratlan)
print("paros:", paros)