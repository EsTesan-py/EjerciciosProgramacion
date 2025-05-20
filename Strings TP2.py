cadena1= str(input())
cadena2= str(input())
contador=0
igualdad=True

for c in cadena1:
    if igualdad==True:
        if c==cadena2[contador]:
            contador+=1
        else:
            print("No son iguales")
            igualdad=False
if igualdad==True:
    print("Son iguales")

    

