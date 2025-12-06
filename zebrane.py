import random
import time
import functools
import itertools
import operator

print(" ----- generator i iterator ")
tab = [10,20,10,40]
genTab = (a for a in tab)
print(next(genTab), next(genTab))
for x in genTab:
    print(x)
    
itTab = iter(tab)
print()
print(f"-- iteratorem: {next(itTab)}, {next(itTab)}")
print(list(itTab))
    

print(" ----- cache funkcji ")
@functools.lru_cache()
def sil(n):
    print(f"n={n}")
    if n==0:
        return 1
    else:
        return n*sil(n-1)
   
for i in range(5):
    print(sil(i))
print(sil.cache_info())



print(" ----- Lambda ")
fPow = lambda x,y: x**y
print(fPow(4,2))

print(list(filter(lambda x: x%4==0, tab)))


print(" ----- yield (LAZY) ")
def nastLos():
    yield random.randint(0, 500)
    yield random.randint(0, 500)
    yield random.randint(0, 500)
    yield random.randint(0, 500)
 
nastLosZm=nastLos()
print(f" - luzne yieldy kolejnych los: {next(nastLosZm)}, {next(nastLosZm)}")
for i in nastLosZm:
    print(i)

print(" ----- yield kolejnych kwadratow (bez tablicy)")
def kolejneKwDoN(n):
    for i in range(n):
        yield i**2
        
for k in kolejneKwDoN(5):
    print(k)
    
print(" ----- yield kolejnej liczby z tablicy zamiast return calej tab kwadratow")
def tabKw(tabLiczb):
    for x in tabLiczb:
        yield x**2

print(" ----- yield wyliczane w locie")
for x in tabKw(tab):
    print(x)
    
    
print(" ----- itertools")
sumSeq = itertools.accumulate(tab, operator.add)
for x in sumSeq:
    print(x)
    
tabBool = [True, False, True, True]
subSeqTab = itertools.compress(tab, tabBool)
print(list(subSeqTab))
    
subSeqTab2 = itertools.filterfalse(lambda x: x%4!=0, tab)
print(list(subSeqTab2))


