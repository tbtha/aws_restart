# APUNTES

## IDE
#### Entorno de desarrollo integrado / Integrated Development Environment
#### Es una aplicación informática (Software) que proporciona servicios integrales para facilitarle al desarrollador o programador el desarrollo de software  
#### IDE de AWS  es Cloud9
_____
### Estandar PEP8 (flake8) -> valida que el codigo este bien escrito
~~~
La barra diagonal invertida final (\) en el valor de la variable del paso anterior se utiliza para mantener el cumplimiento de la guía de estilo Propuestas de Mejora de Python (PEP) 
~~~
_____
___        ______     ____ _                 _  ___  
        / \ \      / / ___|   / ___| | ___  _   _  __| |/ _ \ 
       / _ \ \ /\ / /\___ \  | |   | |/ _ \| | | |/ _` | (_) |
      / ___ \ V  V /  ___) | | |___| | (_) | |_| | (_| |\__, |
     /_/   \_\_/\_/  |____/   \____|_|\___/ \__,_|\__,_|  /_/ 
 ----------------------------------------------------------------- 

## Tipos de datos
##### type() identifica que tipo de datos es la variable
~~~
 numerico 
        entero INT (200/-20)
        flotante FLOAT (1.4/-1.9)
        complejo COMPLEX (1+ 1j)
booleano BOOL              -> IsEmpty = True (buena practica Is...)
        True/False
Cadena de texto            -> son inmutables, cuando se manipula no se modifica, se crea una nueva cadena 
        sting STR        
~~~

~~~
·· Lista LIST                -> 
        myFrutList = ["apple", "banana"]
        print(myFrutList[0]) #imprime el dato de la posicion 0, en este caso -> apple 
                ** append() para agregar un nuevo valor a la lista

·· Tupla TUPLE                -> inmutable, no se puede cambiar despues de su creacion 
        color = ("red","green","blue")
        
·· Diccionario DICT             -> conformados por una clave/key y un valor
        myFavorite = {
                "Juan": "Apple",
                "Marta" : "Banana"
                }
                ** para añadir:
                        myFavorite["Paula"] = "cherry"
                        myFavorite["Creator"] = ["creator2","creato1"]

**para ordenar loteria.sort() / loteria.sort(reverse=true)
~~~

## Conversion/parseado/casteado de datos 
~~~
de string a numero float() int()
de numero a string str()
~~~

## Funciones integradas/nativas
#### Una funcion le indica a la computadora que realice una tarea especifica 
~~~
/ type() nos permite reconocer que tipo de datos es 

/ print() 
        print("Hola mundo")

/ input() nos permite recibir una entrada por parte de un usuario (siempre ingresan como cadena de texto)
        input("Ingresa un numero")
   
/ .format() / f' nos permite devolver variables en string
        name = "Roberto"
        print("Hola {}, como estas?" .format(name))
        print(f'"Hola {name}, como estas?")
   
/ .len() devuelve la longitud de la variable 
        ejemplo = "abcdefghijk"
        print(len(ejemplo))
        print(ejemplo[0:3]) -> devuelve porcion de la variable
        
/ .capitalize() convierte el primer carácter de una cadena en una letra mayúscula y todos los demás alfabetos en minúsculas

/ .upper() convierte todas las minusculas a mayusculas

/ .count() para ir contando catidades de  ...
/  sum()  suma los valores 

/ range(10,14) da una numero menos el 14

/ .values()  obtener valores de un diccionario
/ .keys() obtener claves de un diccionario

/ .split() divide toda una variable de tipo texto, quiero que la variable se divida cada ves que encuntres un guion (-) o cualquier caracter que queramos 
        ejemplo = "pera-mañana-platano-piña"
        print(ejemplo.split("-") #devuelve una lista con esos datos : ["pera","mañana","platano","piña"]

/ .strip() elimina los espacios al comienzo y al final del archivo
        ejemplo= "          estos es una cadena    "
        print(ejemplo.strip()) #devuelve "estos es una cadena"

/ .replace() reemplaza una palabra con otra
        origen = "Esto es una cadena"
        print(origen.replace("una", "otra")) # imprime "Esto es otra cadena"
~~~
## Funciones creadas 
#### namefunction() -> forma de invocar una funcion 
~~~
SINTAXIS        
        def sumar_uno(x):
        return x + 1            -> return devuelve algo de la funcion 
        
        resultado = sumar_uno(5)
        print(resultado) #imprime 6 
~~~

## Condicionales 
~~~
·· IF ELIF ELS
        numero1 = 5
        numero2 = 7
        if numero1 > numero2:
                print("n1 es mayor que n2")
        elif numero1 = 0:
                print(n1 es igual a 0"=
        else:
                print("n2 es mayor que n1")
                
··FOR           -> for i in lista (i por cada valor en lista)
        frutas = ["manzana","pera","uva"]
        for fruta in frutas:
                print("la fruta es:" , fruta)
~~~
## List comprehension             
#### sintaxis newList = [expresion for item in items if condition=True]
#### algo que se va a iterar y una condicion que se va a cumplir / tercer argumento es opcinal ?

~~~
        #manera original
frutas = ["manzanaa","kiwi","piña","mango"]
nuevaLista = []
for fruta in frutas:
        if "a" in fruta:
                nuevaLista.append(fruta)

        #list comprehension    
nuevaLista2 = [fruta for fruta in frutas if "a" in fruta]  
~~~

~~~

## Import
~~~ 

·· importar archivos (permite trabajar con otros archivo )
        with open ("filesname.txt") as archivonuevo
        data = archivonuevo.read()
        
·· importar funciones de otros archivos
       opc1
                 import operaciones 
                 resultado = operaciones.sumar(5)
       opc2
                 from operaciones import sumar,restar
                 reusltado = sumar(5)
                 
·· import random
        random.ranont(1,10) #devuelve un numero randon del 1 al 10 
        
·· import re 
        # sub() sirve para reemplazar las ocurrencias de un patrón en una cadena (como otra opcion tambien tenemos replace())
        # 1er argumento: patrón
        # 2do argumento: valor por el que voy a remplazar las ocurrencias
        # 3er argumento: cadena sobre la cual haré la búsqueda
        
        origen = "Esto es una cadena"
        pattern = r's'  (la r' respresenta que lo siguiente sera un patron para buscar)
        resultado = re.sub(pattern, 'f', origen)
        print(resultado) #imprime efto ef una cadena
        
        pattern2= r'[as]' (para buscar coincidenias de patrones de mas letras)
        pattern3= r'cadena' (busca la palabra completa)
~~~

