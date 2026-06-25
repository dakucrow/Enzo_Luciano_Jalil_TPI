import validaciones

def buscar(busqueda, lista):
    """Busca por coincidencia parcial o exacta ignorando tildes y mayúsculas."""
    # Limpio la búsqueda que ingresó el usuario
    busqueda_limpia = validaciones.remover_acentos(busqueda)
    coincidencias = []
    
    # Filtro las coincidencias recorriendo la lista
    for p in lista:
        # Limpio el nombre del país actual para comparar en igualdad de condiciones
        nombre_pais_limpio = validaciones.remover_acentos(p["nombre"])
        
        if busqueda_limpia in nombre_pais_limpio:
            # Si la coincidencia es exacta, corto acá y devuelvo el país directo
            if nombre_pais_limpio == busqueda_limpia:
                return p
            coincidencias.append(p)

    # Evalúo los resultados obtenidos
    if not coincidencias:
        return None
        
    if len(coincidencias) == 1:
        return coincidencias[0]
        
    # Si encuentro múltiples opciones, le pido al usuario que elija
    print("\nSe encontraron múltiples opciones. Seleccione una:")
    for i, p in enumerate(coincidencias, start=1):
        print(f"{i}. {p['nombre']} ({p['continente']})")
    
    # Ejecuto un bucle para obligar al usuario a ingresar una opción correcta
    while True:
        opcion = validaciones.entero("\nSeleccione el número de opción: ")
        
        # Verifico que el número elegido esté dentro del rango de opciones válidas
        if 1 <= opcion <= len(coincidencias):
            # Resto 1 para obtener el índice correcto de la lista
            return coincidencias[opcion - 1]
        else:
            print(f"ERROR: Opción inválida. Debe ser un número entre 1 y {len(coincidencias)}.")


def filtrar_paises(lista_paises):
    """Muestra un menú para filtrar países por continente o rangos numéricos."""
    if not lista_paises:
        print("No hay países registrados para filtrar.")
        return

    print("\n--- FILTRAR PAÍSES ---")
    print("1. Por Continente")
    print("2. Por Rango de Población")
    print("3. Por Rango de Superficie")
    print("4. Volver al menú principal")
    
    opcion = validaciones.entero("\nSeleccione una opción de filtrado: ")
    resultados = []

    match opcion:
        case 1:
            # Pido el continente e ignoro mayúsculas y tildes
            continente_buscar = validaciones.texto("Ingrese el continente a buscar: ")
            continente_buscar_limpio = validaciones.remover_acentos(continente_buscar)
            
            # Armo la lista filtrada comparando las cadenas limpias
            resultados = [p for p in lista_paises if validaciones.remover_acentos(p["continente"]) == continente_buscar_limpio]
            
        case 2:
            min_pob = validaciones.entero("Ingrese la población MÍNIMA: ")
            max_pob = validaciones.entero("Ingrese la población MÁXIMA: ")
            resultados = [p for p in lista_paises if min_pob <= p["poblacion"] <= max_pob]
            
        case 3:
            min_sup = validaciones.entero("Ingrese la superficie MÍNIMA (km²): ")
            max_sup = validaciones.entero("Ingrese la superficie MÁXIMA (km²): ")
            resultados = [p for p in lista_paises if min_sup <= p["superficie"] <= max_sup]
            
        case 4:
            return
        case _:
            print("Opción inválida. Volviendo...")
            return

    # Muestro los resultados obtenidos en el filtrado
    if not resultados:
        print("\nNo se encontraron países que cumplan con los criterios especificados.")
    else:
        print(f"\n--- SE ENCONTRARON {len(resultados)} COINCIDENCIAS ---")
        for p in resultados:
            print(f"- {p['nombre']} | Continente: {p['continente']} | Población: {p['poblacion']} | Superficie: {p['superficie']} km²")


def ordenar_paises(lista_paises):
    """Muestra un menú para ordenar la lista de países por diferentes criterios."""
    if not lista_paises:
        print("No hay países registrados para ordenar.")
        return

    print("\n--- ORDENAR PAÍSES ---")
    print("1. Por Nombre")
    print("2. Por Población")
    print("3. Por Superficie")
    print("4. Volver al menú principal")
    
    criterio = validaciones.entero("\nSeleccione el criterio de ordenamiento: ")
    clave_orden = ""

    match criterio:
        case 1: clave_orden = "nombre"
        case 2: clave_orden = "poblacion"
        case 3: clave_orden = "superficie"
        case 4: return
        case _:
            print("Opción inválida.")
            return

    print("\n¿En qué sentido desea ordenar?")
    print("1. Ascendente (Menor a Mayor / A-Z)")
    print("2. Descendente (Mayor a Menor / Z-A)")
    sentido = validaciones.entero("\nSeleccione el sentido: ")

    if sentido == 1:
        descendente = False
    elif sentido == 2:
        descendente = True
    else:
        print("Opción inválida. Se ordenará de forma ascendente por defecto.")
        descendente = False

    # Ordeno usando sorted para no alterar la lista que está guardada en memoria original
    if clave_orden == "nombre":
        # Uso lower() en la clave del nombre para que ordene alfabéticamente de forma correcta
        lista_ordenada = sorted(lista_paises, key=lambda x: x[clave_orden].lower(), reverse=descendente)
    else:
        lista_ordenada = sorted(lista_paises, key=lambda x: x[clave_orden], reverse=descendente)

    # Imprimo en pantalla el resultado del ordenamiento
    print("\n--- LISTA ORDENADA ---")
    for p in lista_ordenada:
        print(f"- {p['nombre']} | Población: {p['poblacion']} | Superficie: {p['superficie']} km² | Continente: {p['continente']}")