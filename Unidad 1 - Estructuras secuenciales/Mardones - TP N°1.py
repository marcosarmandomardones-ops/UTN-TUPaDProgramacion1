#Ejercicios de estructuras secuenciales:
#Ejercicio N°1:
#1)Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!”.
print("Hola Mundo!") #Imprime el mensaje "Hola Mundo!" por pantalla

#Ejercicio N°2:
#2)Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando el nombre ingresado. Por ejemplo: si el usuario ingresa “Marcos”, el programa debe imprimir por pantalla “Hola Marcos!”. Consejo: esto será más sencillo si utilizas print(f…) para realizar la impresión por pantalla.
nombre = input("Ingrese su nombre: ") #Solicita al usuario el nombre y almacena la respuesta en la variable nombre
print(f"Hola {nombre}!") #Imprime el saludo con el nombre ingresado 

#Ejercicio N°3:
#3)Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e imprima por pantalla una oración con los datos ingresados. Por ejemplo: si el usuario ingresa “Marcos”, “Pérez”, “30” y “Argentina”, el programa debe imprimir “Soy Marcos Pérez, tengo 30 años y vivo en Argentina”. Consejo: esto será más sencillo si utilizas print(f…) para realizar la impresión por pantalla.
nombre = input("Ingrese su nombre: ") #Solicita al usuario el nombre y almacena la respuesta en la variable nombre
apellido = input("Ingrese su apellido: ") #Solicita al usuario su apellido
edad = input("Ingrese su edad: ") #Solicita al usuario su edad 
lugar_de_residencia = input("Ingrese su lugar de residencia: ") #Solicita al usuario su lugar de residencia
print (f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {lugar_de_residencia}.") #Imprime la oración con los datos ingresados

#Ejercicio N°4:
#4)Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y su perímetro.
radio = float(input("Ingrese el radio del circulo: ")) #Solicitamos al usuario el radio del circulo y lo convertimos a float
import math #Importar la librería math ya que la necesitaremos para utilizar el número pi
area = (math.pi  * (radio **2)) #Calculamos el área del circulo 
perimetro = 2 * math.pi * radio #Caculamos el perimetro del circulo
input(f"El área del circulo es: {area} y el perimetro es: {perimetro}") #Imprimimos el área y el perietro del circulo

#Ejercicio N°5:
#5)Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a cuántas horas equivale.
segundos = int(input("ingrese una cantidad en segundos: ")) #Solicitamos al usuario la cantida de segundos para convertirlos a horas
hora = float(segundos / 3600) #Calculamos las horas dividiendo los segundos por 3600
print(f"{segundos} segundosequivales a {hora} horas") #Imprimimos la cantidad de horas que equivalen a los segundos ingresados

#Ejercicio N°6:
#6)Crear un programa que pida al usuario un número e imprima por pantalla la tabla de multiplicar de dicho número.
numero = int((input("ingrese un número entero: "))) #Solicita al usuario un número entero
print(f"{numero} * 1 = {numero * 1}") #Calculamos e imprimimos por pantalla su tabla de multiplicar del 1 al 10:
print(f"{numero} * 2 = {numero * 2}")
print(f"{numero} * 3 = {numero * 3}")
print(f"{numero} * 4 = {numero * 4}")
print(f"{numero} * 5 = {numero * 5}")
print(f"{numero} * 6 = {numero * 6}")
print(f"{numero} * 7 = {numero * 7}")
print(f"{numero} * 8 = {numero * 8}")
print(f"{numero} * 9 = {numero * 9}")
print(f"{numero} * 10 = {numero * 10}")

#Ejercicio N°7:
#7)	Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos.
numero1 = int(input("Ingrese un primer número distinto de cero: ")) #Solicitamos al usuario un primer número distinto de cero
numero2 = int(input("ingrese un segundo número distinto de cero: ")) #Solicitamos al usuario un segundo número distinto de cero
suma = numero1 + numero2 #Sumamos los dos números
resta = numero1 - numero2 #Restamso el segundo numero al primero
division = numero1 / numero2 #Dividimos el primero número por el segundo
multiplicacion = numero1 * numero2 #Multiplicamos ambos números
print(f"{numero1} + {numero2} = {numero1 + numero2}") #imprimimos la suma de ambos números
print(f"{numero1} - {numero2} = {numero1 - numero2}") #imprimimos la resta de ambos números
print(f"{numero1} / {numero2} = {numero1 / numero2}") #imprimimos la división de ambos números
print(f"{numero1} * {numero2} = {numero1 * numero2}") #imprimimos la multiplicación de ambos números

#Ejercicio N°8:
#8)Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice de masa corporal. Tener en cuenta que el índice de masa corporal se calcula del siguiente modo:
altura = float(input("ingrese su altura en metros: ")) #Solicita al usuario su altura en metros
peso = float(input("ingrese su peso en kilogramos: ")) #Solicita al usuario su peso en kilogramos
inc = peso / (altura ** 2) #Calcula el índice de masa corporal INC
print(f"Su índice de masa corporal es: {inc}") #Imprime el índice de masa corporal calculado

#Ejercicio N°9:
#9)Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por pantalla su equivalente en grados Fahrenheit. Tener en cuenta la siguiente equivalencia:
temperatura_celsius = float(input("Ingrese la temperatura en grados Celsius: ")) #Solicita al usuario la temperatura en grados celsius
temperatura_fahrenheit = float((temperatura_celsius * 9/5) + 32) #Convertimos la temperatura a grados fahrenheit
print(f"{temperatura_celsius} °C equivalen a {temperatura_fahrenheit} °F") #Imprimimos la temperatura en grados fahrenheit

#Ejercicio N°10:
#10)Crear un programa que pida al usuario 3 números e imprima por pantalla el promedio de dichos números.
numero1 = float(input("Ingrese un primer número: ")) #Solicitamos al usuario un primer número 
numero2 = float(input("ingrese un segundo número: ")) #Solicitamos al usuario un segundo número 
numero3 = float(input("ingrese un tercer número: ")) #Solicitamos al usuario un tercer número
promedio = round((numero1 + numero2 + numero3)/3,2) #Calculo del promedio de los números
print(f"El promedio de {numero1}, {numero2} y {numero3} es: {promedio} ") #Imprimimos el promedio calculado
