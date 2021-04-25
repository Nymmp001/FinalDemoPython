def validcard(N):
    T=""; par=0; impar=0;X=""
    if not N.isdigit():return 1,""
    if len(N)<14 or len(N)>19:return 2,""

    for c in range (0,len(N),2):
            X=str(int(N[c])*2)
            if len(X)==2:
                par+=(int(X[0])+int(X[1]))
            else:par+=int(X)
    for c in range(1,len(N),2):
            impar+=int(N[c])
    if (par+impar)%10!=0:return 3,""
    if int(N[0:2])>49 and int(N[0:2])<56:T="**MASTERCARD"
    if N[0:2]=="34" or N[0:2]=="37":T="**AMEX"
    if N[0]=="4":T="**VISA"

    return 4,T

msg=(0,"")

while msg[0]!=4:
    msg=validcard(input("Ingresa el numero de la tarjeta de credito 13-19: "))
    if msg[0]==1:print("solo numeros del 0 al 9")
    if msg[0]==2:print("Deben ser mayor a 13 o más y menor o igual de 19 digitos")
    if msg[0]==3:print("Número de tarjeta inválida")

print("Tarjeta Válida!!")
print("Tipo:"+msg[1])
