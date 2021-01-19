#5. Feladat
#Írj egy programot, amely a felhasználótól páros számot kér be. Amennyiben a megadott szám páratlan, újra és újra megtörténik az adatbekérés mindaddig, amíg végül páros számot nem ad meg a felhasználó.

szam = int(input("Kérek egy páros számot. \n"))

while szam % 2 != 0:
  szam = int(input("Kérek egy páros számot. \n"))
  if szam % 2 == 0:
    print(szam)
    break