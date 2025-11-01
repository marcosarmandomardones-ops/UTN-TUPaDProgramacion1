# Programación I
# Archivos - Práctica

# Ejercicio N°1:
# 1. Crear archivo inicial con productos: Crear un archivo de texto llamado productos.txt con tres productos. Cada línea debe tener: nombre,precio,cantidad
# Modo "W" - crea el archivo y escribe en el mismo
with open("productos.txt", "w", encoding="utf-8") as fichero:
    fichero.write("Teclado,32000,30\n")   # Listado de productos iniciales
    fichero.write("Mouse,10000,15\n")   
    fichero.write("Mousepad,8500,10\n")   

# Ejercicio N°2:
# 2. Leer y mostrar productos: Crear un programa que abra productos.txt, lea cada línea, la procese con .strip() y .split(","), y muestre los productos en el siguiente formato:
# Modo "r" - ingresa al archivo para lectura
print("---Listado de productos actuales---")
with open("productos.txt", "r", encoding="utf-8") as fichero:
    for registro in fichero:
        registro = registro.strip()         # Limpia cada línea - elimina espacios o saltos de línea 
        partes = registro.split(",")           # Separa nombre, precio y cantidad - divide la línea en una lista
        # Muestra cada producto con formato indicado
        print(f"Producto: {partes[0]} | Precio: ${partes[1]} | Cantidad: {partes[2]}")

# Ejercicio N°3:
# 3. Agregar productos desde teclado: Modificar el programa para que luego de mostrar los productos, le pida al usuario que ingrese un nuevo producto (nombre, precio, cantidad) y lo agregue al archivo sin borrar el contenido existente.
# Modo "a" (append): permite agregar información al final del archivo.
with open("productos.txt", "a", encoding="utf-8") as fichero:
    cantidad_ingresos = input("¿Cuántos productos nuevos quiere agregar?: ").strip()
    # Verificamos que sea un número entero positivo
    if cantidad_ingresos.isdigit():       
        cantidad_ingresos = int(cantidad_ingresos)
    else:
        print("No válido - Tiene que ingresar un número entero.")
        exit()                

    # Ciclo for para agregar los productos solicitados
    for i in range(cantidad_ingresos):
        nuevo_registro = input(f"Ingrese producto {i+1} (nombre,precio,cantidad): ").strip()
        fichero.write(nuevo_registro + "\n")           # Agrega el nuevo producto al archivo
 
# Ejercicio N°4: 
# 4. Cargar productos en una lista de diccionarios: Al leer el archivo, cargar los datos en una lista llamada productos, donde cada elemento sea un diccionario con claves: nombre, precio, cantidad.
# Lista vacía para almacenar todos los productos
inventario = []  
# Abrimos el archivo en modo lector
with open("productos.txt", "r", encoding="utf-8") as fichero:
    for fila in fichero:
        datos = fila.strip().split(",") 
            # "Articulo", "Costo" y "Stock" - Luego se agrega a la lista (inventario) 
        item = {"Articulo": datos[0].strip(), "Costo": datos[1].strip(), "Stock": datos[2].strip()}
        
        inventario.append(item)        # Agregamos el diccionario a la lista

        # Muestra los productos leídos 
        print(f"Producto: {item['Articulo']} | Precio: ${item['Costo']} | Cantidad: {item['Stock']}")

# Ejercicio N°5:
# 5. Buscar producto por nombre: Pedir al usuario que ingrese el nombre de un producto. Recorrer la lista de productos y, si lo encuentra, mostrar todos sus datos. Si no existe, mostrar un mensaje de error.
# Solicitamos al usuario un nombre 
buscado = input("Ingrese el nombre del producto que desea buscar: ").strip()
hallado = False  # Bandera para saber si se encontró el producto
# Ciclo para buscar el producto en la lista
for prod in inventario:
    if prod["Articulo"].lower() == buscado.lower():  # Comparación insensible a mayúsculas
        print("=== Producto encontrado ===")
        print(f"Nombre: {prod['Articulo']}")
        print(f"Precio: {prod['Costo']}")
        print(f"Cantidad: {prod['Stock']}")
        hallado = True
        break  # Detenemos la búsqueda al encontrarlo
# Si no se encontró el producto, se muestra error
if not hallado:
    print("No se encontró el producto solicitado")

# Ejercicio N°6:
# 6. Guardar los productos actualizados: Después de haber leído, buscado o agregado productos, sobrescribir el archivo productos.txt escribiendo nuevamente todos los productos actualizados desde la lista.
# Modo "w" - borra el contenido previo y escribe la nueva versión 
with open("productos.txt", "w", encoding="utf-8") as fichero:
    # Recorrenos la lista inventario y escribimos cada producto
    for prod in inventario:
        linea = f"{prod['Articulo']},{prod['Costo']},{prod['Stock']}\n"
        fichero.write(linea)
print("Archivo actualizado")  # Confirmación de actualizacion del archivo