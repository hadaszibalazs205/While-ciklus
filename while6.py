#6. Feladat
#Írj egy programot, amely [1;12] intervallumon állít elő 20 darab véletlenszámot! A képernyőre kizárólag csak a 3-mal oszthatóakat írja ki, és a végén informálja a felhasználót arról is, hány darab ilyen szám volt.

import random

my_list = [];

i = 0
while i < 20:
  z = random.randint(1,12);
  my_list.append(z);
  i = i + 1
 
e = 0
while e < 20:
  if my_list[e] % 3 == 0:
    print(my_list[e])
  e = e + 1