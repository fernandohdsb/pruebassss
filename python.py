
def buscarPalabra(objetivo,nombres):

    TF = False
    if objetivo in nombres:
        TF = True

    return TF





def imprimirListaInversa(nombres):
    for nombre in range(3,-1,-1):
        print(nombres[nombre])
        print()







nombres = ["Mengano", "Fulano", "Zutano", "Perantano"]

imprimirListaInversa(nombres)


edades = {
    "Mengano": 0,
    "Fulano": 25,
    "Zutano": 50,
    "Perantano": 75
} 

while True :
    nombre = input("Buscar nombre: ")

    if nombre == "exit": break
    elif buscarPalabra(nombre,nombres): print(nombre + " tiene " + str(edades[nombre]) + " años")
    else: print("El nombre no existe...")
    print()


print("FIN DEL PROGRAMA")
    