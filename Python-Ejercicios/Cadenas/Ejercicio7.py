#pregunta correo eletrónico y muestra otro correo con el mismo nombre pero con otro dominio. Ejemplo: ceu.es

print('dame un correo electrónico')
correo = input()

longitud = len(correo)
check = 0
nombreCorreo = ""
nuevoDominio = 'ceu.es'

for i in range(longitud):
    caracter = correo[i]
    if check == 0:
        nombreCorreo = nombreCorreo + caracter
        if caracter == "@":
            check = 1

nuevoCorreo = nombreCorreo + nuevoDominio

print('El nuevo correo será: ',nuevoCorreo)


