# Gestor de Países (CSV)

Este es un programa de consola en Python diseñado para gestionar y
analizar una base de datos de países almacenada en un archivo
`paises.csv`.

## Descripción del programa

El programa utiliza el módulo `csv` de Python para leer y analizar datos
de un archivo `paises.csv`. Permite realizar las siguientes operaciones
principales:

### Buscar país

Busca un país por nombre (coincidencia exacta o parcial).

### Filtrar países

Ofrece un submenú para filtrar la lista por: - Continente\
- Rango de población\
- Rango de superficie

### Ordenar países

Permite ordenar la lista completa de países por: - Nombre\
- Población\
- Superficie\
En orden ascendente o descendente.

### Mostrar estadísticas

Calcula y muestra: - País con mayor población\
- País con menor población\
- Promedio de población\
- Promedio de superficie\
- Conteo de países por continente

## Instrucciones de uso

Este script (`funciones.py`) contiene la lógica de las operaciones. Para
funcionar, requiere:

-   Un script principal (`main.py`) que importe estas funciones y
    muestre el menú al usuario.

-   Un archivo de datos `paises.csv` con los encabezados:

        nombre,poblacion,superficie,continente

-   Un módulo `utilidades.py` que incluya la función
    `normalizar_caracteres()`.

## Ejemplos de entradas y salidas

### Ejemplo 1: Buscar un país (coincidencia parcial)

**Entrada:**

    Nombre del país a buscar: arg

**Salida:**

    Argentina
    Población: 46,621,847
    Superficie: 2,780,400 km²

------------------------------------------------------------------------

### Ejemplo 2: Filtrar países

#### Opción 1: Filtrar por continente

**Entrada:**

    Nombre del continente a filtrar: América

**Salida:**

    Argentina
    Población: 46,621,847
    Superficie: 2,780,400 km²

    Brasil
    Población: 216,422,446
    Superficie: 8,515,767 km²

    Estados Unidos
    Población: 339,996,563
    Superficie: 9,833,517 km²

#### Opción 2: Filtrar por rango de población

**Entrada:**

    Límite inferior: 1000000000
    Límite superior: 2000000000

**Salida:**

    China
    Población: 1,425,671,352
    Superficie: 9,596,961 km²

    India
    Población: 1,428,627,663
    Superficie: 3,287,263 km²

#### Opción 3: Filtrar por rango de superficie

**Entrada:**

    Límite inferior: 8000000
    Límite superior: 10000000

**Salida:**

    Brasil
    Población: 216,422,446
    Superficie: 8,515,767 km²

    China
    Población: 1,425,671,352
    Superficie: 9,596,961 km²

    Estados Unidos
    Población: 339,996,563
    Superficie: 9,833,517 km²

------------------------------------------------------------------------

### Ejemplo 3: Ordenar países

#### Opción 1: Ordenar por nombre (ascendente)

**Salida (extracto):**

    Alemania
    Población: 83,294,633
    Superficie: 357,022 km²
    Continente: Europa

    Argentina
    Población: 46,621,847
    Superficie: 2,780,400 km²
    Continente: América

#### Opción 2: Ordenar por población (descendente)

**Salida (extracto):**

    India
    Población: 1,428,627,663
    Superficie: 3,287,263 km²
    Continente: Asia

    China
    Población: 1,425,671,352
    Superficie: 9,596,961 km²
    Continente: Asia

#### Opción 3: Ordenar por superficie (ascendente)

**Salida (extracto):**

    Ciudad del Vaticano
    Población: 518
    Superficie: 0 km²
    Continente: Europa

    Mónaco
    Población: 36,297
    Superficie: 2 km²
    Continente: Europa

------------------------------------------------------------------------

### Ejemplo 4: Mostrar estadísticas

    === ESTADÍSTICAS ===
    Mayor población: India (1,428,627,663 habitantes)
    Menor población: Ciudad del Vaticano (518 habitantes)
    Promedio de población: 40,278,309 habitantes
    Promedio de superficie: 693,587 km²

    Cantidad de países por continente:
    África: 57
    América: 42
    Asia: 50
    Europa: 46
    Oceanía: 3

------------------------------------------------------------------------

### Ejemplo 5: Agregar país

**Entrada:**
    === AGREGAR NUEVO PAÍS ===
    Nombre del país: Imperio Godoycruceño
    Población: 93517351
    Superficie (km^2): 105677432
    Continente: América

**Salida:**

    País añadido exitosamente. # Se agrega el país con sus atributos al CSV

------------------------------------------------------------------------

## Participación de los integrantes

-   Joaquín Godoy
-   Ares Martín Ocaña