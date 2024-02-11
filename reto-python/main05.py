# Reto Python Día #5

"""
Listo, llegamos al reto número 5 de la semana. Nuestro programa ya funciona sumamente bien. Ya podemos crear, listar y editar usarios.

Sin embargo, muy probablemente el código que tengamos hasta ahora pueda mejorar significativamente, es por ello que, para el reto de hoy vamos a definir 5 nuevas funciones; esto con la finalidad de poder separar nuestro código y que este sea fácil de leer, comprender y sobre todo mantener.

Las 5 nuevas funciones serán las siguientes.

new_user

show_user

edit_user

delete_user

list_users

Las funciones, como bien sus nombre nos indican, nos permitirán seperar nuestra lógica para poder crear nuevos usuarios, consultarlos, editarlos, eliminarlos (Que es una nueva acción) y listarlos.

Con Excepción de list_users y new_user, cada una de estas funciones deberá recibir como parámetro el ID de usuario con el cual se desea trabajar.

Un pro Tip. Recuerda que las opciones puedas almacenarlas en como llaves en un diccionario y que, quizás, puedas almacenar las funciones en valores de esas llaves.
"""

import os

# Menu
# 1. Registrar un nuevo usuario
# 2. Ver información de un usuario
# 3. Editar Usuario
# 4. Eliminar Usuario
# 5. Listar Usuarios
# 6. Finalizar Programa
def menu_main():
    options = {
        '1' : ('Registrar un nuevo usuario', new_user),
        '2' : ('Ver información de un usuario', show_user),
        '3' : ('Editar información de un usuario', edit_user),
        '4' : ('Eliminar un Usuario', delete_user),
        '5' : ('Listar Usuarios', list_users),
        '6' : ('Finalizar Programa', exit)
    }

    generate_menu(options, '6')


def generate_menu(options, option_exit):
    option = None
    while option != option_exit:
        view_menu(options)
        option = read_option(options)
        clear()
        execute_option(option, options)
        print()


def view_menu(options):
    print("----------")
    print("BIENVENIDO")
    print("----------")
    print('📅 Seleccione una opción:')
    for key in sorted(options):
        print(f' {key}) {options[key][0]}')


def read_option(options):
    while (a := input('Opción: ')) not in options:
        print('⚠️ Opción incorrecta, vuelva a intentarlo.')
    return a


def execute_option(option, options):
    options[option][1]()


def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def new_user():
    first_name = request_str("Ingresa el nombre del usuario: ")
    last_name = request_str("Ingresa el apellido del usuario: ")
    phone_number = request_number("Ingresa el número de teléfono: ")
    email = input("Ingresa el correo electrónico: ")
    global auto_increment
    global users
    auto_increment += 1
    clear()
    print("✅ Usuario Registrado con exito con el ID:", auto_increment)
    id_users.append(auto_increment)
    message_confirm = "Hola " + first_name + " " + last_name + " en breve recibirás un correo a " + email
    print("    Mensaje de confirmación: [ ", message_confirm, " ]")
    
    user_dict = {
        'firts_name'    : first_name,
        'last_name'     : last_name,
        'phone_number'  : phone_number,
        'email'         : email
    }

    users.update({auto_increment: user_dict})

    input('    Preciona una tecla para continuar')
    clear()


def request_str(input_text):
    data = input(input_text)
    while len(data) < 5 or len(data) > 50:
        print("⚠️  El valor ingresado es invalido, debe tener entre 5 a 50 caracteres")
        data = input(input_text)
    return data


def request_number(input_text):
    data = input(input_text)
    while not is_validate_phone_number(data):
        data = input(input_text)
    return data


def is_validate_phone_number(phone_number):
    try:
        int(phone_number)
        if len(phone_number) > 0 and len(phone_number) <= 10:
            return True
        else:
            print("⚠️  El valor ingresado es invalido, el numero debe ser hasta 10 digitos.")
            return False
    except ValueError:
        print("⚠️  El valor ingresado es invalido, el numero debe ser solo numeros.")
        return False


def list_users():
    if len(users) > 0:
        print('✅ A continuación se listan los IDs de los Usuarios registrados')
        print("----")
        print(" ID ")
        print("----")
        for id_user in users.keys():
            print(id_user)
        print("----")
        print("")

    else:
        print('✅ No hay usuarios registrados en el sistema')

    input('Preciona una tecla para continuar')
    clear()


def show_user():
    try: 
        id = int(input('Ingrese el ID del usuario que desea consultar:'))
        if id in users:
            print_user(users[id])
        else:
            print(f'⚠️  El id {id} no esta registrado en la lista de usuarios.')    
        input('Preciona una tecla para continuar')
        clear()
    except ValueError:
        input("⚠️  Por favor, ingrese un número entero válido. Oprime una tecla para continuar.")


def edit_user():
    try: 
        id = int(input('Ingrese el ID del usuario que desea editar:'))
        if id in users:
            first_name = request_str("Ingresa tus nombres: ")
            last_name = request_str("Ingresa tus apellidos: ")
            phone_number = request_number("Ingresa tu numero de teléfono: ")
            email = input("Ingresa tu correo electrónico: ")
            print("✅ Usuario actualizado con exito con el ID:", id)
            user_dict = {
                'firts_name'    : first_name,
                'last_name'     : last_name,
                'phone_number'  : phone_number,
                'email'         : email
            }
            users.update({id: user_dict})
        else:
            print(f"⚠️  El ID: {id} no existe en el sistema")

        input("Oprime una tecla para continuar.")
        clear()    
    except ValueError:
        input("⚠️  Por favor, ingrese un número entero válido. Oprime una tecla para continuar.")


def delete_user():
    try: 
        id = int(input('Ingrese el ID del usuario que desea eliminar:'))
        if id in users:
            user_deleted = users.pop(id, None)
            if user_deleted != None:
                print("✅ Usuario eliminado con exito con el ID:", id)
            else:
                print("⚠️  El usuario no se encuentra en el sistema con el ID:", id)
        else:
            print("⚠️  El usuario no se encuentra en el sistema con el ID:", id)

        input("Oprime una tecla para continuar.")
            
    except ValueError:
        input("⚠️  Por favor, ingrese un número entero válido. Oprime una tecla para continuar.")

    clear()

    

def print_user(user):
    for id in user:
        print(f' {id} : {user[id]}')


def exit():
    print('Saliendo')


auto_increment = 0
id_users = []
users = {}

menu_main()
