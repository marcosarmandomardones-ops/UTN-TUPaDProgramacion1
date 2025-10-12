# Práctico 2: Funciones en Python

# Ejercicio N°1: 
# 1. Crear una función llamada imprimir_hola_mundo que imprima por pantalla el mensaje: “Hola Mundo!”. Llamar a esta función desde el programa principal.
# Definición de la función
def imprimir_hola_mundo():
    # La instrucción que imprime el mensaje
    print("Hola Mundo!")

# Llamada a la función
imprimir_hola_mundo()

# Ejercicio N°2: 
#2. Crear una función llamada saludar_usuario(nombre) que reciba como parámetro un nombre y devuelva un saludo personalizado. Por ejemplo, si se llama con saludar_usuario("Marcos"), deberá devolver: “Hola Marcos!”. Llamar a esta función desde el programa principal solicitando el nombre al usuario.
# Definimos una función
def saludar_usuario(nombre):
    # La función devuelve un saludo 
    return (f"Hola {nombre}!")
# Programa principal:
# Solicitamos al usuario que ingrese su nombre
nombre_usuario = input("Ingrese su nombre: ")
# Llamamos a la función y pasando como argumento el nombre ingrnesado
saludo = saludar_usuario(nombre_usuario)
# Mostramos por pantalla el saludo devuelto por la función
print(saludo)

# Ejercicio N°3:
# 3. Crear una función llamada informacion_personal(nombre, apellido, edad, residencia) que reciba cuatro parámetros e imprima: “Soy [nombre] [apellido], tengo [edad] años y vivo en [residencia]”. Pedir los datos al usuario y llamar a esta función con los valores ingresados.
# Definimos la función:
def informacion_personal(nombre, apellido, edad, residencia):
    # Devolvemos un texto 
    return (f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")
# Programa principal
# Solicitamos los datos al usuario
nombre_usuario = input("Ingrese su nombre: ")
apellido_usuario = input("Ingrese su apellido: ")
edad_usuario = int(input("Ingrese su edad: "))  
residencia_usuario = input("Ingrese su lugar de residencia: ")
# Llamamos a la función con los valores ingresados por el usuario y guardamos el resultado en una variable
informacion = informacion_personal(nombre_usuario, apellido_usuario, edad_usuario, residencia_usuario)
# Mostramos el mensaje por pantalla
print(informacion)

# Ejercicio N°4:
# 4. rear dos funciones: calcular_area_circulo(radio) que reciba el radio como parámetro y devuelva el área del círculo. calcular_perimetro_ circulo(radio) que reciba el radio como parámetro y devuelva el perímetro del círculo. Solicitar el radio al usuario y llamar ambas funciones para mostrar los resultados.
from math import pi  # Importamos la constante pi 
# Función que calcula el área del círculo
def calcular_area_circulo(radio):
    return pi * radio ** 2
# Función que calcula el perímetro del círculo
def calcular_perimetro_circulo(radio):
    return 2 * pi * radio
# Programa principal
# Solicitamos al usuario que ingrese el valor del radio
radio_circulo = float(input("Ingrese el radio del círculo: "))
# Mostramos los resultados
print(f"Área del círculo: {round(calcular_area_circulo(radio_circulo), 2)}")
print(f"Perímetro del círculo: {round(calcular_perimetro_circulo(radio_circulo), 2)}")

# Ejercicio N°5:
# 5. Crear una función llamada segundos_a_horas(segundos) que reciba una cantidad de segundos como parámetro y devuelva la cantidad de horas correspondientes. Solicitar al usuario los segundos y mostrar el resultado usando esta función.
# Definimos la función que convierte segundos a horas
def segundos_a_horas(segundos):
    return segundos / 3600  # equivalencia en segundos
# Programa principal
segundos_usuario = float(input("Ingrese una cantidad en segundos: "))
# Mostramos el resultado
print(f"{segundos_usuario} segundos equivalen a {round(segundos_a_horas(segundos_usuario), 2)} horas.")

# Ejercicio N°6:
# 6. Crear una función llamada tabla_multiplicar(numero) que reciba un número como parámetro y imprima la tabla de multiplicar de ese número del 1 al 10. Pedir al usuario el número y llamar a la función.
# definimos la función que muestra la tabla de multiplicar del número recibido
def tabla_multiplicar(numero):
    for i in range(1, 11):
        producto = numero * i
        print(f"{numero} x {i} = {producto}")
# Programa principal
numero_usuario = int(input("Ingrese un número: "))
# Llamamos a la función
tabla_multiplicar(numero_usuario)

# Ejercicio N°7:
# 7. Crear una función llamada operaciones_basicas(a, b) que reciba dos números como parámetros y devuelva una tupla con el resultado de sumarlos, restarlos, multiplicarlos y dividirlos. Mostrar los resultados de forma clara.
# Definimos una función de operaciones basicas: 
def operaciones_basicas(a, b):
    # Mostramos el resultado de las operaciones: 
    print(f"Suma entre {a} y {b}: {round(a + b, 2)}")
    print(f"Resta entre {a} y {b}: {round(a - b, 2)}") 
    print(f"Multiplicación entre {a} y {b}: {round(a * b, 2)}")
    # Verificamos que el segundo número no sea cero antes de dividir
    if b != 0:
        print(f"División entre {a} y {b}: {round(a / b, 2)}")
    else:
        # Si b es cero, mostramos un mensaje de error
        print("No se puede dividir por cero.")
# Programa principal:
# Solicitamos al usuario que ingrese dos números:
num1 = float(input("Ingrese un primer número: "))
num2 = float(input("Ingrese un segundo número: "))
# Llamamos a la función 
operaciones_basicas(num1, num2)

# Ejercicio N°8:
# 8. Crear una función llamada calcular_imc(peso, altura) que reciba el peso en kilogramos y la altura en metros, y devuelva el índice de masa corporal (IMC). Solicitar al usuario los datos y llamar a la función para mostrar el resultado con dos decimales.
# Definimos la función que calcula el Índice de Masa Corporal (IMC)
def calcular_imc(peso, altura):
    # Fórmula IMC 
    return peso / (altura ** 2)
# Programa principal:
# Solicito al usuario su peso en kg
peso_usuario = float(input("Ingrese su peso (kg): "))
# Solicito al usuario su altura en mts
altura_usuario = float(input("Ingrese su altura (mts): "))
# Llamamos a la función para calcular el IMC
imc = calcular_imc(peso_usuario, altura_usuario)
# Mostramos el resultado
print(f"Índice de Masa Corporal (IMC): {round(imc, 2)}")

# Ejercicio N°9:
# 9. Crear una función llamada celsius_a_fahrenheit(celsius) que reciba una temperatura en grados Celsius y devuelva su equivalente en Fahrenheit. Pedir al usuario la temperatura en Celsius y mostrar el resultado usando la función.
# Función que convierte grados Celsius a Fahrenheit
def celsius_a_fahrenheit(celsius): 
    return (celsius * 9/5) + 32
# Programa principal:
# Solicitamos al usuario la temperatura en Celsius
celsius_usuario = float(input("Ingrese la temperatura en Celsius (°C): "))
# Llamamos a la función y guardamos el resultado
calculo_fahrenheit = celsius_a_fahrenheit(celsius_usuario)
# Mostramos el resultado 
print(f"{celsius_usuario}°C equivalen a {round(calculo_fahrenheit, 2)}°F")

# Ejercicio N°10:
# 10. Crear una función llamada calcular_promedio(a, b, c) que reciba tres números como parámetros y devuelva el promedio de ellos. Solicitar los números al usuario y mostrar el resultado usando esta función.
# Función que calcula el promedio de tres números
def calcular_promedio(a, b, c): 
    return (a + b + c) / 3
# Programa principal
# Solicitamos tres números al usuario:
num1 = float(input("Ingrese su primer número: "))
num2 = float(input("Ingrese su segundo número: "))
num3 = float(input("Ingrese su tercer número: "))
# Calculamos el promedio usando la función
promedio = calcular_promedio(num1, num2, num3)
# Mostramos el resultado: 
print(f"El promedio entre {num1}, {num2} y {num3} es: {round(promedio, 2)}")