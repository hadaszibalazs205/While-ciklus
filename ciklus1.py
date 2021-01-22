#Készíts egy programot, amely a felhasználótól bekér egy páros számot,majd ennek megfelelően rajzol ki a képernyőre egy pocak szerű alakzatot az alábbiak szerint! 

bekert_szám = int(input("Adj meg egy páros számot! "))
sor = 0
while sor <= bekert_szám:
  oszlop = 0
  while oszlop <= sor+1:
    print('O ', end='')
    oszlop = oszlop + 1
    print('')
    bekert_szám = bekert_szám + 1
    sor = sor + 1
    
