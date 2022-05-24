def seleccionOperacion():
    
    print ("/--------------------------------------------------------------------\\")
    print ("|Nuestra calculadora permite desarrollar las siguientes operaciones:  |")
    print ("|                                                                     |")
    print ("|                            OPERACIONES                              |")
    print ("|                                                                     |")
    print ("|   1-> SUMAR                     2-> RESTAR                          |")
    print ("|   3-> MULTIPLICAR               4-> DIVIDIR                         |")
    print ("|   5-> POTENCIA                  6-> RAIZ CUADRADA                   |")
    print ("\---------------------------------------------------------------------/")
    


def suma(num1, num2):
    return num1 + num2

def multiplicacion(num1, num2):
    return num1 * num2

def resta(num1, num2):
    return num1 - num2

def division(num1, num2):
    if (num2 != 0):
        return num1 / num2
    elif (num2 ==0):
        error = "No se puede dividir por 0"
        return error
    
def potencia(num1, num2):
    return str(num1, num2)


def resultado():
    mensaje = print("El resultado de la operacion: ", operacion, "es") 
    return mensaje

def ingresoValores():
    val1 = float(input("Ingrese el primer valor: "))
    val2 = float(input("Ingrese un segundo valor: "))
    return 

seleccionOperacion()    
operacion = int(input("Elija el tipo de operación matemática a efectuar: "))



if operacion == 1 :
    #ingresoValores()
    val1 = float(input("Ingrese el primer numero: "))
    val2 = float(input("Ingrese el segundo numero: "))
    resultado = suma(val1,val2)
    print (resultado)
    
elif operacion == 2 :
    val1 = float(input("Ingrese el primer numero: "))
    val2 = float(input("Ingrese el segundo numero: "))
    resultado = resta(val1,val2)
    print (resultado)
    
elif operacion == 3 :
    val1 = float(input("Ingrese el numero a multiplicar: "))
    val2 = float(input("Ingrese el multiplicador: "))
    resultado = multiplicacion(val1,val2)
    print (resultado)
    
elif operacion == 4 :
    val1 = float(input("Ingrese el numero que quiere dividir: "))
    val2 = float(input("Ingrese el numero con cual quiere dividir el primer numero: "))
    resultado = division(val1,val2)
    print (resultado)
    
elif operacion == 5 :
    val1 = float(input("Ingrese el numero al cual quiere potenciar: "))
    val2 = float(input("Ingrese la potencia: "))
    print(str(val1 ** val2))

elif operacion == 6 :
    val1 = float(input("Ingrese el numero al cual quiere radicar: "))
    print(str((val1 ** (1/2))))
