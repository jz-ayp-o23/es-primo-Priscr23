"""
Diseña un programa para determinar si un número entero es primo o no
750722
"""
#Entrada
numero = int(input("Introduzca un número: "))
def es_primo(numero):
    if numero < 2:
        return False
    for i in range(2, numero):
        if numero % i ==0:
            return False
        return True
for numero in range(1, 101):
    if es_primo(numero):
        print(f"El numero {numero} sí es primo")
    else:
        print(F"El número {numero} no es primo")


