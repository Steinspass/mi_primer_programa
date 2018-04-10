lista_de_datos= [1, 2, 4, "asd", False, [], True, 23, 2.1]
lista_de_tipos= []

for datos in lista_de_datos:
    lista_de_tipos.append(type(datos))

print(lista_de_tipos)