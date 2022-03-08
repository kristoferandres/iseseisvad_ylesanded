# iseseisev 2
# Kristofer Andres
# 08.03.2022
import random

kordi = int(input("Sisesta mitu korda äratus heliseb: "))
kord = 0
while kordi != kord:
    print("tõuse ja sära!")
    kord +=1
print()
    
ringid = int(input("Seisesta ringide arv: "))
kord = 0
p=0
juurde=2
kordus = ringid // juurde
while kord != kordus:
    p += juurde
    juurde += 2
    kord +=1
print(p)
print()

arv= int(input("Sisesta täringute arv: "))

kord= 0
while arv != kord:
    numb = random.randint(1, 6)
    kord += 1
    print(numb)

nisuteri = 1
ruut= int(input("Sisesta mitmes ruut: "))
while kord != ruut:
    nisuteri *= 2
    kord +=1
print(nisuteri)
print()


oun= 14
mitu= int(input("Mitu pöialpoissi tahab õunu? "))
kord = 0
while kord != mitu:
    i = random.randint(1,2)
    print(i)
    oun -= i
    mitu -=1
print(f"lumivalgekesele jäi {oun}")

