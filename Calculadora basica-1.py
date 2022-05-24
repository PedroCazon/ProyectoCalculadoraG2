
print ("/---------------------------------------------------------\\") 
print ("|                                                          |") 
print ("|                                                          |") #Dibujito bien
print ("|                   Calculadora basica                     |") 
print ("|                                                          |") #Fachero
print ("|                                                          |") 
print ("\----------------------------------------------------------/") 

opciones = float(input("Menu\n1. Suma.\n2. Resta.\n3. Multiplicar.\n4. Dividir.\n5. Potencia.\n6. Raiz Cuadrada. \n-.Cual vas a elegir?: "))
#Se le da a elegir la operacion al usuario

if (opciones == 1): #Se selecciona la opcion que fue indicada anteriormente
    n1 = float(input('Ingrese el primer numero: ')) #Se pide un numero para hacer la suma
    n2 = float(input('Ingrese el segundo numero: ')) ##Se pide un segundo numero para completar la suma
    print(str( n1 + n2)) #Se muestra en pantalla el resultado de la ecuacion

elif (opciones == 2): #Se selecciona la opcion que fue indicada anteriormente
    n1 = float(input('Ingrese el primer numero: ')) #
    n2 = float(input('Ingrese el segundo numero: '))
    print(str( n1 - n2)) #Se muestra en pantalla el resultado de la ecuacion

elif (opciones ==3): #Se selecciona la opcion que fue indicada anteriormente
    n1 = float(input('Ingrese el numero a multiplicar: ')) #Se pide un numero a multiplicar
    n2 = float(input('Ingrese el multiplicador: ')) #Se pide un numero para multiplicar el otro numero
    print(str( n1 * n2)) #Se muestra en pantalla el resultado de la ecuacion

elif (opciones == 4): #Se selecciona la opcion que fue indicada anteriormente
    n1 = float(input('Ingrese el numero que quiere dividir: ')) #Se pide un numero para divir
    n2 = float(input('Ingrese el numero con cual quiere dividir el primer numero: ')) #Se pide un numero para dividir 
    """
    En este caso al ser una calculadora simple/basica/sensilla no encontre una forma de hacerla sin que te salte un mensaje de 
    que no se puede dividir por 0 y si lo probamos vamos a ver que nos va a dar un error de codigo.
    Esto se solucionaria usando una funcion (def) y agregando esto:
                                                        if (num2 != 0):
                                                            return num1 / num2
                                                        elif (num2 ==0):
                                                            error = "No se puede efectuar operación"
                                                            return error
    """
    print(str( n1 / n2)) #Se muestra en pantalla el resultado de la ecuacion

elif (opciones == 5): #Se selecciona la opcion que fue indicada anteriormente
    n1 = float(input('Ingrese el numero al cual quiere potenciar: ')) #Se pide un numero al cual le vamos a elevar a una potencia elegida por el usuario
    n2 = float(input('Ingrese la potencia: ')) #Se pide una potencia 
    print(str(n1 ** n2)) #Se muestra en pantalla el resultado de la ecuacion

elif (opciones == 6): #Se selecciona la opcion que fue indicada anteriormente
    n1 = float(input('Ingrese el primer numero: ')) #Se pide un numero para hacer la ecuacion (Raiz Cuadrada)
    print(str((n1 ** (1/2)))) #Se muestra en pantalla el resultado de la ecuacion