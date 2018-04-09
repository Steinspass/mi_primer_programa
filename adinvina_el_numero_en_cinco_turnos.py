number_to_guess = 6

intento=0

user_number = int(input("adivina el numero: ")

while intento<5:
    print("tienes cinco intentos prueba de nuevo")
    adivina= input()
    adivina= int(adivina)

    intento=intento+1

if number_to_guess<user_number
    print("vuelve a intentarlo tu numero es menor")

if number_to_guess>user_number
    print("vuelve a intentarlo tu numero es mayor")

if number_to_guess == user_number:
    print("Has Ganado")
