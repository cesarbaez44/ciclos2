'''
Programa 2

Crea un programa que permita adivinar un número. La aplicación genera un 
número aleatorio del 1 al 100. A continuación va pidiendo números y va 
respondiendo si el número a adivinar es mayor o menor que el introducido,
a demás de los intentos que te quedan (tienes 10 intentos para acertarlo). 
El programa termina cuando se acierta el número (además te dice en cuantos 
intentos lo has acertado), si se llega al limite de intentos te muestra el 
número que había generado.
Para genear un número entero aleatorio se utiliza la función randint
del paquete random

import random
aleatorio = random.randint(limite_inf, limite_sup)
'''
import random

def adivina_el_numero():
    numero_a_adivinar = random.randint (1, 100)
    intentos_restantes = 10

    print("Adivina el número")
    print("Tienes 10 intentos para adivinarlo.")

    while intentos_restantes > 0:
        intento = int(input("Introduce tu intento: "))
        intentos_restantes -= 1

        if intento < numero_a_adivinar:
            print(f"El número es mayor que {intento}. Te quedan {intentos_restantes} intentos.")
        elif intento > numero_a_adivinar:
            print(f"El número es menor que {intento}. Te quedan {intentos_restantes} intentos.")
        else:
            print(f"¡Felicidades! Has adivinado el número {numero_a_adivinar} en {10 - intentos_restantes} intentos.")
            break

    if intentos_restantes == 0:
        print(f"Lo siento, has agotado tus intentos. El número era {numero_a_adivinar}.")


adivina_el_numero()
