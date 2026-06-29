link youtube: https://youtu.be/_ii1F_GkNuE
link pdf: https://drive.google.com/file/d/1PteBZ7XQTEiq9XhZ07-39QSyqRucey3R/view?usp=sharing
# Enzo_Luciano_Jalil_TPI
 tp integrador UTN programacion 1
Integrantes y Participación

    Luciano - Desarrollo completo de la lógica de negocio, arquitectura modular, optimización de algoritmos de búsqueda y blindaje de validaciones. (Participación: 100%)

# Sistema de Gestión de Países (UTN)

Este proyecto consiste en un sistema de consola desarrollado en Python para la gestión, consulta y análisis estadístico de datos demográficos y geográficos de diferentes países del mundo. El sistema interactúa de forma directa con un archivo físico en formato CSV, asegurando la persistencia de los datos entre ejecuciones.

## 🚀 Características y Funcionalidades

El programa cuenta con un menú interactivo que permite realizar las siguientes acciones:
1. **Agregar país:** Permite registrar nuevos países validando que el nombre no esté duplicado (ignorando tildes y mayúsculas), y que los datos numéricos sean válidos.
2. **Actualizar datos:** Busco un país específico y modifico su población o superficie, guardando el cambio inmediatamente en el archivo CSV.
3. **Buscar país:** Busco por coincidencia exacta o parcial. Si encuentro múltiples opciones, muestro un menú para elegir la correcta.
4. **Filtrar países:** Genero listas específicas por continente o por rangos numéricos (población/superficie).
5. **Ordenar países:** Muestro la lista ordenada por nombre, población o superficie de manera ascendente o descendente sin alterar el orden original del archivo.
6. **Mostrar estadísticas:** Proceso toda la lista en una sola pasada para calcular promedios, máximos, mínimos y el conteo de países por continente.

## 🛠️ Arquitectura del Proyecto

El código está estructurado de manera modular para garantizar la escalabilidad y limpieza:
* `main.py`: Punto de entrada del programa y control del menú principal.
* `gestion_datos.py`: Manejo de lectura/escritura del archivo CSV (`data/paises.csv`) y operaciones de guardado.
* `consultas.py`: Funciones de búsqueda, filtrado y ordenamiento de datos.
* `estadisticas.py`: Cálculos demográficos y geográficos generales.
* `validaciones.py`: Centralización de controles de entrada (textos vacíos, números enteros positivos, control de duplicados y normalización de tildes).

## 📊 Dataset Base (`data/paises.csv`)
El archivo incluye columnas estándar limpias y sin espacios corruptos:
`nombre,poblacion,superficie,continente`
## 💻 Ejemplos de Uso (Entradas y Salidas)

### Ejemplo 1: Búsqueda Inteligente (Con tildes y coincidencias múltiples)
Si ingreso a la opción de búsqueda e introduzco un término parcial y sin tilde:
```text
Ingrese el nombre del país que desea buscar: arg

Se encontraron múltiples opciones. Seleccione una:
1. Argentina (América)
2. Argelia (África)

Seleccione el número de opción: 1

[ RESULTADO DE LA BÚSQUEDA ]
Nombre:     Argentina
Continente: América
Población:  46,200,000 habitantes
Superficie: 2,780,400 km²
