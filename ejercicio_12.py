'''
Programa 12

Realizar un programa para determinar cuánto ahorrará una persona en un año, 
si al final de cada mes deposita cantidades variables de dinero; 
además, se quiere saber cuánto lleva ahorrado cada mes.
'''

total = 0
for i in range(1,13):
    ahorro = float(input(f"\nIngresa la cantidad del mes: {i}: "))
    total = ahorro + total
    print(f"Hasta ahora el total del ahorro es: {total}")