szam = int(input("adj meg egy szamot (0 a kilepes): "))
if szam == 0:
    print("nem adtal meg szamot.")
else:
    minimum = szam
    maximum = szam
    while True:
        szam = int(input("adj meg egy szamot (0 a kilepes): "))
        if szam == 0:
            break
        if szam < minimum:
            minimum = szam
        if szam > maximum:
            maximum = szam
    print("min:", minimum)
    print("max:", maximum)