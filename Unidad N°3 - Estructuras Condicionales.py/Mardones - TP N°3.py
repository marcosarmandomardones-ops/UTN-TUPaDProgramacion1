#UNIDAD N°3 - Estructuras Condicionales

#Ejercicio N°1: 
# 1)Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años, deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”.
EDAD_MINIMA = 18 # Definimos y almacenamos el la variable EDAD_MINIMA el valor de 18. 
edad = int(input("ingrese su edad: ")) # Solicita la edad al ususario.
if edad > EDAD_MINIMA: # Compara la edad ingresada con la edad minima. 
    print("Es mayor de edad") # si la edada es mayor o igual a la edad minima, imprime este mensaje.

#Ejercicio N°2:
 #2)Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el mensaje “Desaprobado”.
nota = float(input("Ingrese su nota: ")) # solicita al ususario que ingrese la nota 
if nota >= 6: # Compara si la nota es mayor o igual a 6
    print("Aprobado") # Si la nota es mayor o igual a 6, imprime este mensaje
else: # Si la nota es menor a 6, imprime el mesaje siguiente 
    print("Desaprobado")

#Ejercicio N°3:
#3) Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un número par, imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso contrario, imprimir por pantalla "Por favor, ingrese un número par". Nota: investigar el uso del operador de módulo (%) en Python para evaluar si un número es par o impar.
numero = int(input("ingrese un número: ")) # Solicita al usuario que ingrese un número.
if numero % 2 == 0: # Compara si el numero es par.
    print("Ha ingresado un número par") # Si el número es par imprime el siguiente mensaje. 
else:
    print("Por favor, ingrese un número par") # Si el número no es par imprime el siguiente mensaje. 

#Ejercicio N°4:
#4) Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las siguientes categorías pertenece: 
# ● Niño/a: menor de 12 años. 
# ● Adolescente: mayor o igual que 12 años y menor que 18 años. 
# ● Adulto/a joven: mayor o igual que 18 años y menor que 30 años. 
# ● Adulto/a: mayor o igual que 30 años.
edad = int(input("Ingrese su edad: ")) # Solicita al usuario que ingrese su edad. 
if edad < 12: # Compara si la edad es menor a 12, si es asi imprime el siguiente mensaje.
    print("Niño/a")
elif edad >= 12 and edad < 18: # Compara si la edad es mayor o igual que 12 y menor a 18, si es asi imprime el siguiente mensaje.
    print("Adolescente")
elif edad >= 18 and edad < 30: # Compara si la edad es mayor o igual que 18 y menor a 30, si es asi imprime el siguiente mensaje.
    print("Adulto/a joven")
else:
    print("Adulto/a")

#Ejercicio N°5:
#5)Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres (incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres". Nota: investigue el uso de la función len() en Python para evaluar la cantidad de elementos que tiene un iterable tal como una lista o un string.
contrasena = str(input("Por favor, ingrese una contraseña de entre 8 y 14 caracteres: ")) # Solicita al ususario que ingrese una contraseña
if len(contrasena) >= 8 and len(contrasena) <= 14: # Compara si la contraseña tiene entre 8 y 14 caracteres, si es asi imprime el siguiente mensaje
    print("Ha ingresado una contraseña correcta")
else: # si la contraseña no tiene entre 8 y 14 caracteres, imprime el siguiente mensaje 
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

#Ejercicio N°6:
#6)Teniendo en cuenta lo antes mencionado, escribir un programa que tome la lista numeros_aleatorios, calcule su moda, su mediana y su media y las compare para determinar si hay sesgo positivo, negativo o no hay sesgo. Imprimir el resultado por pantalla.
#Definir la lista numeros_aleatorios de la siguiente forma:
import random
from statistics import mode, median, mean
numeros_aleatorios = [random.randint(1, 100) for i in range(50)] # Generar lista con 50 números aleatorios entre 1 y 100
# Calcular media, mediana y moda
media_numeros = mean(numeros_aleatorios)
mediana_numeros = median(numeros_aleatorios)
moda_numeros = mode(numeros_aleatorios)
# Mostrar valores calculados
print(f"Lista de números aleatorios: {numeros_aleatorios}")
print(f"Media: {round(media_numeros,2)}")
print(f"Mediana: {round(mediana_numeros,2)}")
print(f"Moda: {round(moda_numeros,2)}")
# Comparar para determinar sesgo
if media_numeros > mediana_numeros and mediana_numeros > moda_numeros:
    print("Sesgo positivo o a la derecha")
elif media_numeros < mediana_numeros and mediana_numeros < moda_numeros:
    print("Sesgo negativo o a la izquierda")
else:
    print("Sin sesgo")

#Ejercicio N°7:
#7)Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por pantalla.
frase = input("Ingrese una frase o palabra: ") # solicita al u
ultima_letra = frase[-1].lower() # Almacenamos en una variable la última letra para comparar
if ultima_letra == "a" or ultima_letra == "e" or ultima_letra == "i" or ultima_letra == "o" or ultima_letra == "u": # Comparamos si la última letra es una vocal
    frase_modificada = frase + "!" # Si la última letra es una vocal, añadimos un signo de exclamación al final de la frase
    print(frase_modificada)
else: # Si la última letra no es una vocal, dejamos la frase tal cual la ingresamos  
    print(frase)

#Ejercicio N°8:
#8)Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3 dependiendo de la opción que desee:
#1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.
#2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.
#3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.
#El programa debe transformar el nombre ingresado de acuerdo a la opción seleccionada por el usuario e imprimir el resultado por pantalla. Nota: investigue uso de las funciones upper(), lower() y title() de Python para convertir entre mayúsculas y minúsculas.
nombre = input("Ingrese su nombre: ") # solicita al ususario que ingrese su nombre:
print("1. Si quiere su nombre en mayúsculas.")
print("2. Si quiere su nombre en minúsculas.")
print("3. Si quiere su nombre con la primera letra mayúscula.")
opcion = int(input("Ingrese una opción (1, 2 o 3: ")) # Solicita al ususario que ingrese una opción (1, 2 o 3):
if opcion == 1:
    print(nombre.upper())
elif opcion == 2:
    print(nombre.lower())
elif opcion == 3:
    print(nombre.title())
else:
    print("Opción no válida")

#Ejercicio N°9:
#9) Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la magnitud en una de las siguientes categorías según la escala de Richter e imprima el resultado por pantalla:
#● Menor que 3: "Muy leve" (imperceptible).
#● Mayor o igual que 3 y menor que 4: "Leve" (ligeramente perceptible).
#● Mayor o igual que 4 y menor que 5: "Moderado" (sentido por personas, pero generalmente no causa daños).
#● Mayor o igual que 5 y menor que 6: "Fuerte" (puede causar daños en estructuras débiles).
#● Mayor o igual que 6 y menor que 7: "Muy Fuerte" (puede causar daños significativos).
#● Mayor o igual que 7: "Extremo" (puede causar graves daños a gran escala).
magnitud = float(input("Igrese la magnitud del terremoto: ")) # 
if magnitud < 3:
    print("Muy leve (imperceptible)")
elif magnitud >= 3 and magnitud < 4:
    print("Leve (ligeramente perceptible)")
elif magnitud >= 4 and magnitud < 5:
    print("Moderado (sentido por personas, pero generalmente no causa daños)")
elif magnitud >= 5 and magnitud < 6:
    print("Fuerte (puede causar daños en estructuras débiles)")
elif magnitud >= 6 and magnitud < 7:
    print("Muy Fuerte (puede causar daños significativos)")
else: # magnitud >= 7
    print("Extremo (puede causar graves daños a gran escala)")

#Ejercicio N°10:    
#10)Utilizando la información aportada en la siguiente tabla sobre las estaciones del año
#Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes del año es y qué día es. El programa deberá utilizar esa información para imprimir por pantalla si el usuario se encuentra en otoño, invierno, primavera o verano.
# Pedimos al usuario el hemisferio y lo convertimos a mayúsculas para uniformidad:
ubicacion = input('Ingrese en el hemisferio que se encuentra ("N" o "S"): ').upper()
# Pedimos al usuario mes y día:
mes = int(input("Ingrese el número del mes (1 al 12): "))
dia = int(input("Ingrese el número del día (1 al 31): "))
# Validación básica de datos:
if ((ubicacion != "N") and (ubicacion != "S")) or (mes < 1) or (mes > 12) or (dia < 1) or (dia > 31):
    print("Datos no válidos")
else:
    # Si está en el hemisferio norte
    if ubicacion == "N":
        # Invierno: del 21 de diciembre al 20 de marzo
        if (mes == 12 and dia >= 21) or (mes in [1, 2]) or (mes == 3 and dia < 21):
            print("Invierno")
        # Primavera: del 21 de marzo al 20 de junio
        elif (mes == 3 and dia >= 21) or (mes in [4, 5]) or (mes == 6 and dia < 21):
            print("Primavera")
        # Verano: del 21 de junio al 20 de septiembre
        elif (mes == 6 and dia >= 21) or (mes in [7, 8]) or (mes == 9 and dia < 21):
            print("Verano")
        # Otoño: del 21 de septiembre al 20 de diciembre
        elif (mes == 9 and dia >= 21) or (mes in [10, 11]) or (mes == 12 and dia < 21):
            print("Otoño")
    # Si está en el hemisferio sur
    elif ubicacion == "S":
        # Verano: del 21 de diciembre al 20 de marzo
        if (mes == 12 and dia >= 21) or (mes in [1, 2]) or (mes == 3 and dia < 21):
            print("Verano")
        # Otoño: del 21 de marzo al 20 de junio
        elif (mes == 3 and dia >= 21) or (mes in [4, 5]) or (mes == 6 and dia < 21):
            print("Otoño")
        # Invierno: del 21 de junio al 20 de septiembre
        elif (mes == 6 and dia >= 21) or (mes in [7, 8]) or (mes == 9 and dia < 21):
            print("Invierno")
        # Primavera: del 21 de septiembre al 20 de diciembre
        elif (mes == 9 and dia >= 21) or (mes in [10, 11]) or (mes == 12 and dia < 21):
            print("Primavera")
