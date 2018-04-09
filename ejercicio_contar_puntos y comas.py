texto_usuario=("Hola, me llamo Nate.¿Tu como te llamas?")

comas = (",")
punto = (".")
espacio = (" ")

n_comas = 0
n_punto = 0
n_espacio = 0

for item in texto_usuario:
    if item in comas:
        n_comas += 1
    elif item in punto:
        n_punto += 1
    elif item in espacio:
        n_espacio += 1

print("las comas son {}".format(n_comas))
print("las punto son {}".format(n_punto))
print("las espacio son {}".format(n_espacio))
print("ha acabado")