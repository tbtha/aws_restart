import random


print("Bienvenido a Adivina el Número!")
print("Las reglas son simples. Yo pensaré en un número y tú intentarás adivinarlo.")

number = random.randint(1,10)
isGuessRight = False

while isGuessRight != True: #Si el usuario no ha adivinado la respuesta correcta, ingrese el bucle.
    guess = input("Adivina un número entre 1 y 10: ") #Pida al usuario que adivine el número.
    if int(guess) == number: #¿Es el número correcto?
        print("Acertó {}. ¡Eso es correcto! ¡Tú ganas!".format(guess))#Si la respuesta es correcta, dígaselo al usuario y salga del bucle.
        isGuessRight = True
    else:
        print("No acerto {}. Lo siento, eso no es todo. Intentar otra vez.".format(guess)) # Si no ha adivinado el número, indique al usuario que fue una suposición incorrecta y continúe con el bucle.