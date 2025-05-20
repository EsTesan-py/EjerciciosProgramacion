print("Ingresar cadena de caracteres.")
cadena=str(input())
contador=0
acumvocales=0
acumespacio=0
palabreo=0
es_palabra = False
for i in cadena:
    contador+=1
    if i in "aeiouAEIOU":
        acumvocales += 1
    if i==" ":
        acumespacio+=1
        es_palabra = False  
    elif not es_palabra:
        if i in "FfMm":
            palabreo += 1
        es_palabra = True

print("Vocales: ",acumvocales)
print("Espacios: ",acumespacio)
print("Palabras con FMfm: ",palabreo)