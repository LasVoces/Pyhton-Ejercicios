# pregunta al usuario el numero de horas trabajadas y el coste/hora. Devuelve el resultado

print('Horas trabajadas')
horas = input()
print('el precio de las horas')
precio = input()

resultado = int(horas) * int(precio)        # Me coge las variables horas y precio como string así que casteo

print('El coste es:', resultado)
