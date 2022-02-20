'''
1.2 Feladat
Készíts egy programot, amely [1;10] intervallumon generál 5 darab véletlen egész számot, és ezeket tárolja el egy listában! A program adja össze a lista elemeit, írja ki a képernyőre az összegüket és a lista elemeit!

A program csak a páros számokat adja össze!
'''

from random import randint

szamok = []
paros = []

for i in range(5):
    szamok.append(randint(1,10))

for szam in szamok:
    if szam %2 == 0:
        paros.append(szam)

print(szamok)
print(sum(paros))