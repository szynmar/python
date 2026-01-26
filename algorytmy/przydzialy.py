import random
import os

from numpy.ma.core import append

#     |  1   2   3   4   5
#   ----------------------
#   A | 12  10   9   7   6
#   B | 15  14  14   8   9
#   C | 13  14  16  11  12
#   D |  4  15  13   9  10
#   E |  9   5   3   6  10
#

tabOld = [[12,10,9,7,6],
          [15,14,14,8,9],
          [13,14,16,11,12],
          [4,15,13,9,10],
          [9,5,3,6,10]]

def save_table(tab):
    filename = 'C:\\programy\\python\\przydzialy_dane.txt'
    with open(filename, "w") as f:
        for row in tab:
            f.write(";".join(map(str, row)) + "\n")

def load_table():
    filename = 'C:\\programy\\python\\przydzialy_dane.txt'
    with open(filename) as f:
        return [list(map(int, row[:]))
                for row in (line.strip().split(";") for line in f)]

def genRandomTable(wymiar):
    tab = []
    for i in range(wymiar):
        row = []
        for j in range(wymiar):
            row.append(random.randint(1, (30 + i*5)))
        tab.append(row)
    return tab


def wypisz(tab):
    s = "  |"
    for j in range(len(tab[0])):
        s += "   " + str(j)
    print(s)
    print("-"*(4*(1+len(tab[0]))))

    for i in range(len(tab)):
        s = str(i) + " |"
        for j in range(len(tab[i])):
            sEl = str(tab[i][j])
            if len(sEl) == 1:
                sEl = " " + sEl
            s += "  " + sEl
        print(s)
    print()

def getQuickMin(tab,dictOp):
    if len(tab) == 1:
        return [tab[0][0]]

    minV = tab[0][0]
    minR = 0
    minC = 0

    for i in range(len(tab)):
        for j in range(len(tab[i])):
            dictOp['comp']+=1
            if tab[i][j] < minV:
                minV = tab[i][j]
                minR = i
                minC = j

    subtab = getSubTab(tab, minR, minC)
    subRes = getQuickMin(subtab,dictOp)
    res = [minV]
    res.extend(subRes)
    return res

# lista (w liczbie len(tab)) najmniejszych wartosci
def getQuickBound(tab,dictOp):
    if len(tab) == 1:
        return [tab[0][0]]

    res = tab[0][:]
    dictOp['comp']+=len(res)-1
    max4 = max(res)

    for i in range(1, len(tab)):
        for j in range(len(tab[i])):
            dictOp['comp']+=1
            if tab[i][j] < max4:
                for k in range(len(res)):
                    if res[k] == max4:
                        res[k] = tab[i][j]
                        dictOp['comp']+=len(res)-1
                        max4 = max(res)
                        break

    return res


def getSubTab(tab, p, q):
    wymiar = len(tab)
    subTab = []
    if wymiar > 0:
        for i in range(wymiar):
            if i != p:
                row = []
                for j in range(wymiar):
                    if j != q:
                        row.append(tab[i][j])
                subTab.append(row)

    return subTab


def getMinResByBranchAndBound(tab, res, items, dictOp):
    wymiar = len(tab)
    if len(res) == 0:
        res=getQuickMin(tab,dictOp)

    for k in range(wymiar):
        iterItem = tab[0][k]
        subitems = items[:]
        subitems.append(iterItem)

        subTab = getSubTab(tab,0, k)
        # wypisz(subTab)

        # --- opcjonalnie dodatkowy bound
        quickBound = getQuickBound(subTab,dictOp)
        dictOp['comp']+=1
        if sum(res) <= sum(subitems)+sum(quickBound):
            continue
        # opcjonalnie dodatkowy bound   ---

        if (len(subTab) > 2):
            subitems = getMinResByBranchAndBound(subTab, res, subitems, dictOp)
        else:
            dictOp['add']+=2
            sum1 =subTab[0][0] + subTab[1][1]
            sum2 =subTab[0][1] + subTab[1][0]

            dictOp['comp']+=1
            if sum1 < sum2:
                subitems.append(subTab[0][0])
                subitems.append(subTab[1][1])
            else:
                subitems.append(subTab[0][1])
                subitems.append(subTab[1][0])

        dictOp['add']+=len(subitems)+1
        dictOp['comp']+=1
        if sum(subitems) < sum(res):
            res = subitems
            # print("@@@")
            # print(sum(res))
            # print(res)
            # wypisz(subTab)
            # print("@@@\n")

    return res

def redukcjaOMinima(tabIn,dictOp):
    tab = [row[:] for row in tabIn]
    for i in range(len(tab)):
        minWiersza = min(tab[i])
        for j in range(len(tab[i])):
            tab[i][j] -= minWiersza

    # wypisz(tab)

    for j in range(len(tab[0])):
        minKolumny = tab[0][j]
        for i in range(1,len(tab)):
            if tab[i][j] < minKolumny:
                minKolumny = tab[i][j]

        for i in range(len(tab)):
            tab[i][j] -= minKolumny

    return tab

def tabTransponowana(tab):
    tabT = [row[:] for row in tab]
    for i in range(len(tabT)-1):
        for j in range(i+1,len(tabT[i])):
            pom = tabT[i][j]
            tabT[i][j] = tabT[j][i]
            tabT[j][i] = pom

    return tabT

def redukcjaOczywisteZera(tabIn,dictOp):
    if len(tabIn) == 0:
        return

    wypisz(tabIn)
    tab = [row[:] for row in tabIn]
    tabT = tabTransponowana(tab)

    for i in range(len(tab)):
        if tab[i].count(0) == 1:
            print(f" pojednycze zero w wierszu nr {i}: {tab[i]} {tab[i].index(0)}")
            idx0 = tab[i].index(0)
            if tabT[idx0].count(0) == 1:
                print(f"  w kolumnie nr {idx0} ({tabT[idx0]}) tez jest jedno zero {tabT[idx0].index(0)}")
                print(f"  czyli znalezione to {[i,idx0]}")
                redukcjaOczywisteZera(getSubTab(tab,i,idx0),dictOp)

                return



tab=tabOld
wypisz(tab)
dictOp = {"add": 0, "comp": 0}
tab0 = redukcjaOMinima(tab,dictOp)
wypisz(tab0)
redukcjaOczywisteZera(tab0,dictOp)
# tabT = tabTransponowana(tab)
# wypisz(tabT)
# redukcjaOczywisteZera(tabT,dictOp)
# tab=getSubTab(tab, 4,4)
# tab = genRandomTable(8)
# save_table(tab)
# tab = load_table()

wypisz(tab)

dictOp = {"add": 0, "comp": 0}
# print(str(getQuickBound(tab,dictOp)))
# print(dictOp)

# print("-"*10)

# dictOp = {"add": 0, "comp": 0}
resMinL = getMinResByBranchAndBound(tab, [], [], dictOp)
print(" -- suma=" + str(sum(resMinL)) + ' dla ' + str(resMinL))
# print(dictOp)
# print("- "*10)
# wypisz(tab)
