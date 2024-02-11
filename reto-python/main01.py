# Reto Python Día #1
"""
Para este primer reto de la semana, tu objetivo será poder crear un programa en Python el cual permita registrar a un usuario en el sistema.

Para ello el programa deberá pedir a nuestro usuario final ingrese su siguiente información.

Nombre(s)
Apellidos
Número de teléfono
Correo electrónico.
Una vez el usuario haya ingresado todos los datos vía teclado, el programa le dará la bienvenida al usuario con el siguiente mensaje:

Hola + seguido del nombre completo del usuario +, en breve recibirás un correo a + seguido del correo electrónico .
"""

first_name = input("Ingresa tus nombres: ")
last_name = input("Ingresa tus apellidos: ")
phone_number = input("Ingresa tu numero de teléfono: ")
email = input("Ingresa tu correo electrónico: ")

message_confirm = "Hola " + first_name + " " + last_name + " en breve recibirás un correo a " + email

print(message_confirm)