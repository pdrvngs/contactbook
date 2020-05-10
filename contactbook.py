import json, re, csv, validators


info = {}
# Load contacts from JSON
with open("contacts.json") as file:
    contacts = json.load(file)


exit = False

def crearContacto():
    nombre = input("Nombre: ")
    telefono = input("Telefono: ")
    email = input("Email: ")
    company = input("Company: ")
    extra = input("Extra: ")

    first_letter = nombre[0].upper()
    alf_ord = []
    for key, value in contacts.items():
        if key not in alf_ord:
            alf_ord.append(key)

    if first_letter not in alf_ord:
        contacts[first_letter] = {}

    for key in contacts.keys():
        if key == first_letter:
            contacts[key][nombre] = {'telefono': telefono, 'email': email, 'company': company, 'extra': extra}


def editarContacto():
    listarContactos()

    index = input("Ver Contacto: ")
    print("\n\n")
    count = 0
    for key, value in contacts.items():
        for contact in value.items():
            count += 1
            if (count == int(index)):
                print(contact[0])
                edit_name = contact[0]
                edit_key = key
                for field, val in contact[1].items():
                    print("  " + field + ":", val)

    change = int(input("Which field would you like to change?\n 1. Telefono\n 2. Email\n 3. Company\n 4. Extra \n 5. Nada\n"))

    if change == 1:
        contacts[edit_key][edit_name]['telefono'] = input("Nuevo Telefono: ")
    if change == 2:
        contacts[edit_key][edit_name]['email'] = input("Nuevo Email: ")
    if change == 3:
        contacts[edit_key][edit_name]['Company'] = input("Nuevo Company: ")
    if change == 4:
        contacts[edit_key][edit_name]['Extra'] = input("Nuevo Extra: ")
    if change == 5:
        pass


def buscarContacto():
    # Look up by name or last name. Use regex for parcial matches

    pass


def eliminarContacto():
    listarContactos()
    delete = False
    index = input("Eliminar Contacto: ")
    print("\n\n")
    count = 0
    for key, value in contacts.items():
        for contact in value.items():
            count += 1
            if (count == int(index)):
                delete_key =  key
                delete_contact = contact[0]
                delete = True

    if delete == True:
        del contacts[delete_key][delete_contact]



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

    index = input("Ver Contacto: ")
    print("\n\n")
    count = 0
    for key, value in contacts.items():
        for contact in value.items():
            count += 1
            if (count == int(index)):
                print(contact[0])
                for field, val in contact[1].items():
                    print("  "+field + ":", val)
                print("\n\n")
                input("Presione enter para continuar.")
                print("\n\n\n\n")


def guardarContactos():
    # saves changes, should be able to be called from anywhere
    pass

def llamarContacto():
    listarContactos()
    index = input("Llamar Contacto: ")
    print("\n")
    count = 0

    for key, value in contacts.items():
        for contact in value.items():
            count += 1
            if (count == int(index)):
                telefono = contact[1]['telefono']
                print("Llamando a " + contact[0] + " al " + telefono)


def textContacto():
    listarContactos()
    index = input("Mensajear Contacto: ")
    print("\n")
    count = 0

    for key, value in contacts.items():
        for contact in value.items():
            count += 1
            if (count == int(index)):
                print(contact[0])
                message = input("Mensaje: ")
                telefono = contact[1]['telefono']
                print("Hola " + contact[0] + " " + telefono)
                print("   > ", message)

def emailContacto():
    listarContactos()
    index = input("Email Contacto: ")
    print("\n")
    count = 0

    for key, value in contacts.items():
        for contact in value.items():
            count += 1
            if (count == int(index)):
                print(contact[0])
                subject = input("Subejct: ")
                mensaje = input("Mensaje: ")
                email = contact[1]['email']
                print("Enviando correo a " + contact[0] + " " + email)
                print("   > ", subject)
                print("   > ", mensaje)

def exportarContactos():
    with open("contact_manager.csv", 'w', newline='') as contacts_csv:
        fieldnames = ['name', 'telefono', 'email', 'company', 'extra']
        writer = csv.DictWriter(contacts_csv, fieldnames = fieldnames)
        writer.writeheader()
        for key, value in contacts.items():
            for contact in value.items():
                writer.writerow({'name': contact[0], 'telefono': contact[1]['telefono'], 'email': contact[1]['email'], 'company': contact[1]['company'], 'extra': contact[1]['extra']})


while not exit:

    input_menu = int(input(" 1. Agregar Contacto \n 2. Editar Contacto\n 3. Buscar Contacto\n 4. Eliminar Contacto\n 5. Ver Contactos\n 6. Llamar Contacto \n 7. Text Contacto \n 8. Email Contacto \n 9. Exportar Contactos \n 10. Salir\n"))
    if input_menu == 1: # Done
        crearContacto()
    if input_menu == 2:
        editarContacto()
    if input_menu == 3:
        buscarContacto()
    if input_menu == 4: # Done
        eliminarContacto()
    if input_menu == 5: # Done
        verContactos()
    if input_menu == 6: # Done
        llamarContacto()
    if input_menu == 7: # Done
        textContacto()
    if input_menu == 8: # Done
        emailContacto()
    if input_menu == 9: # Done
        exportarContactos()

    elif input_menu == 10:

        guardarContactos()
        exit = True