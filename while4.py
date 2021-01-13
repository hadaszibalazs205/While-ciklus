#4. Feladat
#Írj egy programot, amely a felhasználó által meghatározott alkalommal írja ki a bekért szöveget!

szoveg = input("Kérek egy szöveget.")
szam = int(input("Kérek egy számot."))

while szam >= 0:
  print(szoveg * szam)
  break