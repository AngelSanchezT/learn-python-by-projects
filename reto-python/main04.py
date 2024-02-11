# Reto Python Día #4

"""
Ya nos encontramos en la recta final de nuestra semana, y lo que haremos ahora, cómo ya es costumbre, será añadir más funcionalidades a nuestro programa.

Puntualmente 4 nuevas funcionalidades. Aquí van.

1.- Ahora todos los valores que representan a un usuario: Nombre, apellidos, número de teléfono y correo electrónico deberán almacenarse en un diccionario.

2.- Se añadirá la opción de poder listar el ID de todos los usuarios registrados hasta el momento.

3.- Se añadirá la opción de poder ver la información de un usuario con respecto a un ID. Es decir, el usuario podrá ingresar un ID y a partir de este conocer la información registrada.

4.- Se añadirá la opción de poder editar la información de un usuario con respecto a un ID. Es decir, el usuario podrá ingresar un ID y a partir de este el programa pedirá nuevamente los valores de un registro para actualizarlos.

Estas 3 nuevas opciones deberán ser presentadas al usuario al comienzo del programa, esto con la finalidad que sea el usuario quien defina que quiere hacer justo ahora: añadir nuevos usuario, consultarlos o editarlos.

De igual forma el programa tendrán una quinta opción que le permita la usuario finalizar el programa cuando él lo desee.

Un Tip. Para estas nuevas opciones puedes presentarle a tu usuario un pequeño menú del cual pueda elegir. Por ejemplo opción A.-) registrar nuevos usuarios, opción B.-) listar usuarios, Opción C.-) Editar usuarios y así sucesivamente.

"""

import os

# Menu
# 1. Registrar nuevos usuarios
# 2. Listar Usuarios
# 3. Ver información de un usuario
# 4.Editar Usuarios
# 5. Finalizar Programa
def menu_main():
    options = {
        '1' : ('Registrar nuevos usuarios', register_users),
        '2' : ('Listar Usuarios', list_user_id),
        '3' : ('Ver información de un usuario', view_user),
        '4' : ('Editar información de un usuario', edit_user),
        '5' : ('Finalizar Programa', exit)
    }

    generate_menu(options, '5')

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
    print('Seleccione una opción:')
    for key in sorted(options):
        print(f' {key}) {options[key][0]}')

def read_option(options):
    while (a := input('Option ')) not in options:
        print('Opción incorrecta, vuelva a intentarlo.')
    return a

def execute_option(option, options):
    options[option][1]()


def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def ask_number_of_users():
    while True:
        try:
            num_users = int(input("Ingrese el número de usuarios que desea registrar: "))
            if num_users > 0:
                return num_users
            else:
                print("Por favor, ingrese un número entero válido.")
        except ValueError:
            print("Por favor, ingrese un número entero válido.")

def register_user():
    first_name = request_str("Ingresa tus nombres: ")
    last_name = request_str("Ingresa tus apellidos: ")
    phone_number = request_number("Ingresa tu numero de teléfono: ")
    email = input("Ingresa tu correo electrónico: ")
    global auto_increment
    global id_users
    global users
    auto_increment += 1
    print("Usuario Registrado con exito con el ID:", auto_increment)
    id_users.append(auto_increment)
    message_confirm = "Hola " + first_name + " " + last_name + " en breve recibirás un correo a " + email
    print(message_confirm)

    user_dict = {
        'firts_name'    : first_name,
        'last_name'     : last_name,
        'phone_number'  : phone_number,
        'email'         : email
    }

    users.update({auto_increment: user_dict})

def request_str(input_text):
    data = input(input_text)
    while len(data) < 5 or len(data) > 50:
        print("El valor ingresado es invalido, debe tener entre 5 a 50 caracteres")
        data = input(input_text)
    return data

def request_number(input_text):
    data = input(input_text)
    while not is_validate_phone_number(data):
        data = input(input_text)
    return data

def is_validate_phone_number(phone_number):
    try:
        phone_number_int = int(phone_number)
        if len(phone_number) > 0 and len(phone_number) <= 10:
            return True
        else:
            print("El valor ingresado es invalido, el numero debe ser hasta 10 digitos.")
            return False
    except ValueError:
        print("El valor ingresado es invalido, el numero debe ser solo numeros.")
        return False
     
def register_users():
    global auto_increment
    global id_users
    global users

    auto_increment = 0
    id_users = []
    users = {}

    total_users = ask_number_of_users()
    index_user = 1
    while index_user <= total_users:
        clear()
        print("Inicio de Registro del Usuario: #" + str(index_user))
        register_user()
        index_user += 1
    print("----")
    print("Se registraron", len(id_users), "usuario(s) exitosamente.")

def list_user_id():
    print('A continuación se listan los IDs de los Usuarios registrados')
    print("----")
    print(" ID ")
    print("----")
    for id_user in id_users:
        print(id_user)
    input('Preciona una tecla para continuar')
    clear()

def view_user():
    try: 
        id = int(input('Ingrese el ID del usuario que desea consultar:'))
        if id in users:
            print_user(users[id])
        else:
            print(f'El id {id} no esta registrado en la lista de usuarios.')    
        input('Preciona una tecla para continuar')
        clear()
    except ValueError:
        input("Por favor, ingrese un número entero válido. Oprime una tecla para continuar.")

def edit_user():
    try: 
        id = int(input('Ingrese el ID del usuario que desea editar:'))
        if id in users:
            first_name = request_str("Ingresa tus nombres: ")
            last_name = request_str("Ingresa tus apellidos: ")
            phone_number = request_number("Ingresa tu numero de teléfono: ")
            email = input("Ingresa tu correo electrónico: ")
            print("Usuario actualizado con exito con el ID:", id)
            user_dict = {
                'firts_name'    : first_name,
                'last_name'     : last_name,
                'phone_number'  : phone_number,
                'email'         : email
            }
            users.update({id: user_dict})
        input("Oprime una tecla para continuar.")
        clear()    
    except ValueError:
        input("Por favor, ingrese un número entero válido. Oprime una tecla para continuar.")
    

def print_user(user):
    for id in user:
        print(f' {id} : {user[id]}')

def exit():
    print('Saliendo')

auto_increment = 0
id_users = []
users = {}

menu_main()

