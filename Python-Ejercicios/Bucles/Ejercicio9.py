# almacena la contraseña que nos da el usuario y la pedimos hasta que vuelva a repetirla

print('Introduce una contraseña')
password = input()

repetir = True
while (repetir):
    print('Introduce contraseña')
    pwd = input()

    if password == pwd:
        print('Bienvenido')
        repetir = False
    else:
        print('Contraseña erronea')