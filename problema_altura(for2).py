if __name__ == '__main__':
	# estas lineas representan la definicion de las variables que se utilizan en el pseudocodigo
	# variable es un espacio en memoria donde se almacena un dato el cual debe pertenecer a un tipo de dato
	verificacion = int()
	dni = int()
	dni_persona_mayor = int()
	i = int()
	altura = float()
	altura_maxima = float()
	nombre = str()
	apellido = str()
	nombre_persona_mayor = str()
	apellido_persona_mayor = str()
	verificacion = 1
	altura_maxima = 0
	dni_persona_mayor = 0
	# Entrada
	# Toma N valores desde el ambiente por teclado y los asigna a la variable mencionada.
	# El Para ejecuta una secuencia de instrucciones un numero determinado de veces.
	for i in range(1,verificacion+1):
		print("Ingrese su D.N.I.: ")
		dni = int(input())
		print("Ingrese su nombre: ")
		nombre = input()
		print("Ingrese su apellido: ")
		apellido = input()
		print("Ingrese su altura: ")
		altura = float(input())
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
		verificacion = int(input())
		if verificacion==1:
			i = i-1
	print("El mas alto de la comision es ",nombre_persona_mayor," ",apellido_persona_mayor," su numero de D.N.I. es: ",dni_persona_mayor," y su altura es ",altura_maxima," metros.")

