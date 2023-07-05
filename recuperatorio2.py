import random
import sys
import os

def cargar_archivos(nombre_archivo:str) -> list:
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
        print(f"DURACION: {pelicula['duracion']}\n\n")


def filtrar_por_tipo(lista: list, nombre_archivo:str)->bool:
    genero_encontrado = False
    lista1 = []
    while True:
        genero = input(
            "ingrese el genero del cual quiere filtrar las peliculas: ").capitalize()
        for pelicula in lista:
            if pelicula['genero'] == genero:
                id = pelicula['id']
                titulo = pelicula['titulo']
                duracion = pelicula['duracion']
                lista1.append(pelicula)
                genero_encontrado = True

            with open(nombre_archivo, "w") as file:
                for pelicula in lista1:
                    file.write(f"id: {id}, titulo: {titulo}, genero: {genero}, duracion: {duracion}\n\n")

            return True

        if not genero_encontrado:
            print("genero no encontrado")
            return False


def mostrar_duraciones(lista: list)->list:
    for i in range(len(lista) - 1):
        for j in range(i + 1, len(lista)):
            if lista[i]['genero'] > lista[j]['genero']:
                lista[i], lista[j] = lista[j], lista[i]
            elif lista[i]['genero'] == lista[j]['genero'] and lista[i]['duracion'] < lista[j]['duracion']:
                lista[i], lista[j] = lista[j], lista[i]
    return lista


def mostrar_peliculas_ordenadas_por_genero_y_duracion(lista: list) -> None:
    print("peliculas ordenadas por genero y duracion:")
    for pelicula in lista:
        print("ID:", pelicula['id'])
        print("titulo:", pelicula['titulo'])
        print("genero:", pelicula['genero'])
        print("duracion:", pelicula['duracion'])
        print()


def guardar_peliculas(lista: list)->None:
    nombre_archivo = input( "ingrese el nombre del archivo en el que desea guardar la informacion: ")
    with open(nombre_archivo, "w") as file:
        for pelicula in lista:
            file.write(f"id:{pelicula['id']}\n titulo:{pelicula['titulo']}\n genero:{pelicula['genero']}\n duracion{pelicula['duracion']}\n\n")


def menu():
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
        print(" ")
        opcion = int(input("ingrese opcion: "))

        if opcion == 1:
            archivo = input(
                "ingrese el nombre del archivo del que quiere cargar los datos: ")
            lista = cargar_archivos(archivo)
        elif opcion == 2:
            imprimir_lista(lista)
        elif opcion == 3:
            pass
        elif opcion == 4:
            nombre_archivo = input(
                "ingrese el nombre del archivo al que quiere filtrar las peliculas: ")
            filtrar_por_tipo(lista, nombre_archivo)
        elif opcion == 5:
            list=mostrar_duraciones(lista)
            mostrar_peliculas_ordenadas_por_genero_y_duracion(list)
        elif opcion == 6:
            list=mostrar_duraciones(lista)
            guardar_peliculas(list)
        elif opcion == 7:
            break
        os.system("pause")


menu()
