egyenleg = 1000

osszeg = int(input("mennyi penzt szeretnel felvenni? "))

if osszeg <= egyenleg:
    egyenleg = egyenleg - osszeg
    print("sikeres fenz felvetel.")
    print("uj egyenleg:", egyenleg)
else:
    print("nincs eleg penzed.")