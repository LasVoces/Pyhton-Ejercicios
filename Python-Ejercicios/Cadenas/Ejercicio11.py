# pregunta nombre, precio y número de unidadeds de un producto.
# Mostrará en pantalla el nombre del producto en mayúsculas seguido del precio unitario con seis dígitos enteros
# y dos decimales, el número de unidades  el coste total con 8 dígitos
# enteros y 2 decimales

print('Introduce el producto')
producto = input()

print('Precio')
precio = float(input())

print('Número de unidades')
unidades = int(input())

producto2 = producto.upper()
precioUnitario = round(precio / unidades, 2)

print(producto2)
print('Unidades: ', unidades)
print('Precio Unitario',precioUnitario)

