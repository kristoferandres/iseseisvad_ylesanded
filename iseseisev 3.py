# iseseisev 3
# Kristofer Andres
# 08.03.2022

from datetime import *

fail = open("rebased.txt", encoding="UTF-8")

vast = []

for a in fail:
    vast.append(int(a))
fail.close()
    
aasta = int(input("Palun sisestage, millise aasta andmeid vajate: "))
mitmes = aasta - 2011
print(f"{aasta}. aastal oli vastuvõetuid {vast[mitmes]}")

ringid = int(input("Seisesta ringide arv: "))
kord = 0
p=0
juurde=2
kordus = ringid // juurde
for kord in range (0, kordus):
    p += juurde
    juurde += 2
    kord +=1
print(p)
print()

fail = open("konto.txt")
for  a in fail:
    if float(a)>= 0:
        print(a, end="")
print()

kord = 0
fail = "edm.txt"
info = open(fail)
for laul in info:
    kord +=1
    print(kord, end=". ")
    print(laul, end="")
print()
valik = int(input("Sisesta valitud laulu number: "))

info = open(fail)
kord = 0
for laul in info:
    kord +=1
    if kord == valik:
        print(kord, end=". ")
        print(laul, end="")
        
print()
        
fail = "nimekiri.txt"
nimed = open(fail)
kord = 0
kuup = datetime.now().day
for nimi in nimed:
    kord += 1
    if kord == kuup:
        print(nimi)


