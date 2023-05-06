# Crear tabla con franjas de la renta
# Preguntar al usuario renta y le diremos el tipo impositivo

tramos = [['Menos de 10000€', '5%'],
          ['Entre 10000€ y 20000€', '15%'],
          ['Entre 20001€ y 35000€', '20%'],
          ['Entre 35001€ y 60000€', '30%'],
          ['Más de 60000€', '45%']
          ]

tipoImpositivo = 0

for i in range(len(tramos)):
    for j in range(len(tramos[i])):
        print(tramos[i][j])

print('Introduce una renta anual')
renta = float(input())


fila = 0

if (renta < 10000):
    fila = 0
elif (renta <20000):
    fila = 1
elif (renta <35000):
    fila = 2
elif (renta > 60000):
    fila = 3

tipo = ''

# for i in range(len(tipoImpositivo)):

for i in range (len(tramos [fila][1])):
    tipoImpositivo = tramos[fila][j]
    if tipoImpositivo[i] != '%':
        tipo = tipo + tipoImpositivo[i]

print('Renta: renta', '\tTipo Impositivo: ', tipoImpositivo)
print('Tipo: ', tipo, renta / float(tipo))

