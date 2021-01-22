#Készíts egy programot, amely egymásba ágyazott ciklusok segítségével rajzolja ki egy 5 x 5-ös mezőben az alábbi alakzatot! 

sor = 0
while sor < 5:
  oszlop = 0
  print('O', end='')
    while oszlop < 5:
      print('.', end='')
      print('')
      sor= sor +1
      oszlop = oszlop +1