# Práctico 4: Estructuras repetitivas

#Ejercicio N°1:
# 1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100 (incluyendo ambos extremos), en orden creciente, mostrando un número por línea.
for i in range(0, 101): # imprime los número de 0 a 100
	print(i) # Imprime el número actual
	
#Ejercicio N°2:
# 2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de dígitos que contiene.
num = int(input("Ingrese un número entero: "))  # Solicita al usuario un número entero
contar = 0  # Inicializamos el contador en 0
num = abs(num)  # Aseguramos que el número sea positivo
if num == 0:
    contar = 1  # El número 0 tiene 1 dígito
else:
    while num > 0:  # Mientras el número sea mayor que 0
        contar += 1
        num = num // 10  # Eliminamos el último dígito del número
print(f"El número tiene {contar} cifras") # imprime la cantidad de dígitos

#Ejercicio N°3:
# 3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores dados por el usuario, excluyendo esos dos valores.
num1 = int(input("Ingrese un primer número entero: "))   # Solicita al usuario un primer número entero
num2 = int(input("Ingrese un segundo número entero: "))  # Solicita al usuario un segundo número entero
suma = 0 #inicializamos la variable suma en 0
# Aseguramos que num1 sea menor que num2
if num1 > num2:
    num1, num2 = num2, num1  # Intercambiamos los valores
# Recorremos los números entre num1 y num2, excluyendo extremos
for i in range(num1 + 1, num2):
    suma += i
print(f"La suma de los números entero entre {num1} y {num2} es: {suma}")

#Ejercicio N°4:
# 4) Elabora un programa que permita al usuario ingresar números enteros y los sume en secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese un 0.
suma = 0 # inicialozamos la variable suma en 0
num = int(input("Ingrese un número entero (0 para finalizar): ")) # Solicitamos al usuario que ingrese un número entero
while num != 0:  # Mientras el número no sea 0
    suma += num
    num = int(input("Ingrese un número entero (0 para finalizar): "))
print(f"Total acumulado: {suma}")

#Ejercicio N°5:
# 5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el programa debe mostrar cuántos intentos fueron necesarios para acertar el número.
# Inicializamos las variables:
codigo = 5
contar = 0
num = int(input("Ingrese un número entre 0 y 9: ")) # Solicitamos al usuario que ingrese un número entre 0 y 9
while num != codigo: # Mientras el número ingresado no sea igual al código
    contar += 1
    if num < 0 or num > 9: # Verificamos que el número no esté fuera del rango
        print("Número ingresado no es válido")
    else:
        print("Número incorrecto, intenta de nuevo")
        num = int(input("Ingrese un número entre 0 y 9: "))
contar += 1  # Contamos el intento correcto
print(f"Número {codigo} ingresado es correcto y la cantidad de intentos fue {contar}") # imprimimos el número de intentos

#Ejercicio N°6:
# 6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos entre 0 y 100, en orden decreciente.
for i in range(100, -1, -1): # Recorre los números de 99 a 1 en orden decreciente
    if i % 2 == 0: # Verificamos si el número es par
        print(i) 

#Ejercicio N°7:
# 7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un número entero positivo indicado por el usuario.
num = int(input("Ingrese un número entero positivo: "))
suma = 0 # Inicializamos la variable suma
if num >= 0:
    for i in range(0, num + 1): # Incluimos el número final
        suma += i
    print(f"La suma de los números enteros entre 0 y {num} es: {suma}") # Imprimimos el resultado
else:
    print("Debe ingresar un número positivo")

#Ejercicio N°8:
# 8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad menor, pero debe estar preparado para procesar 100 números con un solo cambio).
# Inicializamos contadores
contar_positivos = 0
contar_negativos = 0
contar_ceros = 0
contar_pares = 0
contar_impares = 0
# solicitamos al usuario que ingrese 100 números enteros
for i in range(1, 101):  
    num = int(input(f"Ingrese el número #{i}: "))

    # Verificamos númeero par o impar
    if num % 2 == 0:
        contar_pares += 1
    else:
        contar_impares += 1

    # Verificamos signo
    if num > 0:
        contar_positivos += 1
    elif num < 0:
        contar_negativos += 1
    else:
        contar_ceros += 1
# Mostramos resultados
print(f"Cantidad de pares: {contar_pares}")
print(f"Cantidad de impares: {contar_impares}")
print(f"Cantidad de positivos: {contar_positivos}")
print(f"Cantidad de negativos: {contar_negativos}")
print(f"Cantidad de ceros: {contar_ceros}")

#Ejercicio N°9:
# 9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe poder procesar 100 números cambiando solo un valor).
# Inicializamos variables:
cant_num = 10
sumar = 0
# solicitamos al usuario que ingrese 100 números enteros: 
for i in range(1, cant_num + 1):  
    num = int(input(f"Ingrese el #{i} número entero: "))
    sumar += num
# Calculamos la media:
promedio = sumar / cant_num
# Mostrar resultado al usuario: 
print(f"Suma total: {sumar}")
print(f"Cantidad de números: {cant_num}")
print(f"Media: {promedio}")

#Ejercicio N°10:
# 10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.
num = int(input("Ingrese un número entero: "))
num_original = num  # guardamos para mostrar después
invertido = 0
while num > 0:
    digito = num % 10  # obtenemos el último dígito
    invertido = invertido * 10 + digito  # lo agregamos al invertido
    num //= 10  # quitamos el último dígito
print(f"El número {num_original} invertido es: {invertido}")