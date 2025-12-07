import random
import moj_timer

max = 90
cargo = [40,20,4,5,30,8,2,7,3,19,32,40,20,35,15,32,9]


def znajdz(k):
    box=[]
    i=k

    while i<len(cargo):
        el=cargo[i]
        if sum(box)+el < max:
            box.append(el)
        else:
            break;
        i+=1

    #print("sum=",sum(box), "box:",box)
    return sum(box)

best=0
for n in range(len(cargo)):
    new = znajdz(n)
    if new > best:
        best = new
        print(f"--- n={n}, best={best}")



# wlasciwy kod
with moj_timer.MojTimer("cargo0") as moj:
    resIdxs=[]
    for k in range(100000):
        losIdxBox=[]
        idxBox=[]
        box=[]
        n=0
        while len(losIdxBox) < len(cargo):
            losIdx = random.randint(0,len(cargo)-1)

            if not losIdx in losIdxBox:
                losIdxBox.append(losIdx)

                el=cargo[losIdx]
                if el+sum(box)<=max:
                    box.append(el)
                    idxBox.append(losIdx)

            n+=1

        if sum(box) == max:
            box.sort()
            idxBox.sort()
            sIdx="["
            for i in range(len(idxBox)):
                sIdx+=str(idxBox[i])+","
            if not sIdx in resIdxs:
                resIdxs.append(sIdx)
                print(f" n={n},sum={sum(box)}, losBox={box}, {sIdx}")

print(f"--- len(resIdxs)={len(resIdxs)}")
#print(f"resIdxs={resIdxs}")
