import csv
categoria=str(input())
c=0
with open('datos.csv', newline='') as archivo:
    lector = csv.reader(archivo,delimiter=';') 
    for fila in lector:
        if len(fila) >= 2 and fila[1] == categoria:
            c+= 1
print(c)