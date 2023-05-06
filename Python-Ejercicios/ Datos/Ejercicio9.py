# da cantidad a invertir, interés anual y el número de años. Muestra en pantalla el resultado final

print('Dame una cantidad a invertir')
cantidad = float(input())

print('El interés anual')
interes = float(input())

print('El número de años')
años = float(input())

contador = 0
resultado = 0

while contador <= años:
    cantidad = cantidad + (cantidad * interes) / 100
    contador = contador + 1

print('Capital al final',cantidad)