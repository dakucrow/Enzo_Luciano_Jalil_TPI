import unicodedata

def remover_acentos(texto):
    """Transforma caracteres con tilde en su versión limpia (ej: América -> America)."""
    # Descompongo los caracteres con acentos en sus componentes básicos
    texto_normalizado = unicodedata.normalize('NFD', texto)
    # Filtro y mantengo solo las letras, eliminando los símbolos de las tildes
    return "".join(c for c in texto_normalizado if unicodedata.category(c) != 'Mn').lower().strip()

def texto(txt):
    """Solicita un texto al usuario, valida que no esté vacío y que contenga solo letras."""
    while True:
        input_txt = input(txt).strip()
        
        # Verifico que el usuario no haya presionado Enter sin escribir nada
        if input_txt == "":
            print("ERROR: No puede estar vacío.")
        # Reemplazo temporalmente los espacios para validar que el resto sean solo letras
        elif not input_txt.replace(" ", "").isalpha():
            print("ERROR: Ingrese solo letras.")
        else:
            # Retorno el texto original con sus espacios correctos
            return input_txt

def duplicado(txt, lista_paises):
    """Devuelve True si el país ya existe (ignorando tildes y mayúsculas), False si no."""
    # Limpio el texto ingresado por el usuario sacando tildes y espacios
    txt_limpio = remover_acentos(txt)
    
    # Recorro la lista de países para comparar uno por uno
    for p in lista_paises:
        # Si encuentro una coincidencia exacta sin tildes, aviso del error
        if remover_acentos(p["nombre"]) == txt_limpio:
            print(f"Error: El país '{p['nombre']}' ya se encuentra registrado.")
            return True
    return False

def entero(txt):
    """Solicita un número, valida que no esté vacío, que sea entero y positivo."""
    while True:
        entrada = input(txt).strip()
        
        # Valido específicamente si el campo viene vacío
        if entrada == "":
            print("ERROR: El campo no puede estar vacío. Debe ingresar un número.")
            continue  
            
        try:
            # Intento convertir la entrada de texto a un número entero
            numero = int(entrada)
            # Verifico que el número no sea una cantidad negativa
            if numero < 0:
                print("ERROR: No se aceptan cantidades negativas para este campo.")
            else:
                # Retorno el número válido si pasó todos los controles
                return numero 
                
        except ValueError:
            # Capturo el error si la conversión falla por letras o decimales
            print("ERROR: Formato inválido. Asegúrese de ingresar SOLO números enteros (sin letras, espacios internos ni decimales).")