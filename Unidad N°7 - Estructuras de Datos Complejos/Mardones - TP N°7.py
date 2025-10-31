# Práctico 7: Estructuras de datos complejas:

# Ejercicio N°1: 
# 1) Dado el diccionario precios_frutas precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450} Añadir las siguientes frutas con sus respectivos precios:
# ● Naranja = 1200
# ● Manzana = 1500
# ● Pera = 2300
# Definimos el diccionario inicial: 
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}
# Agregar un nuevo par key-value (frutas con sus respectivos precios)
precios_frutas ['Naranja'] = 1200
precios_frutas ['Manzana'] = 1500
precios_frutas ['Pera'] = 2300
# imprimimos el diccionario actualizado:
print(precios_frutas)

# Ejercicio N°2: 
# 2) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código desarrollado en el punto anterior, actualizar los precios de las siguientes frutas:
# ● Banana = 1330
# ● Manzana = 1700
# ● Melón = 2800
# Definimos el diccionario inicial
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450, 'Naranja': 1200, 'Manzana': 1500, 'Pera': 2300}
# Actualizamos los precios de las frutas indicadas
precios_frutas ['Banana'] = 1330
precios_frutas ['Manzana'] = 1700
precios_frutas ['Melón'] = 2800
# Imprimimos el diccionario actualizado
print(precios_frutas)

# Ejercicio N°3:
# 3) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código desarrollado en el punto anterior, crear una lista que contenga únicamente las frutas sin los precios.
# Definimos el diccionario inicial
precios_frutas = {'Banana': 1330, 'Ananá': 2500, 'Melón': 2800, 'Uva': 1450, 'Naranja': 1200, 'Manzana': 1700, 'Pera': 2300}
# Creamos una lista con solo las frutas (Recuperar solo los keys)
lista_frutas = list(precios_frutas.keys())
# Imprimimos la lista de frutas
print(lista_frutas)

# Ejercicio N°4:
# 4) Escribí un programa que permita almacenar y consultar números telefónicos.
# • Permití al usuario cargar 5 contactos con su nombre como clave y número como valor.
# • Luego, pedí un nombre y mostrale el número asociado, si existe.
# Creamos el diccionario vacío
agenda = {}
# Cargamos los 5 contactos por ciclo for
for i in range(5):
    contacto = input(f"Ingrese el nombre del contacto #{i+1}: ").strip().lower()
    numero_contacto = input(f"Ingrese el número del contacto #{i+1}: ").strip()
    agenda[contacto] = numero_contacto
# Mostrar la agenda completa
print("----Agenda cargada----")
print(agenda)
# Consultar un contacto por su nombre
nombre_consulta = input("\nIngrese el nombre del contacto a consultar: ").strip().lower()
# verificamos si el contacto existe en la agenda
if nombre_consulta in agenda:
    print(f"El número de {nombre_consulta} es {agenda[nombre_consulta]}")
else:
    print("El contacto no existe en la agenda.")

# Ejercicio N°5:
# 5) Solicita al usuario una frase e imprime:
# • Las palabras únicas (usando un set).
# • Un diccionario con la cantidad de veces que aparece cada palabra. Ejemplo:
# Entrada de información del usuario
frase = input("Ingrese una frase: ").lower()
palabras = frase.split()
print(palabras)
# Palabras únicas
palabras_unicas = set(palabras)
print("Palabras únicas:", palabras_unicas)
# Recuento de palabras
recuento = {}
# Contamos las apariciones de cada palabra
for palabra in palabras:
    if palabra in recuento:
        recuento[palabra] += 1
    else:
        recuento[palabra] = 1
# Imprimimos el diccionario de recuentos
print("Recuento:", recuento)

# Ejercicio N°6:
# 6) Permití ingresar los nombres de 3 alumnos, y para cada uno una tupla de 3 notas. Luego, mostrá el promedio de cada alumno.
# Diccionario para almacenar los alumnos y sus notas
alumnos_notas = {}
# Ciclo para ingresar las notas de 3 alumnos
for i in range(3):
    alumno = input(f"Ingrese el nombre del alumno #{i+1}: ").strip().capitalize()
    nota1 = float(input(f"Ingrese la 1° nota de {alumno}: "))
    nota2 = float(input(f"Ingrese la 2° nota de {alumno}: "))
    nota3 = float(input(f"Ingrese la 3° nota de {alumno}: "))
    alumnos_notas[alumno] = (nota1, nota2, nota3)
# Mostramos el diccionario con los alumnos y sus notas
print("Alumnos con sus notas:", alumnos_notas)
# Calculamos y mostramos los promedios para cada alumno
print("\nPromedio de cada alumno:")
for alumno, notas in alumnos_notas.items():
    promedio = sum(notas) / len(notas)
    print(f"{alumno}: {round(promedio, 2)}")

# Ejercicio N°7:
# 7) Dado dos sets de números, representando dos listas de estudiantes que aprobaron Parcial 1 y Parcial 2:
#• Mostrá los que aprobaron ambos parciales.
#• Mostrá los que aprobaron solo uno de los dos.
#• Mostrá la lista total de estudiantes que aprobaron al menos un parcial (sin repetir).
# Conjuntos de estudiantes que aprobaron cada parcial
parcial1 = {"Agus", "Lucas", "Jonas", "Pedro", "Juan"}
parcial2 = {"Jonas", "Juan", "Carlos", "Lucía"}
# Los estudiantes que aprobaron ambos parciales
ambos_parciales = parcial1 & parcial2
# Los estudiantes que aprobaron solo uno de los dos parciales
solo_uno = parcial1 ^ parcial2
# Los estudiantes que aprobaron al menos uno de los parciales (sin repetir)
aprobaron_alguno = parcial1 | parcial2
# Mostrar resultados
print("Aprobaron ambos parciales:", ambos_parciales)
print("Aprobaron solo uno de los parciales:", solo_uno)
print("Aprobaron al menos un parcial:", aprobaron_alguno)

# Ejercicio N°8:
# 8) Armá un diccionario donde las claves sean nombres de productos y los valores su stock. Permití al usuario:
#• Consultar el stock de un producto ingresado.
#• Agregar unidades al stock si el producto ya existe.
#• Agregar un nuevo producto si no existe.
# Diccionario inicial con productos y su stock
stock_productos = {"clavos": 125, "tornillos": 300, "tuercas": 250, "destornilladores": 25, "martillos": 15}
# Imprimimos el stock actual
print("Stock actual:", stock_productos)
# Pedir un producto al usuario
producto = input("Ingrese el nombre del producto a consultar: ").lower().strip()
# Consultamos si tenemos stock del producto
if producto in stock_productos:
    print(f"El producto '{producto}' tiene un stock de {stock_productos[producto]} unidades.")
    
    # Preguntamos si quiere agregar más unidades al stock
    agregar = input("¿Desea agregar mas unidades a este producto? (s/n): ").lower()
    if agregar == "s":
        cantidad = int(input("Ingrese la cantidad a agregar: "))
        stock_productos[producto] += cantidad
        print(f"Stock actualizado:'{producto}': {stock_productos[producto]} unidades.")
    else:
        print("No se modificó el stock.")
else:
    # Si el producto no tiene stock - se permite agregar un nuevo producto
    print(f"El producto: '{producto}' no esta en stock.")
    agregar_nuevo = input("¿Desea agregarlo al sistema? (s/n): ").lower()
    if agregar_nuevo == "s":
        cantidad = int(input("Ingrese la cantidad inicial de stock: "))
        stock_productos[producto] = cantidad
        print(f"Producto: '{producto}' agregado con {cantidad} unidades")
    else:
        print("No se agregó ningún producto nuevo al stock")
# Mostrar el stock final actualizado
print("\nStock final:", stock_productos)

# Ejercicio N°9:
# 9) Creá una agenda donde las claves sean tuplas de (día, hora) y los valores sean eventos.
# Creamos el diccionario de la agenda
agenda = {("lunes", "09:00"): "Junta", ("martes", "11:00"): "Clases", ("miércoles", "14:20"): "Futbol"}
# Mostrar la agenda inicial
print("*** Agenda inicial ***")
for (dia, hora), evento in agenda.items():
    print(f"{dia.capitalize()} a las {hora}: {evento}")
# Consultamos si tenemos algún nuevo evento - (día y hora)
dia = input("\nIngrese el día para consultar: ").lower().strip()
hora = input("Ingrese la hora (HH:MM): ").strip()
# Verificamos si hay un evento en ese día y horario
if (dia, hora) in agenda:
    print(f"En este día y horario tienes: {agenda[(dia, hora)]}")
else:
    print("No tiene eventos en ese día y horario.")
# Agregar un nuevo evento si el usuario quiere
agregar_evento = input("¿Quiere agregar un nuevo evento? (S/N): ").lower()
if agregar_evento == "s":
    nuevo_dia = input("Ingrese día: ").lower().strip()
    nueva_hora = input("Ingrese hora (HH:MM): ").strip()
    nuevo_evento = input("Ingrese evento: ").strip()
    agenda[(nuevo_dia, nueva_hora)] = nuevo_evento
    print("Evento agregado con exito.")
# Mostrar la agenda actualizada
print("*** Agenda final ***")
for (dia, hora), evento in agenda.items():
    print(f"{dia.capitalize()} a las {hora}: {evento}")

# Ejercicio N°10:
# 10) Dado un diccionario que mapea nombres de países con sus capitales, construí un nuevo diccionario donde:
# • Las capitales sean las claves.
# • Los países sean los valores.
# Diccionarios iniciales
original = {}
invertido = {}
# Entrada de datos por el usuario
cantidad_paises = int(input("Ingrese la cantidad de paises/capitales que desea agregar: "))
# Ciclo para ingresar los paises y sus capitales
for i in range(cantidad_paises):
    pais = input(f"Ingresa el {i + 1} país: ")
    capitales = input(f"Ingresa la capital de {pais}: ")
    original[pais] = capitales
# Invertir el diccionario
for pais, capital in original.items():
    invertido[capital] = pais
# Imprimimos los diccionarios
print(f"Original: {original}")
print(f"Invertido: {invertido}")