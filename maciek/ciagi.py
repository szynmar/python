suma = 0

print("Podaj wzor a(n):")
wzor = input()
for n in range(100000):
    #skiping n = 0
    if n == 0:
        continue

    # aN = 1/n/n
    aN = eval(wzor)
    suma += aN
    if n % 1000 == 0:
        print(f"suma: {suma}")


