userReply = input("¿Necesita enviar un paquete? (Ingrese yes o no) ")

if userReply == "yes":
   print("Podemos ayudarlo a enviar ese paquete")
else:
    print("Por favor regrese cuando necesite enviar un paquete. Gracias.")
    
    
    
userReply2 = input("Would you like to buy stamps, buy an envelope, or make a copy? (Enter stamps, envelope, or copy) ")
if userReply2 == "stamps":
    print("We have many stamp designs to choose from.")
elif userReply2 == "envelope":
    print("We have many envelope sizes to choose from.")
elif userReply2 == "copy":
    copies = input("How many copies would you like? (Enter a number) ")
    print("Here are {} copies.".format(copies))
else:
    print("Thank you, please come again.")