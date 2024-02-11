# #RetoPython

## 🐍 Aprende python desde 0 con una semana de retos diarios

El #RetoPython se trata de una semana con aprendizaje y retos diarios para comenzar a programare con Python.
Este reto es creado por [CodigoFacilito](https://codigofacilito.com/)

Cada día del 05 al 09 de Febrero, en el sitio de codigo facilito [#RetoPython](https://codigofacilito.com/cursos/reto-python/)
publicaran una clase nueva con fundamentos de programación y Python, esta vendrá acompañada de un reto que deberás completar
para avanzar en el #RetoPython.

## Temas Aprendidos

- 🐍 Dia 0: Introducción al #RetoPython
  - Qué es el reto python?
  - Como usar gist para entregar tus soluciones a los retos.
  - Instalación de Python en Windows
  - Instalación de Python en Mac
- 🐍 Día 1: Lunes => Tipos de Datos
  - Variables,
  - Tipos de Datos (`int` - `float` - `str`)
  - Operadores relacionales ( `==`, `!=`, `>`, `>=`, `<`, `<=` )
  - Metodos python (`print`, `input`, `int`, `float`, `str`)
- 🐍 Día 2: Martes => Estructuras de Control
  - `if`, `elif`, `match` (switch)
  - `foreach` => Cuando sepamos cuantas iteraciones se necesitan.
  - `while` => Cuando NO sepamos cuantas iteraciones se necesitan (Condición).
- 🐍 Día 3: Miércoles => Listas
  - Listas: Estructuras de Datos
  - Metodos de Listas: `append`, `insert`, `extend`, `remove`, `clear`, `count`, `index`
  - `value in list` => `True` o `False`
  - Indices.
- 🐍 Día 4: Jueves => Tuplas y diccionarios
  - Llave: objetos inmutables (string, enteros, flotantes, Bool, Tuplas)
  - Metodos de los diccionarios: `keys()`,`values()`, `items()`
- 🐍 Día 5: Viernes => Funciones
  - Datos de entrada para una función = Argumentos o Parametros

## Desafios

### 🐍 Día 1: Lunes

Para este primer reto de la semana, tu objetivo será poder crear un programa en Python el cual permita registrar a un usuario en el sistema.

Para ello el programa deberá pedir a nuestro usuario final ingrese su siguiente información.

- Nombre(s)
- Apellidos
- Número de teléfono
- Correo electrónico.

Una vez el usuario haya ingresado todos los datos vía teclado, el programa le dará la bienvenida al usuario con el siguiente mensaje:

Hola + seguido del nombre completo del usuario +, en breve recibirás un correo a + seguido del correo electrónico.

### 🐍 Día 2: Martes

Para este segundo reto de la semana tu objetivo será incrementar el funcionamiento del programa del día de ayer. Si recordamos, ayer construimos un programa en Python capaz de registrar un nuevo usuario en el sistema. Pues bien, continuando con el proyecto, el reto de hoy será que podremos registrar un N cantidad de nuevos usuarios.

Para esto el programa deberá preguntar cuando nuevos usuarios se pretenden registrar.

Si el por ejemplo coloco 5, bueno, serán 5 nuevos usuarios los que se deben capturar, usuarios con sus correspondientes valores: Nombre, apellidos, número de teléfono y correo electrónico.

Además de todo esto, añadiremos una capa extra de seguridad, implementando un par de validaciones sobre los valores que se pueden ingresar.

Validaremos que, tanto nombre, apellidos como correo electrónico tengan una longitud mínimo de 5 caracteres y un longitud máxima de 50.

Así mismo el número de teléfono será a 10 dígitos.

Si por alguna razón el usuario ingresa mal alguno de estos datos, el programa deberá notificarle y no permitirá continuar hasta que se ingresen datos correctos.

### 🐍 Día 3: Miércoles

Vaya, ya llegamos al reto número 3 de la semana, y para este tercer reto lo que haremos será añadir 2 nuevas funcionalidades a nuestro programa de registro de usuarios.

Estas funcionalidades son las siguientes

1.- Siempre que se registre un nuevo usuario de forma exitosa generaremos un identificador único para este registro/usuario. Te recomiendo sea un ID numérico auto incremental, que comience en 1 hasta N. Sin embargo siéntete libre elegir el formato o tipo que tú desees.
2.- Todos estos nuevos identificadores deberán almacenarse en un listado que será impreso en consola cuando todos los registros se hayan creado. Esto de tal forma que el usuario pueda conocer y tenga certeza que las operaciones, en efecto, se realizaron de forma exitosa.

Con estas 2 nuevas funcionalidades es probable te intuyas como iremos finalizando nuestro programa para el quinto día.

### 🐍 Día 4: Jueves

Ya nos encontramos en la recta final de nuestra semana, y lo que haremos ahora, cómo ya es costumbre, será añadir más funcionalidades a nuestro programa.

Puntualmente 4 nuevas funcionalidades. Aquí van.

1.- Ahora todos los valores que representan a un usuario: Nombre, apellidos, número de teléfono y correo electrónico deberán almacenarse en un diccionario.

2.- Se añadirá la opción de poder listar el ID de todos los usuarios registrados hasta el momento.

3.- Se añadirá la opción de poder ver la información de un usuario con respecto a un ID. Es decir, el usuario podrá ingresar un ID y a partir de este conocer la información registrada.

4.- Se añadirá la opción de poder editar la información de un usuario con respecto a un ID. Es decir, el usuario podrá ingresar un ID y a partir de este el programa pedirá nuevamente los valores de un registro para actualizarlos.

Estas 3 nuevas opciones deberán ser presentadas al usuario al comienzo del programa, esto con la finalidad que sea el usuario quien defina que quiere hacer justo ahora: añadir nuevos usuario, consultarlos o editarlos.

De igual forma el programa tendrán una quinta opción que le permita la usuario finalizar el programa cuando él lo desee.

Un Tip. Para estas nuevas opciones puedes presentarle a tu usuario un pequeño menú del cual pueda elegir. Por ejemplo opción A.-) registrar nuevos usuarios, opción B.-) listar usuarios, Opción C.-) Editar usuarios y así sucesivamente.

### 🐍 Día 5: Viernes

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
