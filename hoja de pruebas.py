#Utilizo la funcion de find hecha manual
def Finder(xstr,fstr):
    A=int()
    pos=int(-1)
    while A<= (len(xstr)-len(fstr)):
        if xstr[A:(A+len(fstr))] == fstr:
            pos=A
            A=A+len(xstr)+1
        else:
            A=A+1
    return pos
#Utilizo la funcion de replace tambien hecha manual
def funcion_reem(istr,reemstr,sreem):
    ending = False
    while ending==False:
        if Finder(istr,reemstr)!= (-1):
            subreem = str(istr[0:Finder(istr,reemstr)])
            subreem = str(subreem + sreem) 
            subreem = str(subreem + istr[(Finder(istr,reemstr))+len(reemstr) : len(istr)+1])            
            istr = subreem
        else:
            subreem = istr
            ending = True
    return subreem
#Ya teniendo las funciones anteriores puedo continuar con la funcion requerida
def txtsms(sms):
    mercurio=funcion_reem(sms,"que","q")
    venus=funcion_reem(mercurio,"lo","l")
    marte=funcion_reem(venus,"de","d")
    jupi=funcion_reem(marte,"se","s")
    sat=funcion_reem(jupi,". ",".")
    uran=funcion_reem(sat,", ",",")
    return uran
msg=str(input())
word1=len(msg)
wordfinal=len(txtsms(msg))
output=word1-wordfinal
print("ans = ",txtsms(msg))
print("diferencia = ",output)


