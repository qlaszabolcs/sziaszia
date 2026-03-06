eredmenyek = [45, 78, 90, 32, 67, 50, 98, 44]

osszeg = 0
van_sikeres = 0
legjobb_eredemy = 0
van_elegtelen = False

for e in eredmenyek:
    osszeg += e

    if e < 50:
        van_elegtelen = True

    if e >= 50:
        van_sikeres += 1

    if e > legjobb_eredemy:
        legjobb_eredemy = e


atlag = osszeg/len(eredmenyek)

print("atlag" ,atlag)
print("sikeres" ,van_sikeres)
print("legjobb" ,legjobb_eredemy)
print("van_elegtelen" ,van_elegtelen)