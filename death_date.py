import datetime
import random

#mejorar el programa con mas opciones de si ,no ,a veces . Añadir el random entre 40/80 y decir el dia exacto y evitar que la vida sea -1

AVERAGE_LIFESPAN = 80
SMOKER_PENALIZATION = 10
DRINKER_PENALIZATION = 10
SEDENTARY_PENALIZATION= 20

def print_with_underscores(message):
    print(message)
    print(len(message) * "-")

def ask_yes_or_not (message):
    response= None
    while response != "S" and response != "N":
        response = input( message + "[S/N]")
    return response == "S"

print_with_underscores("¿Averigua cuanto tiempo de vida te queda?")
print("completa esta encuesta para saber cuanto tiempo de vida te queda ")

birth_date = input("¿cual es tu fecha de nacimiento (formato: dd/mm/yyyy)? ")

birth_date = datetime.datetime.strptime(birth_date, "%d/%m/%Y")
year_lost = 0

if ask_yes_or_not("¿fumas?"):
    year_lost -= SMOKER_PENALIZATION

if ask_yes_or_not("¿bebes?"):
    year_lost -= DRINKER_PENALIZATION

if not ask_yes_or_not("¿haces deporte?"):
    year_lost -= SEDENTARY_PENALIZATION


lifespan = AVERAGE_LIFESPAN - year_lost
death_day = birth_date + datetime.timedelta(days=lifespan * 365)
days_to_death = death_day - datetime.datetime.now()

print("Fecha de tu muerte: {}, te quedan {}".format(death_day ,days_to_death))




