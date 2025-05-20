with open("practica.txt","w") as archivo:
    archivo.write("Que onda la rotonda.")
    archivo.write(" O no? Rotondon")
    archivo.write("\n")
    archivo.write("Aca ya hay un bajon de lineaas.")

    lineas=["Juju primera linea\n","Juju segunda linea\n","JUJUU Tercera paa\n"]
    archivo.writelines(lineas)
with open("practica.txt","a") as archivo:
    archivo.write("Esto deberia agregarse al ultimo sin romper las pelotas.\n")
    archivo.write("Que ondificante.")
with open("practica.txt","r") as archivo:
    print(archivo.read())
    archivo.seek(0)
    lineas=(archivo.readlines())
    print(lineas[2])

with open("practica.txt","w+") as archivo:
    separados=lineas[0].split(".")
    print(separados)