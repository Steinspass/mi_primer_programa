numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 15, 20, 35, 45, 55]

for indice in range (len(numeros)) :
    numero = numeros[indice]

    if numero % 3 == 0 or numero % 5 == 0:
        numeros[indice] = ""

        if numero % 3 == 0:
            numeros[indice] += "Fizz"

        if numero % 5 == 0:
            numeros[indice] += "Buzz"


print(numeros)