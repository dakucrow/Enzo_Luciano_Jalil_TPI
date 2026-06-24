def texto(txt):
    while True:
        texto = input(txt).strip()
        
        if texto == "":
            print("ERROR: No puede estar vacío.")
        # Reemplazamos los espacios por nada ("") SOLO para la validación
        elif not texto.replace(" ", "").isalpha():
            print("ERROR: Ingrese solo letras.")
        else:
            return texto  # Retorna el texto original (con sus espacios intactos)
def duplicado(txt, diccionario):
    # Recorremos la lista de diccionarios
    for p in diccionario:
        if p["nombre"].lower() == txt.lower():
            print(f"Error: '{txt}' ya existe en el sistema.")
            return True # Retorna True si ENCONTRÓ un duplicado
            
    return False # Retorna False si recorrió toda la lista y NO hay duplicados
def entero(txt):
    while True:
        entrada = input(txt).strip()
        # 1. Validamos específicamente si está vacío
        if entrada == "":
            print("ERROR: El campo no puede estar vacío. Debe ingresar un número.")
            continue  # Salta al inicio del bucle para volver a preguntar
        try:
            # 2. Intentamos convertir a entero
            numero = int(entrada)
            # 3. Validamos que no sea negativo
            if numero < 0:
                print("ERROR: No se aceptan cantidades negativas para este campo.")
            else:
                return numero # Si pasó todas las pruebas, devuelve el entero válido
                
        except ValueError:
            # 4. Si falla la conversión, es porque tiene letras, puntos decimales o símbolos
            print("ERROR: Formato inválido. Asegúrese de ingresar SOLO números enteros (sin letras, espacios internos ni decimales).")
def buscar(busqueda, lista):
    """Busca por coincidencia parcial o exacta.
    Devuelve el diccionario encontrado o None."""
    busqueda = busqueda.lower()
    coincidencias = []
    
    # Filtrar coincidencias
    for p in lista:
        if busqueda in p["nombre"].lower():
            # Si es exacta, vamos directo con este sin mostrar menú
            if p["nombre"].lower() == busqueda:
                return p
            coincidencias.append(p)

    # Validar resultados
    if not coincidencias:
        return None
        
    if len(coincidencias) == 1:
        return coincidencias[0]
        
    # --- El usuario elige entre las opciones ---
    print("\nSe encontraron múltiples opciones. Seleccione una:")
    for i, p in enumerate(coincidencias, start=1):
        print(f"{i}. {p['nombre']} ({p['continente']})")
    
    # Bucle para obligar al usuario a elegir una opción válida
    while True:
        # Usamos la lógica de validar entero 
        opcion = entero("\nSeleccione el número de opción: ")
        
        # Validamos que el número esté entre 1 y la cantidad de coincidencias
        if 1 <= opcion <= len(coincidencias):
            # Restamos 1 porque las listas en Python empiezan en 0
            return coincidencias[opcion - 1]
        else:
            print(f"ERROR: Opción inválida. Debe ser un número entre 1 y {len(coincidencias)}.")