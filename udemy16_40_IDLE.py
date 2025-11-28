print("jo")
from datetime import date
dzis = date.today()
print("Data:")
print(dzis)
#taki "press any key"

classroom="Matma:104".lower()
print(classroom)

print("elementy listy", classroom.split(":"), sep=":")
print(len(classroom.split(":")))

#ze zlamaniem lini
print("drugi 'find' dla 'a' w ", classroom, "to:", \
      classroom.find("a", classroom.find("a")+1))

sliczba="1234.5"
print(sliczba.isdigit())
print(sliczba.isdecimal())

print(float(sliczba)+1)
print(sliczba+str(1))


t2="nowa linia to: \\n, co nie?"
print(t2)
print("pierwsze 5 znakow=", t2[:5])
print("od piatego znaku=", t2[5:])
print("od znaku 555=", t2[555:])
#print("\n")

s2liczby = "Liczba 1=%4d, a liczba 2=%2d."
print(s2liczby % (3,7))
print(s2liczby % (33,77))

print(s2liczby % (33333, 77777))
print("Liczba 1=%4d, a liczba 2=%2d." % (3,7))

duzyint=999999999999999999999999999999999999999999999999999999999999
print(duzyint+1, type(duzyint+1), sep='\n')
print((duzyint+1)/2+1, (duzyint+1)/2, sep='\n')

print(float("inf") - 999999999999999999999999999999)
print(float("inf") - float("inf"))

#wazna kolejnosc
print("True or True and False = ", True or True and False)
print("(True or True) and False = ", (True or True) and False)

slownik={"w1":"Wartosc1", "w2":"Wartosc 2"}
print("slownik:", slownik)
print("jego klucze:", slownik.keys())
print("jego wartosci: ", slownik.values())

print("Koniec")
#input("Wcisnij cos...")

