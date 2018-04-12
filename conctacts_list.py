ACTION_ADD_CONTACT= 1
ACTION_REMOVE_CONTACT=2
ACTION_FIND_CONTACT=3
ACTION_EXPORT_CONTACT=4
ACTION_EXIT=5

MENU_OPTIONS = [ACTION_ADD_CONTACT, ACTION_REMOVE_CONTACT, ACTION_FIND_CONTACT, ACTION_EXPORT_CONTACT, ACTION_EXIT]

def show_menu():
    print("acciones disponibles:")
    print("1-Añadir contacto ")
    print("2-Eliminar contacto")
    print("3-Buscar contacto")
    print("4- Exportar contactos a CSV")
    print("5- Salir")
    return

    selected_action = ""

    while not selected_action.isdigit() or (selected_action.isdigit() and int(selected_action)not in MENU_OPTIONS):
        selected_action = input(question)

    return int(selected_action)


def add_contact():
    pass

def remove_contact():
    pass

def find_contact():
    pass

def export_contact():
    pass



def main():
    action = show_menu()

    while action != ACTION_EXIT:
        if action == ACTION_ADD_CONTACT:
            add_contact()
        elif action == ACTION_REMOVE_CONTACT:
            remove_contact()
        elif action == ACTION_FIND_CONTACT:
            find_contact()
        elif action == ACTION_EXPORT_CONTACT:
            export_contact()

        action = show_menu()
