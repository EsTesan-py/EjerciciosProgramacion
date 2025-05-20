#Crear un money.py programa que le pide al usuario la cantidad que tiene en yuanes, yenes, y ganó y calcula el total en USD
Yuan = 0.14
Yen = 0.00074
Won = 0.00077
print("Cantidad de yuanes? ")
myuan = float(input())
print("Cantidad de yenes? ")
myen = float(input())
print("Cantidad de wones? ")
mwon = float(input())
Dolar = (Yuan*myuan)+(Yen*myen)+(Won*mwon)
print("Tu cantidad de dolares es: ",Dolar)