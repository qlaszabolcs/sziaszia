egyenleg = 1000

while True:
    tranzakcio = int(input("adj meg egy tranzakciot (0 = kilep): "))

    if tranzakcio == 0:
        break

    if egyenleg + tranzakcio < 0:
        print("nincs eleg penzed!")
    else:
        egyenleg = egyenleg + tranzakcio
        print("uj egyenleg:", egyenleg)

print("vegso egyenleg:", egyenleg)