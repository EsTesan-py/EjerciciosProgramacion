print("Ingrese texto 1.")
texto1= str(input())
print("Ingrese texto 2.")
texto2= str(input())
contadort1=0
contadort2=0
for i in texto1:
    contadort1+=1
for i in texto2:
    contadort2+=1
if contadort1>contadort2:
    print("Cadena mayor: ",texto1)
    print("Cadena menor: ",texto2)
    print("Caracteres: mayor-> ",contadort1," | menor-> ",contadort2)
else:
    print("Cadena mayor: ",texto2)
    print("Cadena menor: ",texto1)
    print("Caracteres: mayor-> ",contadort2," | menor-> ",contadort1)