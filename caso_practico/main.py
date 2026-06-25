# Importo los módulos locales necesarios para el funcionamiento del sistema
import gestion_datos
import consultas
import estadisticas
import validaciones

def menu_principal():
    """Controla el flujo del programa principal mediante un menú interactivo."""
    # Defino la ruta del archivo de datos dentro del proyecto
    archivo = "data/paises.csv"
    # Cargo la lista de países en memoria RAM al iniciar el sistema
    paises = gestion_datos.cargar_datos_csv(archivo)
    
    while True:
        print("\n" + "="*40)
        print("  SISTEMA DE GESTIÓN DE PAÍSES (UTN) ")
        print("="*40)
        print("1. Agregar país")
        print("2. Actualizar población/superficie")
        print("3. Buscar país por nombre")
        print("4. Filtrar países")
        print("5. Ordenar países")
        print("6. Mostrar estadísticas")
        print("7. Salir")
        print("="*40)
        
        opcion = input("Seleccione una opción (1-7): ").strip()
        
        # Evalúo la opción ingresada en el menú principal
        match opcion:
            case "1":
                gestion_datos.agregar_pais(paises)
                input("\nPresione ENTER para continuar...")
                
            case "2":
                gestion_datos.actualizar_pais(paises)
                input("\nPresione ENTER para continuar...")
                
            case "3":
                print("\n--- BUSCAR PAÍS ---")
                nombre = validaciones.texto("Ingrese el nombre del país que desea buscar: ")
                
                # Invoco al buscador universal pasando la lista cargada
                pais_encontrado = consultas.buscar(nombre, paises)
                
                if pais_encontrado:
                    # Imprimo en pantalla la ficha completa si obtuve una coincidencia
                    print(f"\n[ RESULTADO DE LA BÚSQUEDA ]")
                    print(f"Nombre:     {pais_encontrado['nombre']}")
                    print(f"Continente: {pais_encontrado['continente']}")
                    print(f"Población:  {pais_encontrado['poblacion']:,} habitantes")
                    print(f"Superficie: {pais_encontrado['superficie']:,} km²")
                else:
                    print(f"\nNo se encontró ningún país que coincida con '{nombre}'.")
                input("\nPresione ENTER para continuar...")
                
            case "4":
                consultas.filtrar_paises(paises)
                input("\nPresione ENTER para continuar...")
                
            case "5":
                consultas.ordenar_paises(paises)
                input("\nPresione ENTER para continuar...")
                
            case "6":
                estadisticas.mostrar_estadisticas(paises)
                input("\nPresione ENTER para continuar...")
                
            case "7":
                print("Saliendo del sistema. ¡Chau!")
                # Rompo el bucle principal para finalizar la ejecución
                break
                
            case _:
                print("Opción inválida. Por favor, elija un número del 1 al 7.")

if __name__ == "__main__":
    # Inicializo la ejecución del programa
    menu_principal()