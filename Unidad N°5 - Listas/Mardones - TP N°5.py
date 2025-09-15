# UNIDAD 5 - Práctico 5: Listas

#Ejercicio N°1:
#1) Crear una lista con las notas de 10 estudiantes.
#• Mostrar la lista completa.
#• Calcular y mostrar el promedio.
#• Indicar la nota más alta y la más baja.
# Lista con las notas de 10 estudiantes:
notas = [9.1, 8.5, 7.3, 7.5, 8, 5, 6.8, 10, 7, 5.5]
# Mostramos la lista de notas
print(f"Notas de los estudiantes: {notas}")
# Calculo del promedio de las notas
suma = 0
for num in notas:
    suma += num
promedio = suma / len(notas)
print(f"Promedio de las notas: {round(promedio, 2)}")
# Determinación de máximo y mínimo (forma manual)
menor = notas[0]
mayor = notas[0]
for num in notas:
    if num < menor:
        menor = num
    elif num > mayor:
        mayor = num
print(f"Nota más alta: {mayor} - Nota más baja: {menor}")
# Alternativa usando funciones integradas
print(f"(Usando funciones integradas) Nota más alta: {max(notas)} - Nota más baja: {min(notas)}")

#Ejercicio N°2:
#2) Pedir al usuario que cargue 5 productos en una lista.
#• Mostrar la lista ordenada alfabéticamente. Investigue el uso del método sorted().
#• Preguntar al usuario qué producto desea eliminar y actualizar la lista.
lista = []
for i in range(1, 6):
    producto = input(f"Ingrese el nombre del producto #{i}: ").lower()
    lista.append(producto)
# Imprimimos lista original
print(f"Lista original: {lista}")
# Ordenar la lista
lista_ordenada = sorted(lista)
print(f"Lista ordenada alfabéticamente: {lista_ordenada}")
# Eliminar un producto de la lista ordenada
eliminar_producto = input("Ingrese el nombre del producto que desea eliminar: ").lower()
# Verificamos si el producto está en la lista
if eliminar_producto in lista_ordenada:
    lista_ordenada.remove(eliminar_producto)
    print(f"Se eliminó el producto: {eliminar_producto}")
    print(f"Lista actualizada: {lista_ordenada}")
else:
    print("Este producto no está en la lista.")

#Ejercicio N°3:
# 3) Generar una lista con 15 números enteros al azar entre 1 y 100.
#• Crear una lista con los pares y otra con los impares.
#• Mostrar cuántos números tiene cada lista.
import random
# Inicializamos las listas
lista = []
lista_par = []
lista_impar = []
# Generamos 15 números al azar entre 1 y 100
for i in range(1, 16):
    num = random.randint(1, 100)
    lista.append(num)
    if num % 2 == 0: # Verificamos que lo sean pares para incluirlos a la lista
        lista_par.append(num)
    else:
        lista_impar.append(num) # Incluimos a la lista los números impares
# Imprimimos las listas creadas
print(f"Lista original: {lista}")
print(f"Lista de números pares: {lista_par} (Cantidad: {len(lista_par)})")
print(f"Lista de números impares: {lista_impar} (Cantidad: {len(lista_impar)})")

#Ejercicio N°4:
#4) Dada una lista con valores repetidos:
#• Crear una nueva lista sin elementos repetidos.
#• Mostrar el resultado.
# Lista original con valores repetidos
datos = [1, 3, 5, 3, 7, 1, 9, 5, 3]
# Nueva lista sin elementos repetidos con la palabra reservada "set"
Datos_nuevo = list(set(datos))
# Mostrar resultado
print(f"Lista original: {datos}")
print(f"Lista sin repetidos: {Datos_nuevo}")

#Ejercicio N°5:
#5) Crear una lista con los nombres de 8 estudiantes presentes en clase.
#• Preguntar al usuario si quiere agregar un nuevo estudiante o eliminar uno existente.
#• Mostrar la lista final actualizada.
# Lista de estudiantes original 
lista_estudiantes = ["Juan", "Carlos", "Marcos", "Luis", "Agustina", "Fernando", "Marta", "Carla"]
print("Lista inicial de estudiantes:")
print(lista_estudiantes)
# Agregar un nuevo estudiante con la palabra clave "si", y colocamos "no" en caso de omitir la función 
nuevo_estudiante = input("¿Quieres agregar un nuevo estudiante? (Si o No): ").strip().lower()
if nuevo_estudiante == "si":
    nombre_nuevo = input("Ingrese el nombre del nuevo estudiante: ").capitalize()
    lista_estudiantes.append(nombre_nuevo)
    print(f"Se agregó el estudiante: {nombre_nuevo}")
# Eliminar un estudiante existente
eliminar_estudiante = input("¿Quieres eliminar un estudiante existente? (Si o No): ").strip().lower()
if eliminar_estudiante == "si":
    nombre_eliminado = input("Ingrese el nombre del estudiante a eliminar: ").capitalize()
    if nombre_eliminado in lista_estudiantes:
        lista_estudiantes.remove(nombre_eliminado)
        print(f"Se eliminó el estudiante: {nombre_eliminado}")
    else:
        print("Este estudiante no está en la lista.")
# Mostrar la lista final
print("Lista final de estudiantes: ")
print(lista_estudiantes)

#Ejercicio N°6:
#6) Dada una lista con 7 números, rotar todos los elementos una posición hacia la derecha (el último pasa a ser el primero).
# Lista de números números:
lista = [5, 9, 6, 4, 3, 2, 8]
# Rotamos la posición de los índices a la derecha: 
lista_desplazada = [lista[-1]] + lista[:-1]
# Mostramos ambas listas
print(f"Lista original: {lista}")
print(f"Lista desplazada un lugar a la derecha: {lista_desplazada}")

#Ejercicio N°7:
#7) Crear una matriz (lista anidada) de 7x2 con las temperaturas mínimas y máximas de una semana.
#• Calcular el promedio de las mínimas y el de las máximas.
#• Mostrar en qué día se registró la mayor amplitud térmica.
# Matriz 7x2:
matriz = [
    [11.6, 32],
    [18.6, 30],
    [9.2, 33.1],
    [12.6, 30.5],
    [18, 35.6],
    [3, 31.1],
    [6.6, 29.8]
]
# Calculo de mínimos y máximos: 
minimas = [fila[0] for fila in matriz]
maximas = [fila[1] for fila in matriz]
# Calculo de promedios de mínimos y máximos: 
promedio_min = sum(minimas) / len(minimas)
promedio_max = sum(maximas) / len(maximas)
# Calculo de amplitud:
amplitudes = [fila[1] - fila[0] for fila in matriz]
dia_max_amp = amplitudes.index(max(amplitudes)) + 1
# Calculo el promedio de las mínimas y el de las máximas.
print(f"Promedio mínimas: {round(promedio_min, 2)}°C")
print(f"Promedio máximas: {round(promedio_max, 2)}°C")
# Mostramos el día que se registró la mayor amplitud térmica:
print(f"La mayor amplitud fue el día {dia_max_amp} con {max(amplitudes):.2f}°C")

#Ejercicio N°8:
# 8) Crear una matriz con las notas de 5 estudiantes en 3 materias.
#• Mostrar el promedio de cada estudiante.
#• Mostrar el promedio de cada materia.
# Matriz 5x3:
matriz = [
    [8, 9.2, 8.6],
    [6.4, 7, 6.5],
    [8.8, 9, 8.1],
    [4.2, 5.5, 7],
    [6, 8.1, 10]
]
# Promedio de cada estudiante (fila)
print("Promedio de cada estudiante:")
for i in range(5):
    promedio = sum(matriz[i]) / len(matriz[i])
    print(f"Estudiante {i+1}: {round(promedio, 2)}")
# Promedio de cada materia (columna)
print("Promedio de notas de cada materia:")
for j in range(3):
    suma = 0
    for i in range(5):
        suma += matriz[i][j]
    promedio = suma / 5
    print(f"Materia {j+1}: {round(promedio, 2)}")

#Ejercicio N°9:
# 9) Representar un tablero de Ta-Te-Ti como una lista de listas (3x3).
#• Inicializarlo con guiones "-" representando casillas vacías.
#• Permitir que dos jugadores ingresen posiciones (fila, columna) para colocar "X" o "O".
#• Mostrar el tablero después de cada jugada.
# Matriz 3x3 con guiones:
# Inicializamos la matriz 3x3 con guiones "-" es los espacios a completar
matriz = []
for _ in range(3):
    fila = []
    for _ in range(3):
        fila.append("-")
    matriz.append(fila)
# Definimos el jugador inicial y el contador de turnos
Jugador1 = "X"
turno = 0
# Bucle principal del juego (máximo 9 turnos)
while turno < 9:
    print("Tablero actual:")
    # Mostramos el tablero
    for f in range(3):
        print(matriz[f][0], matriz[f][1], matriz[f][2])
    print(f"Juega: {Jugador1}")
    # Pedimos la posición al jugador
    fila_ing = int(input("ingrese número de la fila (1-3): ")) - 1
    columna_ing = int(input("ingrese número de la columna (1-3): ")) - 1
    # Validamos que la posición esté dentro del rango
    if fila_ing < 0 or fila_ing > 2 or columna_ing < 0 or columna_ing > 2:
        print("Fila o columna fuera de rango. Intente de nuevo.")
        continue
    # Validamos que la casilla esté vacía
    if matriz[fila_ing][columna_ing] != "-":
        print("Esa posición ya está ocupada. Intente de nuevo.")
        continue
    # Colocamos la ficha del jugador en la posición elegida
    matriz[fila_ing][columna_ing] = Jugador1
    turno += 1
    # Cambiamos de jugador
    Jugador1 = "O" if Jugador1 == "X" else "X"

#Ejercicio N°10:
# 10) Una tienda registra las ventas de 4 productos durante 7 días, en una matriz de 4x7.
#• Mostrar el total vendido por cada producto.
#• Mostrar el día con mayores ventas totales.
#• Indicar cuál fue el producto más vendido en la semana.
# Matriz 4x7:
import random
# Matriz 4x7:
matriz = []
for j in range(4):
    fila = []  # Inicializar la fila vacía
    for i in range(7):
        num = random.randint(1, 10)  # Generar número aleatorio
        fila.append(num)  # Agregar el número a la fila
    matriz.append(fila)  # Agregar la fila a la matriz
# Mostrar la matriz
for fila in matriz:
    print(fila)
# Mostramos el total vendido por cada producto:
ventas_productos = []
for i in range(4):
    suma_fila = 0
    for j in range(7):
       suma_fila += matriz[i][j]
    ventas_productos.append(suma_fila)
    print(f"Total de ventas del producto {i+1}: {suma_fila}")
# Total vendido por cada día y día de mayor venta
mayor_venta = 0
dia_mayor = 0
for j in range(7):
    suma_columna = 0
    for i in range(4):
        suma_columna += matriz[i][j]
    print(f"Total de ventas del día {j+1}: {suma_columna}")
    if suma_columna > mayor_venta:
        mayor_venta = suma_columna
        dia_mayor = j + 1
print(f"El día {dia_mayor} tiene la mayor cantidad de ventas: {mayor_venta}")
# Indicar cuál fue el producto más vendido en la semana.
maximo_ventas_producto = 0
indice_producto = 0
for i in range(4):
    if ventas_productos[i] > maximo_ventas_producto:
        maximo_ventas_producto = ventas_productos[i]
        indice_producto = i
print(f"El producto más vendido en la semana fue el producto #{indice_producto + 1} con {maximo_ventas_producto} ventas.")