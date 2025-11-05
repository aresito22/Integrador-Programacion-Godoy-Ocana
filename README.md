# README --- Proyecto Integrador: Gestión de Países (Python)

## Descripción del programa

Este proyecto es una aplicación de consola desarrollada en Python que
permite consultar información de países utilizando un archivo CSV con
datos de nombre, población, superficie y continente.

El programa ofrece funcionalidades como:

-   Búsqueda de países por nombre (coincidencia exacta y parcial)
-   Normalización del texto para búsquedas flexibles (sin tildes)
-   Filtrado de países por continente
-   Lectura dinámica de archivos CSV

El proyecto está organizado en tres archivos principales:

-   main.py: menú y control del flujo del programa\
-   funciones.py: funciones principales (buscar, filtrar, mostrar)\
-   utilidades.py: funciones auxiliares como quitar_tildes\
-   paises.csv: base de datos con más de 150 países

## Estructura del proyecto

    /integrador_programacion
    │
    ├── main.py
    ├── funciones.py
    ├── utilidades.py
    ├── paises.csv
    └── README.md

## Instrucciones de uso

### 1. Ejecutar el programa

Ejecutar el archivo principal:

    python main.py

### 2. Menú principal

El programa mostrará un menú con opciones como:

    ---- Menú de países ----
    1. Buscar país por nombre
    2. Filtrar países por continente
    3. Salir
    Elige una opción:

### 3. Búsqueda de países

El usuario ingresa un nombre parcial o exacto.\
El programa no distingue mayúsculas/minúsculas y remueve tildes para
facilitar la búsqueda.

### 4. Filtrar por continente

Permite listar todos los países pertenecientes a un continente
específico.\
Los continentes válidos son América, Europa, Asia, África y Oceanía.

## Ejemplos de entrada y salida

### Ejemplo 1 --- Búsqueda exacta

Entrada:

    Nombre del país a buscar: Argentina

Salida:

    Argentina
    Población: 46612000
    Superficie: 2780400 km^2

### Ejemplo 2 --- Búsqueda parcial

Entrada:

    Nombre del país a buscar: guin

Salida:

    Guinea — Población: 14500000 — Superficie: 245857 km^2
    Guinea Ecuatorial — Población: 1850000 — Superficie: 28051 km^2
    Guinea-Bisáu — Población: 2100000 — Superficie: 36125 km^2

### Ejemplo 3 --- Búsqueda sin tildes

Entrada:

    Nombre del país a buscar: mexico

Salida:

    México
    Población: 130800000
    Superficie: 1964375 km^2

### Ejemplo 4 --- Filtrar por continente

Entrada:

    Nombre del continente a filtrar: europa

Salida (fragmento):

    España — Población: 48600000 — Superficie: 505990 km^2
    Francia — Población: 68100000 — Superficie: 551695 km^2
    Alemania — Población: 83294633 — Superficie: 357022 km^2

### Ejemplo 5 --- País no encontrado

Entrada:

    Nombre del país a buscar: asdf

Salida:

    País no encontrado.

## Autores

Joaquín Godoy
Ares Ocaña