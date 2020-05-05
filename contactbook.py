import json
import re

contacts = {}

# Load contacts from JSON

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
    # Displays

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

    for key,value in contacts.items():
        print(key + " " + value)


def guardarContactos():

    pass

def llamarContacto():
    pass

def textContacto():
    pass

def emailContacto():
    pass

def exportarContactos():
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