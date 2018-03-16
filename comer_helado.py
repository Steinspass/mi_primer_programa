
apetece_helado_input = input("¿apetece un helado? (si/no)")
tienes_dinero_para_el_helado_input= input("tienes dinero para un helado? (si/no)")
esta_el_senor_de_los_helados = input("¿esta el senor de los helado? (si/no)")
esta_tu_tia_input = input ("¿estas con tu tia?")

apetece_helado = apetece_helado_input == "si"
puedes_permitirtelo = tienes_dinero_para_el_helado == "si" or esta_tu_tia_input == "si"
esta_el_senor_de_los_helados =esta_el_senor_de_los_helados == "si"
if apetece__helado and puedes_permitirtelo and esta_el_senor_de_los_helados :
    print("pues comete un helado")
else:
    print("pues nada")
