# Este codigo ha sido generado por el modulo psexport 20180802-w32 de PSeInt.
# Es posible que el codigo generado no sea completamente correcto. Si encuentra
# errores por favor reportelos en el foro (http://pseint.sourceforge.net).


if __name__ == '__main__':
	# estas lineas representan la definicion de las variables que se utilizaran en el seudocodigo.
	# variable es un espacio en la memoria donde se almacena un dato el cual debe pertenecer a un tipo de dato.
	dni = int()
	dnimayor = int()
	cantidadpersonas = int()
	i = int()
	altura = float()
	alturamayor = float()
	apellido = str()
	nombre = str()
	apellidomayor = str()
	nombremayor = str()
	alturamayor = 0
	# entrada de datos para obtener el resultado deseado.
	print("porfavor ingresas cuantas personas hay en la comision")
	cantidadpersonas = int(input())
	# Utilizamos el "para" como estructura de control repetitiva, nos permiten ejecutar varias líneas de código 
	for i in range(1,cantidadpersonas+1):
		print(" señor usuario ingrese su dni")
		dni = int(input())
		print(" señor usuario ingrese su nombre")
		nombre = input()
		print(" señor usuario ingrese su apellido")
		apellido = input()
		print(" señor usuario ingrese su altura")
		altura = float(input())
		# proceso de los datos para obtener el resultado.
		if alturamayor<=altura:
			alturamayor = altura
			dnimayor = dni
			nombremayor = nombre
			apellidomayor = apellido
	# Y terminamos con el "escribir" que nos sirve para mostrar en pantalla un valor
	print("El mas alto de la comisión es ",nombremayor," ",apellidomayor," ",dnimayor," cuya altura es ",alturamayor," metros ")
