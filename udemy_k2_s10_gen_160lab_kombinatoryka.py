import random
import itertools as it

max = 90
cargo = [40,20,4,5,30]

for kombinacja in it.combinations(cargo,3):
    print(kombinacja)
print("-"*10)
for kombinacja in it.permutations(cargo,3):
    print(kombinacja)
print("-"*10)
for kombinacja in it.combinations_with_replacement(cargo,3):
    print(kombinacja)
