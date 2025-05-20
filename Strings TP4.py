print("Ingresar cadena.")
cadena=str(input())
print("Ingresar subcadena a encontrar.")
subcadena=str(input())
contador=0
acum=0
subcadenero=0
for a in subcadena:
    acum+=1
for i in cadena:
    if i==subcadena[contador]:
        contador+=1
    else:
        contador=0
    if contador==acum:
        contador=0
        subcadenero+=1
print("La subcadena se repite ",subcadenero," veces.")