# pide un peso (kg) y estatura (metros) y calcula el índice de masa corporal y lo almacena en una variable.
# mostrará en pantalla el índice obtenido con dos decimales

# el índice de masa corporal es peso / altura^2

print('CALCULADORA DE PESO CORPORAL')

print('Dame un peso (kg)')
peso = float(input())                    # Me los continua cogiendo mal

print('Dame la altura (m)')
altura = float(input())

imc = peso / (altura**2)

print('El indice de masa corporal es:',round(imc,2))        # empleamos round() para redondear la variable
