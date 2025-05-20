if __name__ == '__main__':
	# estas lineas representan la definicion de las variables que se utilizan en el pseudocodigo
	# variable es un espacio en memoria donde se almacena un dato el cual debe pertenecer a un tipo de dato
	dni = int()
	dni_persona_mayor = int()
	altura = float()
	altura_maxima = float()
	verificacion = float()
	nombre = str()
	apellido = str()
	nombre_persona_mayor = str()
	apellido_persona_mayor = str()
	altura_maxima = 0
	dni_persona_mayor = 0
	acum=0
	# Entrada
	print("¿Desea comenzar la carga de datos?")
	print("Ingrese por teclado uno de los siguientes valores:")
	print("(1): para la carga de datos")
	print("(cualquier otro numero): para finalizar")
	verificacion = float(input())
	if verificacion==1:
		# El Para ejecuta una secuencia de instrucciones un numero determinado de veces.
		while verificacion==1:
			print("Ingrese su D.N.I.: ")
			dni = int(input())
			print("Ingrese su nombre: ")
			nombre = input()
			print("Ingrese su apellido: ")
			apellido = input()
			print("Ingrese su altura: ")
			altura = float(input())
			acum=acum+1
			# Proceso
			# Asignacion o inicializacion de variables esta accion permite almacenar un valor en una variable.
			# Esta secuencia de instrucciones depende del valor de una condicion logica.
			if altura_maxima<=altura:
				# Se evalua dicha condicion y se ejecutan las instrucciones que correspondan.
				altura_maxima = altura
				dni_persona_mayor = dni
				nombre_persona_mayor = nombre
				apellido_persona_mayor = apellido
			print("Ingrese por teclado uno de los siguientes valores:")
			print("(1): para continuar la carga de datos")
			print("(cualquier otro numero): para finalizar la carga de datos")
			verificacion = float(input())
		print("El mas alto de la comision es ",nombre_persona_mayor," ",apellido_persona_mayor," su numero de D.N.I. es: ",dni_persona_mayor," y su altura es ",altura_maxima," metros.")
	else:
		print("No se registró la asistencia de ninguna persona")
print("La cantidad de personas que se registraron fue de: ",acum," personas.")

