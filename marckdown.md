# Explicación de las funciones

## Índice
1.  [función1](#uno)
2.  [función2](#dos)
3.  [Datos](#datos)


## 1. PRIMERA FUNCION 
<div id = uno></div>
1. Creo la función  buscarPalabra en el que le paso la lista de nombres y un objetivo.

2. Hago comprobar si la palabra objetivo se encuentra en la lista nombres, dependiendo del resultado le devolvera True o False.
>Si le doy un nombre no funcionaría ya que el bucle no recorrería nada. 

3. Por último, devuelvo el resultado del apartado anterior.

Quedando así el código:


```py
def buscarPalabra(objetivo,nombres):

    TF = False
    if objetivo in nombres:
        TF = True

    return TF

```


## 2. SEGUNDA FUNCIÓN
<div id = dos></div>
1. Creo la función imprimirListaInversa en el que le paso la lista de nombres.

2. Creo un bucle en el que recorre toda la lista de forma invertida.
> Si le doy un nombre no funcionaría ya que el bucle no recorrería nada. Igual que en el primer apartado.
3.En cada recorrido del bucle voy imprimiendo el valor de la celda en la que se esta recorriendo el bucle y después hago un salto de línea.

Quedando así el código:

```py
def imprimirListaInversa(nombres):
    for nombre in range(nombre,-1,-1):
        print(nombre)
        print()

```


## DATOS OFRECIDOS  <div id = datos></div>

|    nombre   |  edad  |
|  ---------- | ------ |
|   Mengano   |     0  |
|   Fulano    |    25  | 
|   Zutano    |    50  |  
|   Perantano |    75  | 

