# az adatokat 3 listában fogom eltárolni
cim = list()
ev = list()
nezo = list()

# a fájl megnyitása és az olvasás
fajl = open("mozi.txt", encoding="UTF-8")
for sor in fajl:
    darabok = sor.strip().split(";")
    cim.append(darabok[0])
    ev.append(darabok[1])
    nezo.append(darabok[2])
fajl.close()

# ellenőrzés
print(f"A címek száma: {len(cim)}")
print(f"A évek száma: {len(ev)}")
print(f"A nézőszámok száma: {len(nezo)}")

print(cim)
print(ev)
print(nezo)

print(f"{cim[1]}: {ev[1]}")
for i in range(0, len(cim)):
    print(cim[i], ev[i])