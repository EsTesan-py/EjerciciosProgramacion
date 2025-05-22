confirmador=True

while confirmador==True:
        operador=str(input())
        configual=True
        for i in range(len(operador)):
                if operador[i]==">":
                        if i + 1 < len(operador) and operador[i + 1] == "=":
                            print("Operador relacional, mayor o igual que")
                        else:
                            print("Operador relacional, mayor que")
                        configual=False
                if operador[i]=="<":
                        if i + 1 < len(operador) and operador[i + 1] == "=":
                            print("Operador relacional, menor o igual que")
                        else:
                            print("Operador relacional, menor que")
                        configual=False
                if configual==True:
                    if operador[i]=="=":
                            print("Operador relacional, igual que")
        print("¿Repetir proceso?")
        respuesta=str(input())
        if respuesta=="si":
            confirmador=True
        elif respuesta=="no":
            confirmador==False
print("Fuera del while")
        


