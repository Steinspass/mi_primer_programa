frase_del_usuario= input("¿introduce una frase?: ")

vocales = ("a","e","u","i","o")

n_vocales = 0
n_consonates = 0

for letra in frase_del_usuario:
    if letra in vocales:
        n_vocales += 1
    else:
        n_consonates += 1

print("las vocales son {}".format(n_vocales))
print("las consonates son {}".format(n_consonates))