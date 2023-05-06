# Pregunta el precio float de un producto y muestra en pantalla el número de euros y céntimos del precio

# se puede hacer de dos formas. Empleando operaciones matemáticas o con cadenas. Al estar en el tema de cadenas,
# lo haremos con cadenas

#   --> No me sale bien lo de los céntimos!!! Avanzo y ya volveré después

print('dame el precio del kilo de naranjas')
precio = input()

euros, centimos = '', ''

check = 0
for i in range(len(precio)):
    if check == 0:
        euros = euros + precio [i]
        if precio [i] == ",":
            euros = precio [i]
            check = 1
    if check != 0 & check < 3:
        centimos = centimos + precio [i]
        check = check + 1

print('Son ', euros, ' con ', centimos,'centimos')

