# alumnos de u ncurso divididos en dos grupos A y B de acuerdo al sexo y el nombre
# el grupo A está formado por mujeres con un nombre anterior a la M y los hombres con su nombre después de la M
# y el grupo B por el resto.
# Pregunta al usuario nombre y sexo y muestra por pantalla a donde correpsonde


grupoA = 'GRUPO A'
grupoB = 'Grupo B'

repetir = True

while repetir:
    print('Nombre del alumno\nIntroduce `salir´ para ver los alumnos introducidos y su distribución por grupos')
    nombre = input()
    if nombre != 'salir':
        print('Sexo (M: mujer; H: hombre: ')
        sexo = input()
        if nombre < 'M':
            grupoA = '\n' + nombre + ' ' + sexo
        else:
            grupoB = '\n' + nombre + ' ' + sexo

    else:
        repetir = False
print(grupoA)
print(grupoB)
