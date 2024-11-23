'''
Programa que pida 10 números e imprima el promedio de estos.

Se utilizan los conceptos del programa anterior de contador y acumulador.
'''

print("Escriba 10 números: ")
sumanum = 0
for i in range(1,11):
    n = int(input("Escribe un numero: "))
    sumanum += n
    
print(f"La suma fue: {sumanum}")
prom = sumanum / 10

print(f"El promedio es: {prom}")