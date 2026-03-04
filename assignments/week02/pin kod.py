helyes_pin = "1234"
probalkozas = 0

while probalkozas < 3:
    pin = input("add meg a PIN-kodot: ")

    if pin == helyes_pin:
        print("helyes PIN!")
        break
    else:
        print("hibas PIN!")

    probalkozas = probalkozas + 1

if probalkozas == 3:
    print("tul sok hibas probalkozas!")