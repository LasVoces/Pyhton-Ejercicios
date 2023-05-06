# dado un número entero, indicamos si es primo o no


repetir = True
while (repetir):
    check = True;

    print('Números primos')
    print('Introduce número entero')
    num = int(input())

    for i in range(2,num -1):
        if num % i == 0:
            check = False;
    if check != False:
        print('El número es primo')
        repetir = False
    else:
        print('El número no es primo')
