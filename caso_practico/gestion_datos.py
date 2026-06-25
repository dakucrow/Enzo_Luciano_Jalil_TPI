import csv
import validaciones
import consultas

def cargar_datos_csv(nombre_archivo):
    """Lee el archivo CSV y devuelve una lista de diccionarios con los países."""
    lista_paises = []
    try:
        # Intento abrir el archivo en modo lectura con codificación utf-8
        with open(nombre_archivo, mode='r', encoding='utf-8') as archivo:
            lector = csv.DictReader(archivo)
            # Recorro cada fila y extraigo los datos formateándolos correctamente
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
        # Abro el archivo en modo escritura para volcar los datos actualizados
        with open(nombre_archivo, mode='w', encoding='utf-8', newline='') as archivo:
            # Defino los encabezados necesarios para la estructura del archivo
            campos = ["nombre", "poblacion", "superficie", "continente"]
            escritor = csv.DictWriter(archivo, fieldnames=campos)
            
            escritor.writeheader()
            for pais in lista_paises:
                escritor.writerow(pais)
    except Exception as e:
        print(f"Error al guardar los datos en el archivo CSV: {e}")


def agregar_pais(lista_paises):
    """Solicita los datos de un nuevo país, los valida y los añade al sistema."""
    print("\n--- AGREGAR PAÍS ---")
    while True:
        # 1. Pido y valido el nombre del país
        nombre = validaciones.texto("Ingrese el nombre del país: ")
        
        # 2. Verifico que el país no exista previamente para evitar duplicados
        if validaciones.duplicado(nombre, lista_paises):
            print("Por favor, intente con otro nombre.\n")
        else:
            # Rompo el bucle si el nombre es válido y no está duplicado
            break 
            
    # 3. Pido y valido la población (debe ser entero positivo)
    poblacion = validaciones.entero("Ingrese la población (solo números enteros): ")

    # 4. Pido y valido la superficie (debe ser entero positivo)
    superficie = validaciones.entero("Ingrese la superficie en km² (solo números enteros):  ")

    # 5. Pido y valido el continente
    continente = validaciones.texto("Ingrese el continente: ")
    
    # Armo el nuevo diccionario con toda la información recolectada
    nuevo_pais = {
        "nombre": nombre,
        "poblacion": poblacion,
        "superficie": superficie,
        "continente": continente
    }
    # Agrego el nuevo registro a la lista en memoria RAM
    lista_paises.append(nuevo_pais)
    
    # Guardo inmediatamente el cambio directo en el archivo físico
    guardar_datos_csv("data/paises.csv", lista_paises)
    print(f"¡País '{nombre}' agregado y guardado con éxito!")


def actualizar_pais(lista_paises):
    """Busca un país y permite modificar campos específicos mediante un menú."""
    print("\n--- ACTUALIZAR DATOS DE UN PAÍS ---")
    nombre = validaciones.texto("Ingrese el nombre del país que desea actualizar: ")
    
    # Busco el país usando el buscador general
    pais_encontrado = consultas.buscar(nombre, lista_paises)
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

    # Evalúo la opción seleccionada por el usuario
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
            # Corto el flujo de la función para evitar reescribir el archivo sin cambios
            return  
            
        case _:
            print("Opción inválida. Volviendo al menú principal sin realizar cambios.")
            return

    # Si modificó la población o la superficie, guardo los cambios en el archivo CSV
    guardar_datos_csv("data/paises.csv", lista_paises)
    print(f"¡Los datos de '{pais_encontrado['nombre']}' se guardaron con éxito en el archivo!")