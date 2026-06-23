import csv

def validar_y_limpiar_fila(fila):
    """
    Valida y limpia una fila del CSV. 
    Devuelve el diccionario del país si es válido, o None si tiene errores.
    """
    try:
        # 1. Comprobar que no haya datos vacíos en los campos obligatorios
        if not fila["nombre"] or not fila["poblacion"] or not fila["superficie"] or not fila["continente"]:
            return None

        # 2. Limpiar y transformar tipos de datos
        return {
            "nombre": fila["nombre"].strip(),
            "poblacion": int(fila["poblacion"].strip()),
            "superficie": int(fila["superficie"].strip()),
            "continente": fila["continente"].strip()
        }
    except (ValueError, KeyError, TypeError):
        # Captura si falta una columna, si no es número, o si viene un None
        return None