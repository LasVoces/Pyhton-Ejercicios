# el usuario nos da una fecha en formato dd/mm/aa y la mostramos por pantalla separada

print('Introduce fecha dd/mm/aa')
fecha = input()

check = 0
dia, mes, anno = '','',''

for i in range(len(fecha)):
    if check == 2:
        anno = anno + fecha[i]

    if check == 1:
        if fecha[i] != '/':
            mes = mes +fecha[i]
        else:
            check = 2

    if check == 0:
        if fecha[i] != '/':
            dia = dia + fecha[i]
        else:
            check = 1



print('Fecha: \nAño:', anno,'; mes:',mes,'; día')