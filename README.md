# Gestor de Tickets de Soporte Técnico

Proyecto Integrador de Programación I.

## Equipo

Byte Solo - Grupo 10

### Integrante

Santino López

## Descripción

El proyecto consiste en un sistema de consola para registrar,
consultar y analizar tickets de soporte técnico.

La Etapa 1 funciona completamente en memoria. Los datos cargados
se pierden cuando finaliza la ejecución del programa.

## Problema

En un equipo pequeño de soporte técnico, los pedidos e incidencias
pueden quedar distribuidos entre mensajes, correos o notas.

El sistema centraliza la información básica de cada ticket y permite
consultar su estado, prioridad y categoría, además de generar
indicadores e informes.

## Datos de un ticket

Cada ticket contiene:

- Código.
- Fecha.
- Cliente.
- Categoría.
- Prioridad.
- Estado.
- Responsable.
- Descripción.

## Funcionalidades

El sistema permite:

1. Registrar tickets.
2. Listar tickets.
3. Buscar un ticket por código.
4. Cambiar el estado de un ticket.
5. Mostrar indicadores.
6. Detectar tickets y categorías en condición de alerta.
7. Mostrar distintos informes.
8. Finalizar el programa mediante el menú principal.

## Estructuras utilizadas

### Lista homogénea

La colección principal es una lista cuyos elementos son tuplas
que representan tickets con la misma estructura.

### Tuplas

Cada ticket se representa mediante una tupla.

También se utilizan tuplas para las categorías, prioridades
y estados permitidos.

### Matriz homogénea

Se utiliza una matriz de números enteros para representar
la cantidad de tickets según categoría y prioridad.

Las filas representan categorías y las columnas representan
prioridades.

### Cadenas

Se utilizan para códigos, fechas, clientes, categorías,
prioridades, estados, responsables y descripciones.

## Procesamientos realizados

El proyecto incluye:

- Acumulación del total de tickets.
- Acumulación por categoría.
- Conteo de tickets por estado.
- Búsqueda por código.
- Categoría con mayor cantidad de tickets.
- Detección de tickets críticos.
- Detección de categorías con acumulación de tickets abiertos.
- Ranking de categorías.
- Porcentaje de tickets resueltos.

## Uso de comprensión, slicing y lambda

Se utiliza comprensión para generar estructuras y obtener
tickets críticos.

Se utiliza slicing para reconstruir una tupla al modificar
el estado de un ticket.

Se utiliza lambda para ordenar el ranking de categorías
según su cantidad de tickets.

## Modularización

El proyecto está dividido en:

- main.py: menú, entrada de datos y presentación.
- datos.py: configuración y datos iniciales.
- operaciones.py: validaciones, búsquedas, cálculos y reglas.
- README.md: documentación del proyecto.

## Ejecución

Desde la carpeta del proyecto ejecutar: main.py
