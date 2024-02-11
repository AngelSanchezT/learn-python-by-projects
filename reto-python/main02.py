# Reto Python Día #2
"""
Para este segundo reto de la semana tu objetivo será incrementar el funcionamiento del programa del día de ayer. Si recordamos, ayer construimos un programa en Python capaz de registrar un nuevo usuario en el sistema. Pues bien, continuando con el proyecto, el reto de hoy será que podremos registrar un N cantidad de nuevos usuarios.

Para esto el programa deberá preguntar cuando nuevos usuarios se pretenden registrar.

Si el por ejemplo coloco 5, bueno, serán 5 nuevos usuarios los que se deben capturar, usuarios con sus correspondientes valores: Nombre, apellidos, número de teléfono y correo electrónico.

Además de todo esto, añadiremos una capa extra de seguridad, implementando un par de validaciones sobre los valores que se pueden ingresar.

Validaremos que, tanto nombre, apellidos como correo electrónico tengan una longitud mínimo de 5 caracteres y un longitud máxima de 50.

Así mismo el número de teléfono será a 10 dígitos.

Si por alguna razón el usuario ingresa mal alguno de estos datos, el programa deberá notificarle y no permitirá continuar hasta que se ingresen datos correctos.
"""

def register_user():
    first_name = request_str("Ingresa tus nombres: ")
    last_name = request_str("Ingresa tus apellidos: ")
    phone_number = request_number("Ingresa tu numero de teléfono: ")
    email = input("Ingresa tu correo electrónico: ")
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
     

try:
    total_users = input("Ingresa el número de usuarios a registrar: ")
    total_users = int(total_users)
    index_user = 1
    while index_user <= total_users:
        print("Inicio de Registro del Usuario: #" + str(index_user))
        register_user()
        index_user += 1
except ValueError:
    print("Error: número de usuarios ingresado es invalido!")
