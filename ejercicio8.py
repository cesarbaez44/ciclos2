'''
Programa 8

Escribir un programa que imprima todos los números pares entre dos números que 
se le pidan al usuario.
'''
limite_infe = int(input("Escribe el limite inferior: "))
limite_supe = int(input("Escribe el limite superior: "))

for i in range(limite_infe,limite_supe + 1):
    if i % 2 == 0:
        print(i)