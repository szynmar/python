import random

print("lusuje 2 liczby")
losLimit=10
los1 = random.randint(1,losLimit)
los2 = random.randint(1,losLimit)

print("wylosowalem: ",los1, " i ",los2)

if los1 >= los2:
    print("wieksza to ",los1)
else:
    print("wieksza to ", los2)

los3=random.randint(1,losLimit)
print("wylosowalem jeszcze trzecia =",los3)

if los1 > los2:
    if los1 >= los3:
        print("najwieksza to",los1)
    else:
        print("najwieksza to ",los3)
elif los1 < los2:
    if los2 >= los3:
        print("najwieksza to",los2)
    else:
        print("najwieksza to ",los3)
else:
    if los1 < los3:
        print("najwieksza to ",los3)
    else:
        print("najwieksza to",los1)

#----------
maks = los1
if maks < los2:
    maks = los2
if maks < los3:
    maks = los3
print("najwieksza to",maks)


#-----------
print("------\nLosuje jeszcze 7 liczb:")
for i in range(7):
    losi=random.randint(1,losLimit)
    print("Liczba nr ",i+4," : ", losi)
    if maks < losi:
        maks = losi

print("najwieksza to ", maks)
