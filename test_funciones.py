def input_con_confirmacion (pregunta):
    confirmacion = False
    dato_usuario = ""
    while not confirmacion :
        dato_usuario = input(pregunta)
        seguro = input("has dicho {} , Estas seguro? [Si/No]: ".format(dato_usuario))
        if seguro == "Si":
            confirmacion = True
    return dato_usuario
