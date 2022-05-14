# WORLD CRAFT ASCII: Parte 2
> Elaborado por: Ferney Vanegas Hernández

> Misión Tic 2022

## **Contexto**
Una vez que un jugador ha sido registrado y aceptado en World Craft ASCII, está listo para ser asignado a un mundo

## **Identificación del Problema (I)**
### Objetivo
* Crear una lista de posiciones (Coordenadas) aleatorias para el mundo, cuyas dimensiones son escogidas por el usuario
* Con las coordenadas construir el mundo
### Interesados
* Personas que ya fueron aceptadas y están registradas en el juego interactivo World Craft ASCII

## **Definición del Problema (D)**
### ¿Qué información conozco se me ha suministrado?

* Deben presentarse 4 listas:
    * lista con número de ﬁlas
    * Lista con número de columnas,
    * Lista con ancho del muro
    * Lista con largo del muro     
* La lista que se crea como producto de las enteriores debería ser como:
    * muros=["0:2”,”1:0","1:1","1:2","2:1","2:2",”3:1”,”3:2”,”4:1”,”4:2”]
![ejemplo](img/Ejemplo.jpg 'Ejemplo de ejercicio')

### ¿Qué información debo conocer?
* Manejo de expresiones (ariméticas, relacionales y lógicas) en Python
* Manejo de Flujos secuenciales en Python
* Manejo de Flujos condicionales en Python
* Manejo de Flujos cíclicos en Python
* Manejo de modulos en Python
* Manejo de funciones en Python
* Manejo de listas en Python (Estructuras de datos)

### División del problema

* Definir un módulo principal
* Definir un módulo que proporcione lista con número de ﬁlas
* Definir un módulo que proporcione lista con número de columnas,
* Definir un módulo que proporcione lista con ancho del muro
* Definir un módulo que proporcione lista con largo del muro
* Recibir las listas en el main
* Construir la lista final
* Imprimir el mapa del mundo con los muros

## **Estratégia (E)**
### Ejemplos Particulares
* Ejemplo:
    * Lista ﬁlas: = [0,3,5,6]
    * Lista columnas = [1,3,11,12]
    * Lista anchos = [2,9,1,4]
    * Lista largos = [5,2,2,1]
    ![ejemploEspecifico](img/EjemploEspecifico.jpg 'Ejemplo Específico')
* Pruebas
![Pruebas](img/PruebasHechas.jpg 'Pruebas para compresion')
### Estratégia de Solucion
1. Voy a separar las listas diferentes en módulos
2. Voy a recibirlas en el módulo principal
3. Voy a implementar una funcioń (en otro módulo) que me construya lista de coordenadas según las listas recibidas
4. Voy a implementar una función (en otro módulo) que reciba la lista unificada y escriba los muros

## **Algoritmos (A)**

### Algoritmo: get_rows
*Parámetros: Ninguno*
* Funcion rows <- get_rows ():
    * rows = [azar(31),azar(31),azar(31),azar(31)]
    * Retorne rows
* FinFuncion
***
### Algoritmo: get_columns
*Parámetros: Ninguno*
* Funcion columns <- get_columns ():
    * columns = [azar(31),azar(31),azar(31),azar(31)]
    * Retorne columns
* FinFuncion
***
### Algoritmo: get_widths
*Parámetros: Ninguno*
* Funcion widths <- get_widths ():
    * widths = [azar(31),azar(31),azar(31),azar(31)]
    * Retorne widths
* FinFuncion
***
### Algoritmo: get_longs
*Parámetros: Ninguno*
* Funcion longs <- get_longs ():
    * longs = [azar(31),azar(31),azar(31),azar(31)]
    * Retorne longs
* FinFuncion
***
### Algoritmo: get_coord_walls
*Parámetros: rows, columns, widhts, longs, dim*
* Funcion coord_walls <- get_coord_walls ():
    * Dimension coord_walls[]
    * Longitud_de_los_arrays = 4
    * Para general_index<-0 Hasta Longitud_de_los_arrays con Paso 1 Hacer
        * Para i<-rows[general_index] Hasta (rows[general_index] + longs[general_index])  con Paso 1 Hacer
            * Para j<-columns[general_index] Hasta (columns[general_index]  + widths[general_index])  con Paso 1 Hacer
                * coord_walls = coord_walls + Dimension coordenanda[i,j]
            * FinPara
        * FinPara
    * FinPara
    * /*Limpiar las coordenadas que sobran*/
    * Longitud_coord_walls
    * Para i<-0 Hasta Longitud_coord_walls con Paso -1
        * Si coord_walls[i][0] > dim or coord_walls[i][1] > dim Entonces
            /*Eliminar del array*/
            * Llamar eliminar(coord_walls[i])
        * FinSi
    * FinPara
    * Retorne coord_walls
* FinFuncion
***
### Algoritmo: construct_walls
*Parámetros: coord_walls, dim*
* Funcion construct_walls():
    * BRICK=*#*
    * SPACE=' '
    * Longitud_coord_walls = 32  /* Suponiendo, este valor varia pero hace referencia a la cantidad de coordenadas */
    * Para cada i<-0 Hasta dim con Paso 1 Hacer
        * row = ''
        * Para cada j<-0 Hasta dim con Paso 1 Hacer
            * /*Con i y j ya tenemos una coordenada. Ahora, revisar si está en la lista*/
            * cordenada_existe=Falso
            * Para cada coord<-0 Hasta Longitud_coord_walls con Paso 1 Hacer:
                * Si coord_walls[coord][0] == i and coord_walls[coord][1]==j Entonces
                    * cordenada_existe=True
                * FinSi
            * FinPara
            * Si cordenada_existe=True Entonces
                * row+=BRICK
            * SiNo
                * row+=SPACE
            * FinSi
        * FinPara
        * Escriba row
    * FinPara
* FinFuncion
***
### Algoritmo: main
*Parámetros: Ninguno*
* Funcion main ():
    * Leer dim /*Dimensiones del cuadrado. Un número*/
    * Dimension rows = Llamar get_rows(dim)
    * Dimension columns = Llamar get_columns(dim)
    * Dimension widths = Llamar get_widths(dim)
    * Dimension longs = Llamar get_longs(dim)
    * Dimension walls = Llamar get_walls(rows, columns, widths, longs, dim)
    * Imprimir walls
    * Llamar construct_walls(walls, dim)
* FinFuncion

## **Logros (L)**


