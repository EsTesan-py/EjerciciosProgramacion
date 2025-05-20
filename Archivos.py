#ARCHIVOS PARTE 1
archivo = open("cliente.txt", "a+") #"archivo extension", "forma de abrirlo"
archivo2 = open("cliente.txt", "r") #abrimos solo lectura
variable = archivo2.readline() #leee la linea donde esta el puntero

if variable != "dni   apellido   nombre   legajo \n":
  archivo.write("dni   apellido   nombre   legajo \n") #nos imprime por pantalla, no en el archivo
archivo.close() #para que guarde los cambios efectuados

for i in range(3):
  dni = int(input("Ingrese su dni: "))
  apellido = str(input("Ingrese su apellido: "))
  nombre = str(input("Ingre su nombre: "))
  legajo = int(input("Ingrese su legajo: "))

  registro =(f"dni   {dni} apellido   {apellido} nombre   {nombre} legajo   {legajo}\n")

  archivo.write(registro) #introduce el dato en el archivo


#ARCHIVOS PARTE 2
#MOSTRAR TODY EL ARCHIVO.
archivo=open("localidades.txt","r")
print("LISTA DE LOCALIDADES")
print(archivo.read() )
#Imprimir el registro 1 de un archivo.
#Moviliza puntero a bit 0 y leer primera linea.
archivo.seek(0)#Metodo, mover el puntero a bit .
print(archivo.readline())
#Imprimir el registro 4 de un archivo
print("CUARTA LINEA DE CODIGO")
archivo.seek(0)
renglones=archivo.readlines()
print(renglones[3])
#Imprimir primer columna de archivo.
archivo.seek(0)
for i in archivo:
    campo=i.split(";")
    if len(campo)>=2:
        codigo_postal=campo[0].strip()
        print(codigo_postal)
#Imprimir un solo contenido de un campo
print("ARCHIVO CUALQUIERA")
archivo.seek(0)
bandera=int(0)
for i in archivo:
    campo=i.split(";")
    if campo[0]=="5186":
        bandera=1
if bandera==1:
    print("Existe el codigo postal")
     #print (campo[0])
else:
    print("El codigo no existe")