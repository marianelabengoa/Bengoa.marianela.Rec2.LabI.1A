import random
import os

def cargar_archivos(nombre_archivo: str) -> list:
    lista = []
    with open(nombre_archivo, "r", encoding="utf-8") as file:
        for linea in file:
            lista2 = linea.strip().split(",")
            try:
                pelicula = {
                    "id": lista2[0],
                    "titulo": lista2[1],
                    "genero": lista2[2],
                    "duracion": lista2[3],
                }
                lista.append(pelicula)
            except IndexError:
                continue
    return lista


def imprimir_lista(lista: list) -> None:
    for pelicula in lista:
        print(f"TITULO: {pelicula['titulo']}")
        print(f"ID: {pelicula['id']}")
        print(f"GENERO: {pelicula['genero']}")
        print(f"DURACION: {pelicula['duracion']}\n")


def asignar_duracion(pelicula):
    duracion = random.randint(100, 240)
    pelicula["duracion"] = duracion
    return pelicula


def filtrar_por_tipo(lista: list, nombre_archivo: str) -> bool:
    genero_encontrado = False
    lista1 = []
    genero = input("Ingrese el género del cual quiere filtrar las películas: ").capitalize()

    for pelicula in lista:
        if pelicula['genero'] == genero:
            lista1.append(pelicula)
            genero_encontrado = True

    if genero_encontrado:
        with open(nombre_archivo, "w") as file:
            for pelicula in lista1:
                file.write(f"id: {pelicula['id']}, titulo: {pelicula['titulo']}, genero: {pelicula['genero']}, duracion: {pelicula['duracion']}\n")
        return True
    else:
        print("Género no encontrado")
        return False


def ordenar_por_genero_y_duracion(lista: list) -> None:
    n = len(lista)
    for i in range(n - 1):
        for j in range(n - i - 1):
            pelicula_actual = lista[j]
            pelicula_siguiente = lista[j + 1]
            if pelicula_actual['genero'] > pelicula_siguiente['genero']:
                lista[j], lista[j + 1] = pelicula_siguiente, pelicula_actual
            elif pelicula_actual['genero'] == pelicula_siguiente['genero'] and pelicula_actual['duracion'] < pelicula_siguiente['duracion']:
                lista[j], lista[j + 1] = pelicula_siguiente, pelicula_actual

    for pelicula in lista:
        print("ID:", pelicula['id'])
        print("titulo:", pelicula['titulo'])
        print("genero:", pelicula['genero'])
        print("duracion:", pelicula['duracion'])
        print()



def guardar_peliculas(lista: list) -> None:
    nombre_archivo = input("Ingrese el nombre del archivo en el que desea guardar la información: ")
    with open(nombre_archivo, "w") as file:
        for pelicula in lista:
            file.write(f"id: {pelicula['id']}\n titulo: {pelicula['titulo']}\n genero: {pelicula['genero']}\n duracion: {pelicula['duracion']}\n\n")


def menu():
    opcion1 = False
    lista = []

    while True:
        os.system("cls")
        print("*** MENU DE OPCIONES ***")
        print("1. Cargar archivo")
        print("2. Imprimir lista")
        print("3. Asignar tiempos")
        print("4. Filtrar por tipo")
        print("5. Mostrar duraciones")
        print("6. Guardar películas")
        print("7. Salir")
        print()
        opcion = int(input("Ingrese opción: "))

        if opcion == 1:
            archivo = input("Ingrese el nombre del archivo del que quiere cargar los datos: ")
            lista = cargar_archivos(archivo)
            opcion1 = True
        elif opcion == 2:
            if opcion1 == False:
                print("Primero ingresa los datos (opción 1)")
            else:
                imprimir_lista(lista)
        elif opcion == 3:
            if opcion1 == False:
                print("Primero ingresa los datos (opción 1)")
            else:
                lista = list(map(asignar_duracion, lista))
                print("Duración asignada aleatoriamente.")
        elif opcion == 4:
            if opcion1 == False:
                print("Primero ingresa los datos (opción 1)")
            else:
                nombre_archivo = input("Ingrese el nombre del archivo al que quiere filtrar las películas: ")
                filtrar_por_tipo(lista, nombre_archivo)
        elif opcion == 5:
            if opcion1 == False:
                print("Primero ingresa los datos (opción 1)")
            else:
                ordenar_por_genero_y_duracion(lista)
        elif opcion == 6:
            if opcion1 == False:
                print("Primero ingresa los datos (opción 1)")
            else:
                guardar_peliculas(lista)
        elif opcion == 7:
            break
        os.system("pause")


menu()