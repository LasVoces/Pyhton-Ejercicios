# lee un numero entero positivo n y luego muestra por pantallala suma de los numeros hasta n

print('Dame un número entero')
numero: int = input()        # sigue cogiéndome los números como strings
numeroInt = int(numero)
contador = 1
suma = 0

while contador <= numeroInt:
    suma = suma + contador
    contador = contador + 1


print('La suma de los números hasta',numero,'es:',suma)