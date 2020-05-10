import json, re, csv, validators



# Load contacts from JSON
with open("contacts.json") as file:
    contacts = json.load(file)

for key,value in contacts.items():
    for contact in value.items():
        print(contact[0])
        print(contact[1]['telefono'])





exit = False

def crearContacto():

    # Input fields: V; Name&Last, V;phone, V; email, E; company, E; extra
    # fail upon wrong ingres of any of these, preferably reverting to the ones not correctly inputed.

    input_nombre = input("Ingrese nombre del nuevo contacto\n")
    input_telefono = input("Ingrese telefono del nuevo contacto\n")
    contacts[input_nombre] = input_telefono

def editarContacto():
    input_nombre = input("Ingrese nombre del contacto que quiere editar\n")

    existe = input_nombre in contacts

    if existe:
        input_telefono = input("Ingrese nuevo telefono del contacto\n")
        contacts[input_nombre] = input_telefono
    else:
        print("El contacto no existe, porfavor intente de nuevo\n")

def buscarContacto():
    # Look up by name or last name. Use regex for parcial matches

    input_nombre = input("Ingrese nombre del contacto que quiere buscar\n")
    existe = input_nombre in contacts

    if existe:
        print(input_nombre + " " + contacts[input_nombre])
    else:
        print("El contacto no existe, porfavor intente de nuevo\n")


def eliminarContacto():
    pass
    # Displays contacts with display function, erase based on number index


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
    if input_menu == 1:
        crearContacto()
    if input_menu == 2:
        editarContacto()
    if input_menu == 3:
        buscarContacto()
    if input_menu == 4:
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