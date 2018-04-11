lista_mixta=["hacer", 23, "comer", 45, "berserker", 12, "auriculares"]


lista_de_numero=[int]
lista_de_palabras =[str]

for numero in lista_mixta:
    lista_de_numero.append(type(numero))

print(lista_de_numero)

for palabra in lista_mixta:
    lista_de_palabras.append( type(palabra))

print(lista_de_palabras)