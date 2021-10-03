# Utilitário para cálculos de distribuição de poisson

import math

def poisson(n, l):
    return (math.e**(-l)*l**(n))/(math.factorial(n))

option = input("Digite 1 para calcularr a probabilidade de X assumir um único valor específico ou digite qualquer outra coisa para calcular um conjunto 1 a n de valores de X: ")

l = float(input("Qual a média de sucessos no intervalo? "))

if option == "1":
    n = int(input("Qual o valor de X cuja probabilidade se deseja calcular? "))
    result = poisson(n, l)
    print(f"\nP(X = {n}) = {result} \n")
else:
    n= int(input("Até qual valor se deseja calcular as probabilidades? "))
    for i in range(n+1):
        result = poisson(i, l)
        print(f"\nP(X = {i}) = {result} \n")

