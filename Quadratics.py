print("Escriba valores a,b y c de la funcion cuadratica")
a = float(input())
b = float(input())
c = float(input())

x1 = (-b)+(((b**2)-4*a*c)**0.5)/(2*a)
x2 = (-b)-(((b**2)-4*a*c)**0.5)/(2*a)

print("X1: ",x1)
print("x2: ",x2)