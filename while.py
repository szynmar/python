import sys
print(sys.version)

liczby = [10,43,12,48,12,11,18,98,57,28,19,27,49,19,74]

i=0;
max = len(liczby)-2

while i<max :
    print(i,liczby[i],liczby[i+1],liczby[i+2])
    if liczby[i]<=liczby[i+1] and liczby[i+1] <= liczby[i+2]:
        print("mam")
        i=max
        
    i+=1

print("---",range(5))

import random
myRandom = random.randint(0, 20)

print("Zgadnij wylosowana liczbe od 0 do 100: ")

guess = int(input())
i=1
while guess != myRandom:
    if guess < myRandom:
        print("Proba nr ",i, " - za malo")
    else:
        print("Priba nr ",i," - za duzo")

    print("Jeszcze raz:")
    guess = int(input())
    i+=1
    
print("Brawo, faktycznie wylosowalem: ", myRandom)


