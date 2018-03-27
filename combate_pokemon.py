pokemon_elegido= input ("¿Contra que pokemon quieres combatir?(squirtle / charmander /bulbasaur): ")

vida_pikachu = 100
vida_enemigo= 0

if pokemon_elegido == "squirtle":
    vida_enemigo = 90

if pokemon_elegido == "charmander":
    vida_enemigo = 80

if pokemon_elegido == "bulbasaur":
    vida_enemigo = 100


while vida_pikachu > 0 and vida_enemigo > 0:
    ataque_elegido = input ("¿que ataque vamos a usar?(chispazo / bola voltio):")
    if ataque_elegido =="chispazo" :
        vida_enemigo -= 10
    if ataque_elegido =="bola voltio":
        vida_enemigo -= 12

    print("la vida del enemigo es de {} ".format (vida_enemigo))

    if pokemon_elegido == "squirtle":
        print("squirtle te hace un ataque de 8 de dano")
        vida_pikachu -= 8

    if pokemon_elegido == "charmander":
        print("charmander te hace un ataque de 7 de dano")
        vida_pikachu -= 7

    if pokemon_elegido == "bulbasaur":
        print("bulbasaur te hace un ataque de 10 de dano")
        vida_pikachu -= 10

    print("tu vida de pikachu es de {} ".format(vida_pikachu))

print ("el combate ha terminado")
