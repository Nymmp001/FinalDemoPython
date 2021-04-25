n=int(input("Introduce el numero de renglones del triángulo "))

if n <= 8:
    for i in range(n+1):
        espacio=n-i
        print(' '*espacio+'#'*i)
else:

    print("El numero ingresado no es correcto. ")
    n=int(input("Introduce nuevamente el numero: "))
 

    

