texto=input()
palabras = len(texto.split())  #Separo las palabras a traves de los espacios.
caracteres_con_espacios = len(texto)  #Cuento todos los caracteres.
caracteres_sin_espacios = len(texto.replace(' ', '').replace('\n', ''))  #Reemplazo los espacios en blanco y los saltos de linea por "" para contar el total de caracteres.
lineas = texto.count('\n') + 1  #Cuenta las líneas contando los saltos de línea. Suma 1 porque puede no haber salto de línea al final.
parrafos = len(texto.split('\n\n'))  #Cuenta los párrafos identificados por doble salto de línea
# Imprime la información obtenida
print(f"Palabras: {palabras}")
print(f"Caracteres (con espacios): {caracteres_con_espacios}")
print(f"Caracteres (sin espacios): {caracteres_sin_espacios}")
print(f"Líneas: {lineas}")
print(f"Párrafos: {parrafos}")