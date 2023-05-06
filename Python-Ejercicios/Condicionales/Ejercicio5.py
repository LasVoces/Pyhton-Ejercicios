# preguntar al usuario si cumple un mínimo para tributar
# Mínimo 16 años y 1000€/mes

print('Introduce edad')
edad = int(input())

print('Salario mensual')
salario = int(input())

if edad >= 16 & salario >= 1000:
    print('Te toca tributar')
else:
    print('Te salvas de tributar')

