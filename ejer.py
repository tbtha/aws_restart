#ejercicio hollman 3
#Escribir un codigo que pregunte al usuario por el número de horas de trabajo y el costo por hora, despues debe mostrar por pantalla
#la paga correspondiente

nHoras = input("Ingrese el numero de horas de trabajo: ")
costoHora = input("Ingrese el costo por hora de trabajo: ")

#print(" la paga correspondiente es: ", int(nHoras) * int(costoHora))


#Escribir un codigo que pida al usuario dos números enteros y muestre por pantalla "la división entre <n> y <m> da un cociente <c>
#y un resto <r>" donde n y m son los enteros dados por el usuario y cyr son el cociente y el resto de la division entera


int1 = int(input("Ingrese un numero entero: "))
int2 = int(input("Ingrese otro numero entero: "))

#print("la división entre {} y {} da un cociente {} y un resto {} " .format(int1,int2, int1// int2, int1%int2 ))


#ejercicio 4 holman

#Escribir un programa que pregunte al usuario los números ganadores de la lotería, los almacene en una lista y 
#los muestre por pantalla ordenados de menor a mayor.


loteria = []

loteria.append( int(input("Ingrese los numeros ganadores de la loteria: ")))
loteria.append( int(input("Ingrese los numeros ganadores de la loteria: ")))
loteria.append( int(input("Ingrese los numeros ganadores de la loteria: ")))
loteria.append( int(input("Ingrese los numeros ganadores de la loteria: ")))

loteria.sort()
#print(loteria)
loteria.sort(reverse=True)
#print(loteria)

#ejercicio6
#Escribir un programa que guarde en una variable el diccionario {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}, pregunte al usuario por una divisa y 
#muestre su símbolo o un mensaje de aviso si la divisa no está en el diccionario.



divisas = {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}

user = input("Ingrese el nombre de una divisa")








