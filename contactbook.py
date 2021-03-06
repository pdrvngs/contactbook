from csv import DictWriter
from emoji import emojize
from json import load as jsonload
from re import search as research
from time import sleep
from validators import email as emailcheck

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
# Load contacts from JSON
with open("contacts.json") as file:
    contacts = jsonload(file)

exit_menu = False


def crearContacto():

    # Validacion de que se ingrese algo para el nombre
    nombre = input("Nombre: ")
    while len(nombre) < 1:
        nombre = input("Porfavor ingrese un nombre: ")

    # Validacion del numero telefonico
    valid_phone = 0
    telefono = ""
    while valid_phone != 8:
        valid_phone = 0
        telefono = input("Telefono: ")
        for i in telefono:
            if i in numbers:
                valid_phone += 1
            else:
                pass
        if valid_phone != 8:
            print("Numero telefonico invalido, porfavor intente de nuevo:\n")

# Validacion del correo
    email = input("Correo: ")
    while emailcheck(email) is not True:
        email = input("No es un correo valido, porfavor intente de nuevo: \n")

# Estas casillas no son necesarias, por lo tanto no se validan.
    company = input("Empresa: ")
    extra = input("Extra: ")

# Crea un nuevo KEY para el orden alfabetico.
    first_letter = nombre[0].upper()
    alf_ord = []
    for key, value in contacts.items():
        if key not in alf_ord:
            alf_ord.append(key)

    if first_letter not in alf_ord:
        contacts[first_letter] = {}

# Asignamos todos los valores al key alfabetico correcto y se asignan el diccionario de info con el nombre como key.
    for key in contacts.keys():
        if key == first_letter:
            contacts[key][nombre] = {'telefono': telefono, 'email': email, 'company': company, 'extra': extra}

    print("\n\n\n")


def editarContacto():
    listarContactos()

    valid_phone = 0
    telefono = ""
    found = False
    index = input("Editar Contacto: ")
    print("\n\n")
    count = 0

    try:
        index = int(index)

    except ValueError:
        pass

    for key, value in contacts.items():
        for contact in value.items():
            count += 1
            # Contamos mientra itera sobre los nombres y buscamos cuando la cuenta sea igual al numero del usuario
            # Si index no es int, solo busca que el nombre ingresado sea igual al que esta en iteracion.
            if count == index or contact[0] == index:
                print(contact[0])
                found = True
                edit_name = contact[0]
                edit_key = key
                for field, val in contact[1].items():
                    print("  " + field + ":", val)

                change = int(input(
                    "\nWhich field would you like to change?\n 1. Telefono\n "
                    "2. Email\n 3. Company\n 4. Extra \n 5. Nada\n"))

                if change == 1:
                    while valid_phone != 8:
                        valid_phone = 0
                        telefono = input("Nuevo Telefono: ")
                        for i in telefono:
                            if i in numbers:
                                valid_phone += 1
                            else:
                                pass
                        if valid_phone != 8:
                            print("Numero telefonico invalido, porfavor intente de nuevo:\n")

                    contacts[edit_key][edit_name]['telefono'] = telefono

                if change == 2:

                    email = input("Nuevo correo: ")
                    while emailcheck(email) is not True:
                        email = input("No es un correo valido, porfavor intente de nuevo: \n")

                    contacts[edit_key][edit_name]['email'] = email
                if change == 3:
                    contacts[edit_key][edit_name]['Company'] = input("Nueva empresa: ")
                if change == 4:
                    contacts[edit_key][edit_name]['Extra'] = input("Nueva información extra: ")
                if change == 5:
                    pass

    if found is not True:
        print("Contacto Invalido\n")

    print("\n\n\n")


def buscarContacto():
    searcher = input("Ingrese a quien quisiera buscar: ")
    for key, value in contacts.items():
        for contact in value.items():
            # Usamos RegEx para hacer un parcial match de lo que ingrese el usuario.
            if research(rf"{searcher.lower()}", contact[0].lower()):
                print("-", contact[0])

    print("\n\n")
    input("Presione enter para continuar")
    print("\n\n\n")


def eliminarContacto():
    listarContactos()
    delete = False
    index = input("Eliminar contacto: ")
    print("\n\n")
    count = 0
    delete_contact = ""
    delete_key = ""

    try:
        index = int(index)

    except ValueError:
        pass

    for key, value in contacts.items():
        for contact in value.items():
            count += 1
            if count == index or contact[0] == index:
                delete_key = key
                delete_contact = contact[0]
                delete = True

    # Busca si existe el contacto, si existe lo borra llamando sus keys.
    if delete is True:
        print(f"Contacto {delete_contact} borrado\n\n")
        del contacts[delete_key][delete_contact]
        sleep(3)


def listarContactos():
    count = 0
    for key, value in contacts.items():
        print(key + ":")
        for contact in value:
            count = count + 1
            print("  ", str(count) + ".", contact)
        print("")


def verContactos():
    listarContactos()

    index = input("Ver contacto: ")
    print("\n\n")
    count = 0

    try:
        index = int(index)

    except ValueError:
        pass

    for key, value in contacts.items():
        for contact in value.items():
            count += 1
            if count == index or contact[0] == index:
                print(contact[0])
                for field, val in contact[1].items():
                    print("  " + field + ":", val)
                print("\n\n")
                input("Presione enter para continuar.")
                print("\n\n\n\n")


def llamarContacto():
    listarContactos()
    index = input("Llamar contacto: ")
    print("\n")
    count = 0

    try:
        index = int(index)

    except ValueError:
        pass

    for key, value in contacts.items():
        for contact in value.items():
            count += 1
            if count == index or contact[0] == index:
                telefono = contact[1]['telefono']
                print(emojize("Llamando :phone: a " + contact[0] + " al " + telefono, use_aliases=True))
                sleep(3)

    print("\n\n\n")


def textContacto():
    listarContactos()
    index = input("Mensajear Contacto: ")
    print("\n")
    count = 0

    try:
        index = int(index)

    except ValueError:
        pass

    for key, value in contacts.items():
        for contact in value.items():
            count += 1
            if count == index or contact[0] == index:
                print(contact[0])
                message = input("Mensaje: ")
                telefono = contact[1]['telefono']
                print("Hola " + contact[0] + " " + telefono)
                print("   > ", message)
                enviar = input("\nDesea enviar el mensaje? (y/n)\n ")
                if enviar.lower() == 'y':
                    print(f"\nEnviando mensaje a {contact[0]}\n\n")
                    sleep(3)
                else:
                    print("\nMensaje no enviado\n\n")
                    sleep(1)

    print("\n\n\n")


def emailContacto():
    listarContactos()
    index = input("Email contacto: ")
    print("\n")
    count = 0

    try:
        index = int(index)

    except ValueError:
        pass

    for key, value in contacts.items():
        for contact in value.items():
            count += 1
            if count == index or contact[0] == index:
                print(contact[0])
                subject = input("Sujeto: ")
                mensaje = input("Mensaje: ")
                email = contact[1]['email']
                print(emojize("Enviando :envelope: a " + contact[0] + " " + email))
                print("   > ", subject)
                print("   > ", mensaje)
                print("\n\n\n")
                sleep(2)


def exportarContactos():
    with open("contact_manager.csv", 'w', newline='') as contacts_csv:
        infonames = ['name', 'telefono', 'email', 'company', 'extra']
        writer = DictWriter(contacts_csv, fieldnames=infonames)
        writer.writeheader()
        for key, value in contacts.items():
            for contact in value.items():
                writer.writerow({'name': contact[0], 'telefono': contact[1]['telefono'], 'email': contact[1]['email'],
                                 'company': contact[1]['company'], 'extra': contact[1]['extra']})
    print("Contactos exportados con exito.")
    sleep(3)
    print("\n\n\n")


while not exit_menu:

    input_menu = 10
    valid = False
    while valid is False:
        try:
            input_menu = int(input(" 1. Agregar Contacto \n 2. Editar Contacto\n 3. Buscar Contacto\n"
                                   " 4. Eliminar Contacto\n 5. Ver Contactos\n 6. Llamar Contacto \n "
                                   "7. Text Contacto \n 8. Email Contacto \n 9. Exportar Contactos \n 10. Salir\n"))
            valid = True
        except ValueError:
            print("\n\n\n")
            print("Not es una opción valida.")

    if input_menu == 1:
        crearContacto()
    if input_menu == 2:
        editarContacto()
    if input_menu == 3:
        buscarContacto()
    if input_menu == 4:
        eliminarContacto()
    if input_menu == 5:
        verContactos()
    if input_menu == 6:
        llamarContacto()
    if input_menu == 7:
        textContacto()
    if input_menu == 8:
        emailContacto()
    if input_menu == 9:
        exportarContactos()

    elif input_menu == 10:
        exit_menu = True
