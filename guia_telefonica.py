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