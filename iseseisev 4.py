# iseseisev 4
# Kristofer Andres
# 08.03.2022

from datetime import *

def banner(a):
    l = a.upper()
    return l

kord = 0
kordus = int(input("sisesta mitu korda tahad seda korrata: "))
reklaamlause = input("sisesta reklaamlause: ")
while kord != kordus:
    kord +=1
    print(banner(reklaamlause))
print()

def mahlapakkide_arv(a):
    l = a *0.4 /3
    return int(l)

kogus = int(input("sisesta õunte kogus: "))
print(mahlapakkide_arv(kogus))
print()

def eelarve(arv):
    summa = arv *10 +55
    return summa
inimesed = int(input("sisesta kutsutud külaliste arv: "))
kinimesed = int(input("sisesta kindlalt tulevate külaliste arv: "))
print(f"maksimum eelarve: {eelarve(inimesed)}")
print(f"miinimum eelarve: {eelarve(kinimesed)}")
print()

def tervitus(numb):
    print('Võõrustaja: "tere!"')
    print(f'Täna {numb}. kord tervitada, mõtiskleb võõrustaja')
    print('külaline: "Tere, suur tänu kutse eest!"')

kord= 0
kordus = int(input("sisesta külaliste arv: "))
while kord != kordus:
    kord +=1
    tervitus(kord)
print()


def pronksikarva_summa(m):
    
    l = 0
    for a in m:
        if int(a) == 1 or int(a) == 2 or int(a) == 5:
            l += int(a)
    return l
fail = open("mundid.txt")
print(f"pronksikarva sente on {pronksikarva_summa(fail)}")
print()


kuud = ["jaanuar", "veebruar", "märts", "aprill"]
def kuu_nimi(k):
    l = kuud[int(k)]
    return l
def kuupäev_sõnena(a):
    paev, kuu, aasta = a.split(".")
    b = f"{paev}.{kuu_nimi(kuu)}.{aasta}"
    return b
kuupaev = input("sisesta kuupäev formaadis DD.MM.YYYY")
print(kuupäev_sõnena(kuupaev))
    
    
    


