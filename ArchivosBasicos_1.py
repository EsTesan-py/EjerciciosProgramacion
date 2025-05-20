with open("cliente.txt","w") as archivo:
    archivo.write("APELLIDO|NOMBRE|DNI|\n")
    
with open("cliente.txt","a") as archivo:
    for i in range(3):

        archivo.write(input("Coloque el apellido: "))
        archivo.write("|")
        archivo.write(input("Coloque su nombre: "))
        archivo.write("|")
        archivo.write(input("Coloque su DNI: "))
        archivo.write("|")
        archivo.write("\n")
        print("Contador de personas identificadas: ",i+1)
        