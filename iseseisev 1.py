# iseseisev harjutus 1
# Kristofer Andres
# 08.03.2022

print("tere, maailm!")

aasta = 2020
liblikas = "teelehemosaiikliblikas"
lause_keskosa = ". aasta liblikas on "
lause = str(aasta)+lause_keskosa+liblikas
print(lause)

kõrgus = float(input("sisesta pilve kõrgus kilomeetrites: "))
if kõrgus >= 6:
    print("need on ülemised pilved")
else:
    print("need ei ole ülemised pilved")
    
    
inimesed = 20
kohad = 40
buss= inimesed // kohad +1
viimaneb = inimesed % kohad
if inimesed % kohad == 0:
    buss =  inimesed // kohad
    viimaneb = kohad

print(f"inimeste arv: {inimesed}")
print(f"kohtade arv: {kohad}")
print (f" busse vaja: {buss}")
print (f"viimases bussis inimesi: {viimaneb}")


