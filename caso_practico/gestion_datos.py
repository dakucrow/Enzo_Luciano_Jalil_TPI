import csv

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

# Funciones vacías para mañana
def agregar_pais(lista): pass
def actualizar_pais(lista): pass