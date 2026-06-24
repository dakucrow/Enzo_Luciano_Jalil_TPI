import csv
import validaciones

def cargar_datos_csv(nombre_archivo):
    """Lee el archivo CSV y devuelve una lista de diccionarios con los países."""
    lista_paises = []
    try:
        with open(nombre_archivo, mode='r', encoding='utf-8') as archivo:
            lector = csv.DictReader(archivo)
            for fila in lector:
                pais = {
                    "nombre": fila["nombre"].strip(),
                    "poblacion": int(fila["poblacion"]),
                    "superficie": int(fila["superficie"]),
                    "continente": fila["continente"].strip()
                }
                lista_paises.append(pais)
        print("¡Datos cargados con éxito!")
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo {nombre_archivo}.")
    except Exception as e:
        print(f"Ocurrió un error al cargar el archivo: {e}")
    
    return lista_paises


def guardar_datos_csv(nombre_archivo, lista_paises):
    """Guarda la lista de diccionarios actualizada en el archivo CSV."""
    try:
        with open(nombre_archivo, mode='w', encoding='utf-8', newline='') as archivo:
            # Definimos los encabezados tal cual el ejemplo de la consigna
            campos = ["nombre", "poblacion", "superficie", "continente"]
            escritor = csv.DictWriter(archivo, fieldnames=campos)
            
            escritor.writeheader()
            for pais in lista_paises:
                escritor.writerow(pais)
    except Exception as e:
        print(f"Error al guardar los datos en el archivo CSV: {e}")


def agregar_pais(lista_paises):
    print("\n--- AGREGAR PAÍS ---")
    while True:
        # 1. Validar nombre
        nombre = validaciones.texto("Ingrese el nombre del país: ")
        
        # 2. Validar duplicado
        if validaciones.duplicado(nombre, lista_paises):
            print("Por favor, intente con otro nombre.\n")
        else:
            break # Rompemos el bucle para continuar con el programa
    # 3. Validación de Población (Debe ser un número entero positivo)
    poblacion = validaciones.entero("Ingrese la población (solo números enteros): ")

    # 4. Validación de Superficie (Debe ser un número entero positivo)
    superficie = validaciones.entero("Ingrese la superficie en km² (solo números enteros):  ")

    # 5. Validación de Continente (No vacío)
    continente = validaciones.texto("Ingrese el continente: ")
    # Si todo está bien, creamos el diccionario y lo sumamos a la lista
    nuevo_pais = {
        "nombre": nombre,
        "poblacion": poblacion,
        "superficie": superficie,
        "continente": continente
    }
    lista_paises.append(nuevo_pais)
    
    # Impactamos el cambio directamente en el archivo
    guardar_datos_csv("data/paises.csv", lista_paises)
    print(f"¡País '{nombre}' agregado y guardado con éxito!")

def actualizar_pais(lista_paises):
    """Busca un país y permite modificar campos específicos mediante un menú."""
    print("\n--- ACTUALIZAR DATOS DE UN PAÍS ---")
    nombre = validaciones.texto("Ingrese el nombre del país que desea actualizar: ")
    
    # Buscamos el país
    pais_encontrado = validaciones.buscar(nombre, lista_paises)
    if not pais_encontrado:
        print(f"Error: El país '{nombre}' no está registrado en el sistema.")
        return 

    print(f"\nPaís seleccionado: {pais_encontrado['nombre']} ({pais_encontrado['continente']})")
    print(f"Datos actuales -> Población: {pais_encontrado['poblacion']} | Superficie: {pais_encontrado['superficie']} km²")
    print("-" * 40)

    # --- MENÚ DE MODIFICACIÓN ---
    print("¿Qué dato desea modificar?")
    print("1. Población")
    print("2. Superficie")
    print("3. Nada (Volver al menú principal)")
    
    opcion = validaciones.entero("\nSeleccione una opción: ")

    match opcion:
        case 1:
            nueva_pob = validaciones.entero("Ingrese la NUEVA población: ")
            pais_encontrado["poblacion"] = nueva_pob
            print(f"¡Población actualizada a {nueva_pob}!")
            
        case 2:
            nueva_sup = validaciones.entero("Ingrese la NUEVA superficie en km²: ")
            pais_encontrado["superficie"] = nueva_sup
            print(f"¡Superficie actualizada a {nueva_sup} km²!")
            
        case 3:
            print("No se realizaron modificaciones. Volviendo al menú...")
            return  # Cortamos la función acá sin guardar nada
            
        case _:
            # Por si pone un número como 4, 5, etc.
            print("Opción inválida. Volviendo al menú principal sin realizar cambios.")
            return

    # Si modificó la opción 1 o 2, guardamos los cambios en el archivo CSV
    guardar_datos_csv("data/paises.csv", lista_paises)
    print(f"¡Los datos de '{pais_encontrado['nombre']}' se guardaron con éxito en el archivo!")