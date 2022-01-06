# FÁJL MEGNYITÁSA OLVASÁSRA
f = open("adatok.txt", encoding="UTF-8")

# A FÁJL TELJES TARTALMÁNAK BEOLVASÁSA EGY VÁLTOZÓBA
szoveg = f.read()
print(szoveg)
f.close()

# A FÁJL TARTALMÁNAK OLVASÁSA SORONKÉNT - vigyázzunk a sor végi "\n"-re!!!
print("\nKiírom a verset másként:")
f2 = open("adatok.txt", encoding="UTF-8")
for sor in f2:
    print(sor.strip())
f2.close()

# SORONKÉNT EGY ADAT A FÁJLBAN - Tároljuk el egy sorozatban!
szamok = list()
try:
    f3 = open("busz.txt", encoding="UTF-8")
    for sor in f3:
        szamok.append(sor.strip())
    print(f"A beolvasott elemek darabszáma: {len(szamok)}")
    f3.close()
except FileNotFoundError:
    print("Nem létezik a fájl!")

# a beolvasott értékek felhasználása
for szam in szamok:
    print(szam)
