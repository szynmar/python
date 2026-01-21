import math

suma = 0

# print("Podaj wzor a(n):")
# wzor = input()
porcja=1000
for n in range(100*porcja):
    #skiping n = 0
    if n == 0:
        continue

    aN = 1/n/n
    # aN = eval(wzor)
    suma += aN

    if n % porcja == 0:
        print(f"suma: {suma:.10f}   aN={aN:.10f}")


epsilon=0.0001
granica2 = 1.6449238628
granica = math.pi**2/6

suma = 0
for n in range(100*porcja):
    if n == 0:
        continue

    aN = 1/n/n
    suma += aN
    if abs(granica - suma) < epsilon:
        print(f"dla n= {n} aN={aN:.10f} suma wynosi {suma:.10f}   czyli roznica to {(granica - suma):.10f}")
        break

