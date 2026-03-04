orak = int(input("hany orat parkoltal? "))

if orak <= 0:
    print("nincs fizetendo dijad.")
else:
    osszeg = 3 + (orak - 1) * 2
    print("fizetendo osszeg:", osszeg, "RON")