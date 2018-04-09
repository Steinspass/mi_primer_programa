numeros_usuario = []
numero_del_usuario = ""

while len(numeros_usuario) < 10:
    while not numero_del_usuario.isdigit():
        numero_del_usuario = input("dime un numero: ")
    numeros_usuario.append(int(numero_del_usuario))
    numero_del_usuario=""
    print("¡Numero Añadido!")

numero_grande = numeros_usuario [0]

for numero in numeros_usuario:
    if numero >numero_grande:
        numero_grande= numero

print("el numero mas grande es {}".format(numero_grande))