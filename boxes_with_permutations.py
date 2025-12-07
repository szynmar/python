import itertools as it
import moj_timer

max = 90
# cargo = [40,20,10,10]
cargo = [40,20,4,5,30,8,2,7,3,19,32,40,20,35,15,32,9]

with moj_timer.MojTimer("cargo") as moj:
    ile=0
    for k in range(1, len(cargo)):
        for boxKomb in it.combinations(cargo,k):
            if sum(boxKomb) == max:
                ile += 1
                print(boxKomb)

    print(ile)
