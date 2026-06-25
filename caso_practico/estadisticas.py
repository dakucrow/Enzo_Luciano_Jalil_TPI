def mostrar_estadisticas(lista_paises):
    """Calcula y muestra estadísticas demográficas y geográficas de los países."""
    # Verifico si la lista tiene elementos antes de procesar
    if not lista_paises:
        print("\nNo hay países registrados para calcular estadísticas.")
        return

    print("\n" + "="*40)
    print("      REPORTE ESTADÍSTICO GENERAL")
    print("="*40)

    # 1. Inicializo variables para los cálculos acumulativos
    total_poblacion = 0
    total_superficie = 0
    cantidad_paises = len(lista_paises)
    
    # Tomo el primer país de la lista como base inicial para realizar las comparaciones
    pais_mayor_pob = lista_paises[0]
    pais_menor_pob = lista_paises[0]
    
    # Estructuro un diccionario vacío para agrupar el conteo por continente
    conteo_continentes = {}

    # 2. Recorro la lista una sola vez para recolectar y procesar todos los datos en memoria
    for p in lista_paises:
        # Acumulo los valores para obtener los totales generales
        total_poblacion += p["poblacion"]
        total_superficie += p["superficie"]
        
        # Evalúo si el país actual supera el registro de mayor población
        if p["poblacion"] > pais_mayor_pob["poblacion"]:
            pais_mayor_pob = p
            
        # Evalúo si el país actual es menor al registro de menor población
        if p["poblacion"] < pais_menor_pob["poblacion"]:
            pais_menor_pob = p
            
        # Registro la cantidad por continente usando el método get para evitar errores de clave
        continente = p["continente"]
        conteo_continentes[continente] = conteo_continentes.get(continente, 0) + 1

    # 3. Realizo los cálculos matemáticos finales para los promedios
    promedio_pob = total_poblacion / cantidad_paises
    promedio_sup = total_superficie / cantidad_paises

    # 4. Imprimo los resultados finales formateando los números para mayor claridad
    print(f"• Total de países registrados: {cantidad_paises}")
    print(f"• País con MAYOR población:    {pais_mayor_pob['nombre']} ({pais_mayor_pob['poblacion']:,} hab.)")
    print(f"• País con MENOR población:    {pais_menor_pob['nombre']} ({pais_menor_pob['poblacion']:,} hab.)")
    print(f"• Promedio de población:       {promedio_pob:,.2f} habitantes")
    print(f"• Promedio de superficie:      {promedio_sup:,.2f} km²")
    
    print("\n--- Cantidad de países por continente ---")
    # Recorro el diccionario de continentes para mostrar el desglose individual
    for cont, cantidad in conteo_continentes.items():
        print(f"  - {cont}: {cantidad} {'país' if cantidad == 1 else 'países'}")
    print("="*40)