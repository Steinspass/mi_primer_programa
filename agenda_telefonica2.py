salida = False
agenda = dict()

while not salida:
    accion = input("¿Que quieres hacer ? [añadir numero[A] / [consultar numero[C] / [salir[S]: ")

    if accion == "A":
        print("vamos a añadir un numero de telefono: ")
        print("--------------------------------------")
        nombre =input("Nombre:")
        numero = input("Numero:")
        agenda[nombre]= numero
    elif accion == "C":
        print("consultar numero:")
        print("--------------------------------------")
        nombre = input("de quien quieres el numero:")
        print(agenda[nombre])



    elif accion == "S":
        salida =True