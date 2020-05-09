import json, re, csv, validators



# Load contacts from JSON
with open("contacts.json") as file:
    contacts = json.load(file)

for key,value in contacts.items():
    for contact in value.items():
        print(contact[0])
        for field, val in contact[1].items():
            print(field+":", val)





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
    # Displays contacts with display function, erase based on number index

    input_nombre = input("Ingrese nombre del contacto que quiere eliminar\n")
    existe = input_nombre in contacts

    if existe:
        del contacts[input_nombre]
        print("Contacto eliminado con exito!\n")
    else:
        print("El contacto no existe, intentelo de nuevo\n")


def verContactos():

    # Prints dict in list form is numbered and arranged alphabetically. Not including letters that dont exist yet.
    ## After printing list ask to see any individual contact. Enter 0 for exit.
    count = 0
    for key,value in contacts.items():
        print(key + ":")
        for contact in value:
            count = count + 1
            print("  ",str(count) + ".",contact)

    index = input("Ver Contacto: ")

    count = 0
    for key, value in contacts.items():
        for contact in value.items():
            count += 1
            if (count == int(index)):
                print(contact[0])
                for field, val in contact[1].items():
                    print(field + ":", val)


def guardarContactos():
    # saves changes, should be able to be called from anywhere
    pass

def llamarContacto():
    # Does wierd print thingy and waits then returns to main menu
    pass

def textContacto():
    # Prints texting and waits to return to mm
    pass

def emailContacto():
    # Prints emailing, asks for sender, subject and message etc
    pass

def exportarContactos():
    # export to csv
    pass



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
        # Ask  to save changes or not
        guardarContactos()
        exit = True