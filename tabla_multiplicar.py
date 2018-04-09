numero_tabla= int(input("de que numero quieres la tabla ded multiplicar: "))

for multiplo in range(5, 16):
    print("{} x {}= {}".format(numero_tabla, multiplo, numero_tabla * multiplo))