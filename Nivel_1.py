

#Nivel 1: El usuario va a ingresar un texto por teclado y debemos determinar cual es la palabra feliz.
#Una palabra feliz se la considera aquella que tiene 2 vocales iguales en dicha palabra Ejemplo: Cooperativa, booleano, gaara.

#Nivel 2: Dada una matriz (MxN) la cual se la considera un diccionario de palabras se solicita encontrar 
#en dicho diccionario CUANTAS palabras felices se encuentran en él. Ejemplo: Gaara, Coop.
Lleno una matriz de palabras y con un doble ciclo for voy a ir recorriendo la matriz, a cada elemento que voy
a ir recorriendo va a ser sometido a la funcion anteriormente realizada en el nivel 1 para encontrar las vocales
iguales, si este elemento la contiene, va a sumarse un valor mas a un contador que se va a ir actualizando o no
segun si el elemento es o no es una palabra feliz, al finalizar daria con el resultado de cuantas palabras son felices

#Nivel 3: Dado un archivo el cual contiene el diccionario de palabras se solicita encontrar en ese diccionario
# la palabra o las palabras felices mostrandoló por pantalla y en otro archivo. 
Empezaria abriendo el archivo con un "with open(nombrearchivo,r) as archivo" a, ahi exploraria el archivo para recolectar

texto=str(input())
palabrero=texto.split()
vocales="aeiouAEIOU"
for i in palabrero:
    if i in vocales:
        print("Tiene vocales")


        