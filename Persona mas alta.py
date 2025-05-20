#Procedo a declarar las variables 
Altura = float()
Nombre = str()
Apellido = str()
Cuit = str()
nmax = str() #Nombre de la persona mas alta
amax = str() #Apellido de la persona mas alta
alturamax = float(0) #Altura de la persona mas alta
cmax = str() #Cuit de la persona mas alta
i = int(1) #Variable para el contador

print("Coloque la cantidad de personas que hay en la comision")
cant = int(input()) #Pido cantidad de personas para hacer el "PARA" o "FOR"
for i in range(0, cant):
    print("Coloque su nombre: ")
    Nombre = input()
    print("Coloque su apellido: ")
    Apellido = input()
    print("Coloque su cuit: ")
    Cuit = input()
    print("Coloque su altura: ")
    Altura = float(input())
if Altura > alturamax: #Comparo la altura del actual individuo con la altura maxima anteriormente inputada
    alturamax = Altura #Si la informacion del "Si" o "If" es verdadera, procederan a cambiarse los valores siguientes
    nmax = Nombre
    amax = Apellido
    cmax = Cuit

print("La persona mas alta de la comision es:", nmax, " ", amax, " Cuit: ", cmax, "| Con una altura de: ", alturamax, " metros.")
#Y por ultimo se imprimen los valores totalmente correctos.
#Estefano Tesan.