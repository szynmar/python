produkty = []
ceny = []
koszyk = []
koszykIlosci = []

while True:
    print("-----------------")
    print("wybierz opcje:")
    print("W - wyswietl produkty")
    print("D - dodaj produkt")
    print("U - usun produkt")
    print("Z - zakupy")
    print("K - zawartosc kosza")
    print("Q - koniec")
    print("------------")
    print("-Twoj wybor? ")

    opcja = input().upper()

    if opcja == "W":
        print(f"aktualne produkty w sklepie:")
        for i in range(len(produkty)):
            print(f"'{produkty[i]}'  -- {ceny[i]} zl")
    elif opcja == "D":
        print("wprowadz nazwy i ceny produktow ('Q' konczy wprowadzanie)")
        while True:
            print("--podaj nazwe nowego produktu:")
            nowyProdukt = input()
            if nowyProdukt.upper() == 'Q':
                print(f"koniec wprowadzania (liczba produktow: {len(produkty)})")
                break
            elif nowyProdukt in produkty:
                print(f"produkt '{nowyProdukt}' juz jest w sklepie")
            else:
                print(f"--podaj cene zl dla '{nowyProdukt}':")
                cena = int(input())
                produkty.append(nowyProdukt)
                ceny.append(cena)
                print(f"dodano produkt: '{nowyProdukt}' z cena {cena}")
    elif opcja == "U":
        print("--podaj nazwe produktu do usuniecia:")
        delProdukt = input()
        if delProdukt in produkty:
            produkty.remove(delProdukt)
            print(f"usunieto produkt '{delProdukt}'")
        else:
            print(f"produktu '{delProdukt}' nie ma w sklepie")
    elif opcja == "Z":
        print("--podaj nazwe kupowanego produktu:")
        produkt = input()
        if produkt in produkty:
            indeksProduktu = produkty.index(produkt)
            cenaProduktu = ceny[indeksProduktu]
            print(f"--{produkt} kosztuje cena: {cenaProduktu} - podaj ile sztuk chcesz kupic:")
            ile = int(input())
            koszyk.append(produkt)
            koszykIlosci.append(ile)
            print(f"dodales do koszyka produkt: '{produkt}' - wartosc {ile}*{cenaProduktu}={ile*cenaProduktu}")
        else:
            print(f"produktu '{produkt}' nie ma w sklepie")
    elif opcja == "K":
        print(f"Zawartosc koszyka:")
        doZaplaty = 0
        for i in range(len(koszyk)):
            produkt = koszyk[i]
            if produkt in produkty:
                cena = ceny[produkty.index(produkt)]
                wartosc = koszykIlosci[i]*cena
                doZaplaty += wartosc
                print(f"'{koszyk[i]}'  -- wartosc {koszykIlosci[i]}*{cena}={wartosc}")
        print(f"Razem do zaplaty: {doZaplaty}")
    elif opcja == "Q":
        break

    print("press any key to continue")
    input()