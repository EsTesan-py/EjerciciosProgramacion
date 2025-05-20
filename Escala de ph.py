print("Nivel de ph")
quimico = float(input())
if quimico<=14 and quimico>=1:
 if quimico>7:
     print("Basico")
 elif quimico<7:
     print("Acido")
 else:
     print("Neutral")
else:
    print("wtf")