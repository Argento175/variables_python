# Tipos de variables [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejercicios de práctica numérica y consola

# Ahora los valores a operar deben ser ingresados por
# consola con la función "input" como se ve a continuación
print('Ingrese por consola el primer número decimal a operar:')
numero_1 = float(input())   # 2.75

print('Ingrese por consola el segundo número decimal a operar:')
numero_2 = float(input())   # 1.25

# Alumno: Imprima en pantalla los dos números decimales solicitados
# print(....)
print(numero_1,numero_2)
# Alumno: Calcule la suma, resta, división y multiplicación de los números ingresados
# numero_1, numero_2
# Imprima en pantalla todos los resultados con el siguiente formato de ejemplo:
# El resultado de sumar 4 y 2 es 6
# NOTA: No coloque usted los nùmeros y resultados, use las variables

# Suma
suma = (numero_1 + numero_2)            # 4.0
# Resta
resta = (numero_1 - numero_2)           # 1.5
# División
division = (numero_1 / numero_2)        # 2.2
# Multiplicación
multiplicacion = (numero_1 * numero_2)  # 3.4375

print("El resultado de sumar",numero_1,"y",numero_2,"es",suma)
print("El resultado de restar",numero_1,"y",numero_2,"es",resta)
print("El resultado de dividir",numero_1,"y",numero_2,"es",division)
print("El resultado de multiplicar",numero_1,"y",numero_2,"es",multiplicacion)