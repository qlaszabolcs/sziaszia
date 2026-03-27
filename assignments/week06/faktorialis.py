szam = int(input("adj meg egy egesz szamot: "))

faktorialis = 1

if szam <= 0:
    faktorialis = 0
else:
    for i in range(1, szam + 1):
        faktorialis *= i

print("a szamod faktorialisa:", faktorialis)