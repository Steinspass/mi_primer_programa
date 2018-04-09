mi_lista = []

input_usuario= input("¿que nesesitas comprar?(escribe FIN para salir): ")

while input_usuario != "FIN":
    mi_lista.append(input_usuario)
    input_usuario = input("que nesesitas comprar?(escribe FIN para salir): ")
for item in mi_lista:
    print("Tengo que comprar {}".format(item))

print("esta es la lista de la comprar")