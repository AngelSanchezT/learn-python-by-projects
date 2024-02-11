# Reto Python Día #3

"""
Vaya, ya llegamos al reto número 3 de la semana, y para este tercer reto lo que haremos será añadir 2 nuevas funcionalidades a nuestro programa de registro de usuarios.

Estas funcionalidades son las siguientes

1.- Siempre que se registre un nuevo usuario de forma exitosa generaremos un identificador único para este registro/usuario. Te recomiendo sea un ID numérico auto incremental, que comience en 1 hasta N. Sin embargo siéntete libre elegir el formato o tipo que tú desees.
2.- Todos estos nuevos identificadores deberán almacenarse en un listado que será impreso en consola cuando todos los registros se hayan creado. Esto de tal forma que el usuario pueda conocer y tenga certeza que las operaciones, en efecto, se realizaron de forma exitosa.

Con estas 2 nuevas funcionalidades es probable te intuyas como iremos finalizando nuestro programa para el quinto día.

Entrega tu ejercicio aquí
"""

import os

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
    auto_increment += 1
    print("Usuario Registrado con exito con el ID:", auto_increment)
    id_users.append(auto_increment)
    message_confirm = "Hola " + first_name + " " + last_name + " en breve recibirás un correo a " + email
    print(message_confirm)


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
     
auto_increment = 0
id_users = []


print("----------")
print("BIENVENIDO")
print("----------")
total_users = ask_number_of_users()
index_user = 1
while index_user <= total_users:
    clear()
    print("Inicio de Registro del Usuario: #" + str(index_user))
    register_user()
    index_user += 1

print("----")
print("Se registraron", len(id_users), "usuario(s) exitosamente.")
print("----")
print(" ID ")
print("----")
for id_user in id_users:
    print(id_user)
