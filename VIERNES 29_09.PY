print("Ingrese su nombre de usuario.")
user=str(input())
print("Ingrese su correo electronico.")
email=str(input())
mailval=False
while mailval==False:
    for i in email:
        if i =="@":
         mailval=True
    if mailval==False:
       print("Por favor, ingrese un correo electrónico válido.")
       email=str(input())
print("Ingrese una contraseña.")
print("Condiciones mínimas: 1 mayúscula, 1 número y 1 caractér de los siguientes:")
print("Caractéres disponibles: |!#$%&/()=?¡¿'*")

psw=str(input())
while True:
    mayuscula=any(caracter.isupper() for caracter in psw)
    numero=any(caracter.isdigit() for caracter in psw)
    especial=any(caracter in "|!#$%&/()=?¡¿'*" for caracter in psw)
    if mayuscula and numero and especial:
        print("Contraseña válida.")
        break
    else:
        print("La contraseña no cumple con los requisitos. Debe contener al menos una mayúscula, un número y un carácter especial.")
        psw=input("Intente de nuevo: ")

print("Seleccione una pregunta de las siguientes:")
print("1) ¿Nombre de su madre?")
print("2) ¿Nombre de su primera mascota?")
print("3) ¿Fecha de cumpleaños de un amigo?")
print("4) ¿Pelicula favorita?")
print("5) ¿Comida favorita?")

eleccion=(int(input()))
if eleccion==1:
    pregunta="¿Nombre de su madre?"
    print("Responda la pregunta.")
    respuesta=str((input()))
elif eleccion==2:
    pregunta="¿Nombre de su primera mascota?"
    print("Responda la pregunta.")
    respuesta=str((input()))
elif eleccion==3:
    pregunta="¿Fecha de cumpleaños de un amigo?"
    print("Responda la pregunta.")
    respuesta=str((input()))
elif eleccion==4:
    pregunta="¿Pelicula favorita?"
    print("Responda la pregunta.")
    respuesta=str((input()))
elif eleccion==5:
    pregunta="¿Comida favorita?"
    print("Responda la pregunta.")
    respuesta=str((input()))

print("Datos almacenados.")
print("¿Desea aportar correos electrónicos o números telefónicos de confianza?")
print("1) Deseo aportar numeros telefonicos de confianza.")
print("2) Deseo aportar correos electronicos de confianza.")
print("3) No.")
dataextra=int(input())
telefono=False
correoelectronico=False
if dataextra==1:
    telefono=True
    print("Escriba los numeros de telefono que usted desee aportar bajo su confianza.")
    print("Deben ser 2.")
    print("Numero 1: ")
    num=str(input())
    print("Numero 2: ")
    num2=str(input())
    print("Por favor, confirme los numeros.")
    print("Numero 1: ")
    numu=str(input())
    print("NUmero 2: ")
    numu2=str(input())
    while num!=numu and num2!=numu2:
        print("Uno de los numeros no coincide, vuelva a reescribirlos correctamente.")
        print("Numero 1: ")
        numu=str(input())
        print("Numero 2: ")
        numu2=str(input())
elif dataextra==2:
    correoelectronico=True
    print("Escriba los correos electronicos que usted desee aportar bajo su confianza.")
    print("Deben ser 2.")
    print("Correo 1: ")
    correo=str(input())
    print("Correo 2: ")
    correo2=str(input())
    print("Por favor, confirme los correos.")
    print("Correo 1: ")
    correu=str(input())
    print("Correo 2: ")
    correu2=str(input())
    while correo!=correu and correo2!=correu2:
        print("Uno de los correos no coincide, vuelva a reescribirlos correctamente.")
        print("Correo 1: ")
        correu=str(input())
        print("Correo 2: ")
        correu2=str(input())
menu=True
while menu==True:
    print("Menu principal")
    print("1) Verificar datos.")
    print("2) Modificar datos.")
    print("3) Salir del programa.")
    menueleccion=int(input())
    if menueleccion==1:
        print("Nombre de usuario: ",user)
        print("Correo electronico: ",email)
        print("Contraseña: ",psw)
        print("Pregunta de verificacion y su respuesta:")
        print(pregunta," - ",respuesta)
        if telefono==True:
            print("Numeros de confianza: ")
            print("1: ",num)
            print("2: ",num2)
        elif correoelectronico==True:
            print("Correos de confianza: ")
            print("Correo 1: ",correo)
            print("Correo 2: ",correo2)
    elif menueleccion==2:
        print("¿Que datos desea modificar?")
        print("1) Contraseña.")
        print("2) Nombre de usuario.")
        print("3) Pregunta de verificacion.")
        if telefono==True:
            print("4) Numeros de telefono de confianza.")
        elif correoelectronico==True:
            print("4) Correos electronicos de confianza.")
        electario=int(input())
        if electario==1:
            pswcomparador=str(input("Ingresar contraseña vieja: "))
            if pswcomparador==psw:
                newpsw=str(input("Escribir nueva contraseña: "))
                while newpsw==psw:
                    newpsw=input("Coloque una contraseña distinta a la antigua: ")
                while True:
                    mayuscula=any(caracter.isupper() for caracter in newpsw)
                    numero=any(caracter.isdigit() for caracter in newpsw)
                    especial=any(caracter in "|!#$%&/()=?¡¿'*" for caracter in newpsw)
                    if mayuscula and numero and especial:
                        print("Contraseña reemplazada.")
                        psw=newpsw
                        break
                    else:
                        print("La contraseña no cumple con los requisitos. Debe contener al menos una mayúscula, un número y un carácter especial.")
                        newpsw=input("Intente de nuevo: ") 
        if electario==2:
            confirmador=str(input("Su contraseña: "))
            if confirmador==psw:
                newuser=str(input("Escriba un nuevo nombre de usuario: "))
                while newuser==user:
                    newuser=input("Coloque un nombre de usuario diferente al que desea cambiar: ")
                print("Nombre de usuario cambiado con éxito.")
                user=newuser
            elif confirmador!=psw:
                print("Contraseña no coincide.")
        if electario==3:
            pswcomparador=input("Contraseña: ")
            if pswcomparador==psw:
                    print("Confirme cual era su pregunta.")
                    print("1) ¿Nombre de su madre?")
                    print("2) ¿Nombre de su primera mascota?")
                    print("3) ¿Fecha de cumpleaños de un amigo?")
                    print("4) ¿Pelicula favorita?")
                    print("5) ¿Comida favorita?")
                    eleccion2=int(input())
                    if eleccion==eleccion2:
                        print("Responda la pregunta.")
                        respuesta_confirmador=str(input())
                        if respuesta==respuesta_confirmador:
                            print("Perfecto ¿Por cual pregunta desea cambiar la antigua?")
                            print("1) ¿Nombre de su madre?")
                            print("2) ¿Nombre de su primera mascota?")
                            print("3) ¿Fecha de cumpleaños de un amigo?")
                            print("4) ¿Pelicula favorita?")
                            print("5) ¿Comida favorita?")
                            eleccion=input()
                            if eleccion==1:
                                pregunta="¿Nombre de su madre?"
                                print("Responda la pregunta.")
                                respuesta=str((input()))
                            elif eleccion==2:
                                pregunta="¿Nombre de su primera mascota?"
                                print("Responda la pregunta.")
                                respuesta=str((input()))
                            elif eleccion==3:
                                pregunta="¿Fecha de cumpleaños de un amigo?"
                                print("Responda la pregunta.")
                                respuesta=str((input()))
                            elif eleccion==4:
                                pregunta="¿Pelicula favorita?"
                                print("Responda la pregunta.")
                                respuesta=str((input()))
                            elif eleccion==5:
                                pregunta="¿Comida favorita?"
                                print("Responda la pregunta.")
                                respuesta=str((input()))
                            print("Pregunta y respuesta de seguridad cambiadas.")
                        else:
                            print("Respuesta incorrecta.")
                    elif eleccion2!=eleccion:
                        print("Incorrecto.")
        if electario==4:
            if telefono==True:
                pswcomparador=input("Contraseña: ")
                if psw==pswcomparador:
                    print("Numero 1: ",num)
                    print("Numero 2: ",num2)
                    eleccion_telefono=int(input("¿Cual numero desea reemplazar? : "))
                    if eleccion_telefono==1:
                        numu=input("Ingrese un nuevo numero de telefono: ")
                        while numu==num:
                            numu=input("Ingrese un numero distinto al que desea cambiar: ")
                        numu_conf=int(input("Confirme el numero reescribiendolo: "))
                        if numu_conf!=numu:
                            print("No coinciden.")
                        elif numu_conf==numu:
                            num=numu
                    elif eleccion_telefono==2:
                        numu2=input("Ingrese un nuevo numero de telefono: ")
                        while numu2==num2:
                            numu2=input("Ingrese un numero distinto al que desea cambiar: ")
                            numu2_conf=int(input("Confirme el numero reescribiendolo: "))
                        if numu2_conf!=numu2:
                            print("No coinciden.")
                        elif numu2_conf==numu2:
                            num2=numu2
                        print("Numero cambiado correctamente.")
                print("Contraseña incorrecta.")
            elif correoelectronico==True:
                pswcomparador=input("Contraseña: ")
                if psw==pswcomparador:
                    print("Correo 1: ",num)
                    print("Correo 2: ",num2)
                    eleccion_correo=int(input("¿Cual correo desea reemplazar? : "))
                    if eleccion_correo==1:
                        correu=input("Ingrese un nuevo correo electronico: ")
                        while correu==correo:
                            correu=input("Ingrese un correo electronico distinto al que desea cambiar: ")
                        correu_conf=int(input("Confirme el correo electronico reescribiendolo: "))
                        if correu_conf!=correu:
                            print("No coinciden.")
                        elif correu_conf==correu:
                            correo=correu
                    elif eleccion_correo==2:
                        correu2=input("Ingrese un nuevo correo electronico: ")
                        while correu2==correo2:
                            correu2=input("Ingrese un correo electronico distinto al que desea cambiar: ")
                            correu2_conf=int(input("Confirme el correo electronico reescribiendolo: "))
                        if correu2_conf!=correu2:
                            print("No coinciden.")
                        elif correu2_conf==correu2:
                            correo2=correu2
                        print("Correo cambiado correctamente.")
                elif psw!=pswcomparador:
                    print("Contraseña incorrecta.")
    elif menueleccion==3:
        menu=False





       

        
        


