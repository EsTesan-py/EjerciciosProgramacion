River = 0
Boca = 0
Talleres = 0
Belgrano = 0

print("Q1:¿Color de piel?")
print("1:Negro")
print("2:Blanquito")
print("3:Fideomoñito")
print("4:Colorado")
R1 = int(input())
print("Q2:¿Peso?")
print("1:+100kg")
print("2:+70kg")
print("3:ysiihijo")
print("4:+40kg")
R2 = int(input())
print("Q3:¿Orientacion Sexual?")
print("1:Puto")
print("2:Normal")
print("3:taiereeee")
print("4:Pan")
R3 = int(input())
if R1==1:
    Boca= Boca+1
elif R1==2:
    River= River+1
elif R1==3:
    Talleres=Talleres+1
elif R1==4:
    Belgrano=Belgrano+1

if R2==1:
    Boca=Boca+1
elif R2==2:
    River=River+1
elif R2==3:
    Talleres=Talleres+1
elif R2==4:
    Belgrano=Belgrano+1

if R3==1:
    Boca=Boca+1
elif R3==2:
    River=River+1
elif R3==3:
    Talleres=Talleres+1
elif R3==4:
    Belgrano=Belgrano+1

if River>Boca and River>Talleres and River>Belgrano:
    print("De River pa")

if Boca>River and Boca>Talleres and Boca>Belgrano:
    print("De Boca pa")

if Talleres>Boca and Talleres>River and Talleres>Belgrano:
    print("De Talleres pa")
    
if Belgrano>Boca and Belgrano>Talleres and Belgrano>River:
    print("De Belgrano pa")