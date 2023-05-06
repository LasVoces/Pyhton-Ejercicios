# el usuario introduce una lista de productos y se los mostramos por separado

print('LISTA DE LA COMPRA')
print('Introduce los productos separados por una coma')
listaCompra = input()

check = 0


producto = ''

for i in range (len(listaCompra)):

    if listaCompra[i] != ',':
        producto = producto + listaCompra[i]
    elif listaCompra[i] == ',':
        print(producto)
        producto = ''
    if i == (len(listaCompra) -1):
        print(producto)






