# Mini programinha python para auxiliar ao fazer cálculos tediosos e repetitivos de distribuição binomial

import math

def esperanca(fp):
    mi = 0
    for i in range(len(fp)):
        mi += i * fp[i]
    return mi

def variancia(fp, esperanca):
    e2 = 0
    for i in range(len(fp)):
        e2 += (i ** 2) * fp[i]

    variancia = e2 - (esperanca ** 2)
    return variancia

def binomio(n, k, p):
    
    comb = (math.factorial(n)) / (math.factorial(k) * math.factorial(n-k))

    b = comb * (p ** k) * ((1-p) ** (n - k))
    return b

n = int(input("Quantos ensaios serão feitos? "))
p = float(input("Qual a chance de sucesso? "))
print("\n\n\n")

fp = []
for k in range(n + 1):
    b = binomio(n, k, p)
    print(f"p(X = {k}) = {b}")
    fp.append(b)

mi = esperanca(fp)
print(f"\nA esperança é {mi}\n")

var = variancia(fp, mi)
print(f"A variância é {var}\n")

dp = math.sqrt(var)
print(f"O desvio Padrão é {dp}\n")