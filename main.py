from Calculadora import Calculadora

#Utilizar la clase Calculadora
n1=int(input("Ingrese el primer numero: "))
n2=int(input("Ingrese el segundo numero: "))
calculadora = Calculadora(n1,n2)

#Llamar al metodo sumar
print(calculadora.sumar())

