# Utilitártio para facilitar cálculos sobre distribuições geométricas de probabilidade

def geom(n, p):
    return ((1 - p)**(n-1))*p

option = input("Digite 1 para calcularr a probabilidade de X assumir um único valor específico ou digite qualquer outra coisa para calcular um conjunto 1 a n de valores de X: ")

p = float(input("Qual a probabilidade de sucesso do evento? "))

if option == "1":
    n = int(input("Qual o valor de X cuja probabilidade se deseja calcular? "))
    result = geom(n, p)
    
    print(f"\nP(X = {n}) = {result} \n")
else:
    n= int(input("Até qual valor se deseja calcular as probabilidades? "))
    for i in range(1, n+1):
        result = geom(i, p)
        print(f"\nP(X = {i}) = {result} \n")

esperanca = 1 / p
var = (1-p)*(p*p)
print(f"\nEsperança = {esperanca}\n")
print(f"\nVariância = {var}\n")