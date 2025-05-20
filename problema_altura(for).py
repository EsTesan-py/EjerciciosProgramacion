if __name__ == '__main__':
	# Saber quien, cuantos y que cantidad de estudiantes fueron evaluados para obtener, el alumno mas alto de la comision, segun la cantidad de personas que la componen, en forma quincenal, porque cada 15 dias se renuevan las becas.
	# estas lineas representan la definicion de las variables que se utilizan en el pseudocodigo
	# variable es un espacio en memoria donde se almacena un dato el cual debe pertenecer a un tipo de dato
	cantidad_personas = int()
	dni = int()
	dni_persona_mayor = int()
	i = int()
	altura = float()
	altura_maxima = float()
	nombre = str()
	apellido = str()
	nombre_persona_mayor = str()
	apellido_persona_mayor = str()
	# Entrada
	# Escribir permite mostrar valores por pantalla.
	print("Ingrese la cantidad total de personas en su comision: ")
	# Leer permite ingresar informacion desde el ambiente.
	cantidad_personas = int(input())
	# Toma N valores desde el ambiente por teclado y los asigna a la variable mencionada.
	# El Para ejecuta una secuencia de instrucciones un numero determinado de veces.
	for i in range(1,cantidad_personas+1):
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
		altura_maxima = 0
		dni_persona_mayor = 0
		# Esta secuencia de instrucciones depende del valor de una condicion logica.
		if altura_maxima<=altura:
			# Se evalua dicha condicion y se ejecutan las instrucciones que correspondan.
			altura_maxima = altura
			dni_persona_mayor = dni
			nombre_persona_mayor = nombre
			apellido_persona_mayor = apellido
	print("El mas alto de la comision es ",nombre_persona_mayor," ",apellido_persona_mayor," su numero de D.N.I. es: ",dni_persona_mayor," y su altura es ",altura_maxima," metros.")

