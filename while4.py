"""4. Feladat
Írj egy programot, amely a felhasználó által meghatározott alkalommal írja ki a bekért szöveget!"""

szoveg = input()
szam = int(input())

while szam < 0:
  print(szoveg * szam)
  szam = szam - 1
