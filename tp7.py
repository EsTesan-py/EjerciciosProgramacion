inversion=float(input("Cantidad a invertir: "))
tasa=float(input("Interes anual: "))
años=int(input("Años: "))

print("Capital final: " + str(round(inversion * (tasa / 100 + 1) ** años, 2)))