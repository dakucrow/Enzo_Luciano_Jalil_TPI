# Importamos las funciones de los otros archivos (.py)
import gestion_datos
import consultas
import estadisticas
import validaciones


def menu_principal():
    # Buscamos el archivo dentro de la carpeta 'data'
    archivo = "data/paises.csv"
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
        
        # Menu principal programa
        match opcion:
            case "1":
                gestion_datos.agregar_pais(paises)
            case "2":
                gestion_datos.actualizar_pais(paises)
            case "3":
                consultas.buscar_pais(paises)
            case "4":
                consultas.filtrar_paises(paises)
            case "5":
                consultas.ordenar_paises(paises)
            case "6":
                estadisticas.mostrar_estadisticas(paises)
            case "7":
                print("Saliendo del sistema. ¡Buenas noches!")
                break
            case _:
                print("Opción inválida. Por favor, elija un número del 1 al 7.")
if __name__ == "__main__":
    menu_principal()