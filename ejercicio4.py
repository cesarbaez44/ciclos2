'''
Programa 4

Programa que muestre la tabla de multiplicar de los números 1,2,3,4 y 5.
'''
for i in range(1,6):
    print(f"\nTabla del {i}")
    for e in range(1,11):
        print(f"{i}x{e}={i*e}")