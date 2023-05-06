# dada una graduación de productividad, el usuario introducirá el grado
# y, con una base de 2400€, devolveremos lo que proceda

tablaProductividad = [['Incaceptable', 0],
                      ['Aceptable', 0.4],
                      ['Meritorio', 0.6]
                      ]

importeMax = 2400
primaProductividad = 0
listaGrados = ""

for i in range(len(tablaProductividad)):
    listaGrados = listaGrados + ", " + tablaProductividad[i][0]

print(listaGrados)
print ('Indica un grado de productividad')
gradoProductividad = input()


for i in range(len(tablaProductividad)):
    if gradoProductividad == tablaProductividad[i][0]:
        multiplicadorProductividad = tablaProductividad[i][1]
        primaProductividad = importeMax * multiplicadorProductividad

print('Prima de productividad:', primaProductividad)