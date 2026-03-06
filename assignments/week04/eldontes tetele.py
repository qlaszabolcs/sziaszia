n = int(input("hany szamot olvasol be"))

nagativ_szam = False
van_100nal_nagyobb = False

for i in range(0, n):
    szam=int(input("adj egy szamot"))

    if szam < 0:
        nagativ_szam = True

    if szam > 100:
        van_100nal_nagyobb = True


print ("van negativ szam", nagativ_szam)
print ("a 100nal nagyobb szam",van_100nal_nagyobb)
