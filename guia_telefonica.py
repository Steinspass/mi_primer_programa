salida = False
agenda = []

while not salida:
    accion = input("¿Que quieres hacer ? [añadir numero[A] / [consultar numero[C] / [salir[S]: ")

    if accion == "A":
        print("vamos a añadir un numero de telefono: ")
        print("--------------------------------------")
        nombre =input("Nombre:")
        numero = input("Numero:")
        agenda.append([nombre, numero])
    elif accion == "C":
        print("consultar numero:")
        print("--------------------------------------")
        nombre = input("de quien quieres el numero:")
        for nombre_numero in agenda:
            if nombre_numero [0] == nombre:
                print(nombre_numero[1])


    elif accion == "S":
        salida =True