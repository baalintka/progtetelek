import math
import random
'''eljaras,parameterben 2 szam, ezen egesz szamok közötti összeget szamolja ki az eljaras'''
def feladat(szam1,szam2):
    osszeg:int=0

    if szam1>szam2:
        i:int=szam1
        for i in range(szam2,szam1,1):
            if i%2==0:

                osszeg+=i
            szam2+=1
    elif szam1<szam2 :
        i=szam1
        for i in range(szam1,szam2,1):
            if i % 2 == 0:
                osszeg += i
            i += 1
    return (osszeg)
'''20 veletlen szam -10 es plusz 10 között'''
'''szamoldmeg hayn negativ szam van közötte
a visszateresi ertek a negativ szamok szama legyen'''
def negativ():
    i:int=0

    while i<20:
        veletlenszam:int=math.floor(random.random()*(10+10)-10)
        if veletlenszam<0:
            negativszamok:int=0
            negativszamok+=1
        i+=1
    return  negativszamok
def negativ2():
    db:int=0
    for db in range (0,20,1):
        veletlenszam: int = math.floor(random.random() * (10 + 10)-10)
        if veletlenszam < 0:
            db += 1

    return db
'''irj fuggvenyt amely general 10 db veletlen szamot, 12 és 33 között és visszater ezek összegevel'''

def veletlen():
    for i in range(0,10,1):
        veletlenszam: int = math.floor(random.random() * (33 - 12+1 )+ 12)
        osszeg:int=0
        osszeg+=veletlenszam
    return osszeg
'''irj fuggvenyt amely general 8 db veletlen szamot, 20 és 50 között és visszater ezek összegevel'''
def legnagyobbb():
    for i in range(0, 8, 1):
        veletlenszam: int = math.floor(random.random() * (50 - 20+ 1) + 20)
        big:int = 0
        if veletlenszam > big:
                big = veletlenszam

    return big
def egesz3szam():
    osszeg: int = 0
    atlag: int = 0
    for i in range(0, 3,1):
        szam:int=int(input("Kérem adjon meg egy számot: "))


        osszeg+=szam
    atlag=osszeg/3
    return atlag
def bekeres():
    db:int=0
    osszeg: int = 0
    atlag: int = 0
    szam:int=int(input("Kérem adjon meg egy számot: "))
    while szam!=0:
        if szam !=0:
            szam: int = int(input("Kérem adjon meg egy számot: "))
            osszeg+=szam
            db+=1
    atlag=osszeg/db
    return atlag
