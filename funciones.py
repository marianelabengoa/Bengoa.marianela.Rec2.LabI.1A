import json

########## OPCION 1 ###########
def leer_datos_csv(nombre_archivo:str)->list:
    lista = []
    with open(nombre_archivo, "r", encoding = "utf-8") as file:
        for linea in file:
            lista2 = linea.strip().split(",")
            try:
                insumo = {
                    "id": lista2[0],
                    "nombre": lista2[1],
                    "marca": lista2[2],
                    "precio": lista2[3],
                    "caracteristicas": lista2[4]
                }
                lista.append(insumo)

            except IndexError:
                continue
    return lista


########## OPCION 2 ###########

def obtener_cantidad_por_marca(datos:list)->dict:
    cantidad_por_marca = {}
    for elemento in datos:
        marca = elemento['marca']
        cantidad = cantidad_por_marca.get(marca, 0)
        cantidad += 1
        cantidad_por_marca[marca] = cantidad
    return cantidad_por_marca


def mostrar_cantidad_por_marca(cantidad_por_marca:dict)->None:
    for marca in cantidad_por_marca:
        cantidad = cantidad_por_marca[marca]
        print(f"Marca: {marca} - Cantidad: {cantidad}")



########## OPCION 3 ###########

def agrupar_insumos_por_marca(datos:list)->dict:
    insumos_por_marca = {}
    for elemento in datos:
        marca = elemento['marca']
        insumos_por_marca[marca] = insumos_por_marca.get(marca, [])
        insumos_por_marca[marca].append((elemento['nombre'], elemento['precio']))
    return insumos_por_marca


def mostrar_insumos_por_marca(datos:list)->None:
    insumos_por_marca = {}

    for elemento in datos:
        marca = elemento['marca']
        nombre = elemento['nombre']
        precio = elemento['precio']

        insumos_por_marca[elemento['marca']] = insumos_por_marca.get(
            elemento['marca'], [])
        insumos_por_marca[elemento['marca']].append(
            (elemento['nombre'], elemento['precio']))

    for elemento['marca'] in insumos_por_marca:
        print("Marca:", elemento['marca'])

        insumos = insumos_por_marca[elemento['marca']]
        for insumo in insumos:
            nombre = insumo[0]
            precio = insumo[1]
            print("  Nombre:", nombre)
            print("  Precio:", precio)



########## OPCION 4 ###########

def buscar_insumos_por_caracteristica(lista:list, caracteristica:str)->list:
    insumos_con_caracteristica = []
    for insumo in lista:
        if caracteristica in insumo["caracteristicas"]:
            insumos_con_caracteristica.append(insumo)
    return insumos_con_caracteristica


def mostrar_insumos_con_caracteristica(lista:list, insumos_con_caracteristica:list, caracteristica:str)->None:
    insumos_con_caracteristica=buscar_insumos_por_caracteristica(lista, caracteristica)
    if insumos_con_caracteristica:
        print(f"Insumos con la característica '{caracteristica}':")
        for insumo in insumos_con_caracteristica:
            print(insumo)
            print("")
    else:
        print(
            f"No se encontraron insumos con la característica '{caracteristica}'.")



########## OPCION 5 ###########

def ordenar_lista_por_marca_y_precio(lista:list):
    for i in range(len(lista) - 1):
        for j in range(i + 1, len(lista)):
            if lista[i]['marca'] > lista[j]['marca']:
                lista[i], lista[j] = lista[j], lista[i]
            elif lista[i]['marca'] == lista[j]['marca'] and lista[i]['precio'] < lista[j]['precio']:
                lista[i], lista[j] = lista[j], lista[i]


def mostrar_insumos_ordenados_por_marca_y_precio(lista:list)->None:
    print("Insumos ordenados por marca y precio:")
    for insumo in lista:
        print("ID:", insumo['id'])
        print("Descripción:", insumo['nombre'])
        print("Precio:", insumo['precio'])
        print("Marca:", insumo['marca'])
        caracteristicas = insumo['caracteristicas'].split("~")
        if caracteristicas:
            print("Primera característica:", caracteristicas[0])
        print()



########## OPCION 6 ###########

def realizar_compra(datos:list)->None:
    compra = []
    total = 0
    marca_encontrada=False
    confirm=True

    while confirm==True:
        marca = input("Ingrese la marca de los insumos que desea comprar (o 'Salir' para finalizar): ").capitalize()
        if marca == "Salir":
            break
        for producto in datos:
            if producto["marca"] == marca:
                print("Descripción:", producto["nombre"])
                print("Precio:", producto["precio"])
                print()
                marca_encontrada = True
        if not marca_encontrada:
            print("marca no encontrada")
            
        
        producto_nombre = input("Ingrese el nombre del producto que desea comprar (o 'Salir' para finalizar la compra): ").capitalize()
        if producto_nombre == "Salir":
            break

        producto_encontrado = False
        subtotal = 0

        for producto in datos:
            if producto["nombre"] == producto_nombre:
                producto_encontrado = True
                try:
                    cantidad = int(input("Ingrese la cantidad deseada: "))
                except ValueError:
                    print("no es un numero")
                producto["precio"] = float(producto["precio"].replace("$", ""))
                subtotal = producto["precio"] * cantidad
                total += subtotal
                compra.append((producto, cantidad, subtotal))
                print(f"Se agregó {cantidad} {producto['nombre']} a la compra.")
                break
        if not producto_encontrado:
            print("El producto ingresado no es valido")
                

        print("***COMPRA FINALIZADA***")
        print("Detalles de la compra:")
        for producto, cantidad, subtotal in compra:
            print(f"{cantidad} {producto['nombre']} - Subtotal: {subtotal}")
        print("Total de la compra:", total)

        with open("factura_de_la_compra.txt", "a") as file:
            file.write("""Cantidad / Producto / Subtotal\n\n""")
            for producto, cantidad, subtotal in compra:
                file.write(f"""{cantidad} / {producto['nombre']} / {subtotal}\nTotal: {total}\n
                        
                        """)
        
        respuesta=input("\ndesea ingrear otro producto? (si/no) ").lower()
        if respuesta=="si":
            confirm=True
        else:
            confirm=False




########## OPCION 7 ###########

def filtrar_productos_por_palabra_clave(datos:list, palabra_clave:str)->list:
    productos_filtrados = []
    for producto in datos:
        if palabra_clave in producto["nombre"]:
            productos_filtrados.append(producto)
    return productos_filtrados


def mostrar_productos(lista:list)->None:
    for insumo in lista:
        print("ID:", insumo['id'])
        print("Descripción:", insumo['nombre'])
        print("Precio:", insumo['precio'])
        print("Marca:", insumo['marca'])

def guardar_datos(datos:list, nombre_archivo:str)->None:
    js = json.dumps(datos, indent = 2)
    with open(nombre_archivo, "w") as file:
        file.write(js)


########## OPCION 9 ###########
def aplicar_aumento(producto:dict)->dict:
    producto["precio"] = float(producto["precio"].replace("$", ""))
    precio_actualizado = producto["precio"] * 1.084
    producto["precio"] = round(precio_actualizado, 2)
    return producto



def aumento(datos:list)->None:
    for producto in datos:
        pr = producto["precio"]
        pr=str(pr)
        pr = (pr.strip("$").replace(",", ".").replace("PRECIO", "").replace(" ","0").replace("","0"))
        pr = float(pr)
        aumento = pr+(pr*0.84)
        producto["precio"] = pr
    for producto in datos:
        print(producto["marca"])
        print(producto["nombre"])
        print(producto["precio"])
        print("-------------")



########## OPCION 10 ###########

def agregar_elemento(nombre_archivo:str)->list:
    lista = []
    while True:
        try:
            id = int(input("ingrese el id (mayor a 50): "))
            if id > 50:
                break

        except ValueError:
            print("id no valido")

    nombre = input("ingrese el nombre del producto: ")

    file = open("marcas.txt", "r")
    marcas = file.read()
    print(f"""MARCAS
    
    {marcas}""")

    marca = input("ingrese la marca del producto: ")
    for linea in marcas:
        if marca in linea:
            break
    marca=marca.capitalize()

    while True:
        try:
            precio = float(input("ingrese el precio (mayor a 8): "))
            if precio > 8:
                break
        except ValueError:
            print("precio no valido")

    caracteristicas = input("ingrese las caracteristicas del producto: ")

    with open(nombre_archivo, "r", encoding="utf-8") as file:
        insumo = {
            "id": id,
            "nombre": nombre,
            "marca": marca,
            "precio": precio,
            "caracteristicas": caracteristicas
        }
        lista.append(insumo)
    return lista



########## OPCION 11 ###########

def llenar_archivo(lista:list)->None:
    tipo_archivo=input("ingrese el nombre del archivo al que quiere agregar la informacion (solo es permitido archivos csv o json):")

    if ".csv" in tipo_archivo:
        with open(tipo_archivo, "a") as file: 
            for elemento in lista:
                datos=(f"""
                       
                {elemento['id']},
                {elemento['nombre']},
                {elemento['marca']},
                ${elemento['precio']},
                {elemento['caracteristicas']}
                       
                       """)
                file.write(datos)

    elif ".json" in tipo_archivo:
        with open(tipo_archivo, "w")as file:
            json.dump(lista, file, indent=4)
    
    else:
        print("no valido")


########## OPCION 12 ###########
# Agregar opción stock por marca: Pedirle al usuario una marca y
# mostrar el stock total de los productos de esa marca.


def set_por_stock(datos: list, valor: str)->set:
    productos = set()
    for elemento in datos:
        productos.add(elemento[valor])
    return productos

def stock_por_marca(datos: list, set: set, valor: str, titulo: str)->None:
    titulo.upper
    for producto in set:
        print(f"-------------------------\n{titulo} : {producto}")
        for marca in datos:
            if (producto == marca[valor]):
                print(f"{marca['nombre']}")


def mostrar_stock_marca(datos: list, valor: str, titulo: str):
    sets = set_por_stock(datos, valor)
    stock_por_marca(datos, sets, valor, titulo)


########## OPCION 13 ###########
# Agregar opción imprimir bajo stock. Que imprima en un archivo de
# texto en formato csv. Un listado con el nombre de producto y el stock de
# aquellos productos que tengan 2 o menos unidades de stock.



def mostrar_insumos_menos_de_dos_unidades(datos:list, cantidad_por_marca: dict, nombre_archivo:str) -> None:
    l = []
    for marca in cantidad_por_marca:
        cantidad = cantidad_por_marca[marca]
        if cantidad <= 2:
            for elemento in datos:
                if elemento["marca"] == marca:
                    nombre = elemento["nombre"]
                    l.append(nombre)

    with open(nombre_archivo, "w") as file: 
                for item in l:
                    file.write(f"{item}\n")


def csv_menos_de_dos_unidades(datos:list, nombre_archivo:str):
    cantidad=obtener_cantidad_por_marca(datos)
    mostrar_insumos_menos_de_dos_unidades(datos, cantidad, nombre_archivo)





def menu():
    import os
    while True:
        opcion_1 = False
        opcion_7 = False
        opcion_10 = False
        os.system("cls")
        print("1. Cargar datos desde archivo")
        print("2. Mostrar cantidad por marca")
        print("3. Mostrar insumos por marca")
        print("4. Mostrar insumos por característica")
        print("5. Listar insumos ordenados")
        print("6. Realizar compra")
        print("7. Filtrar productos por palabra clave")
        print("8. Mostrar productos filtrados")
        print("9. Actualizar precios")
        print("10. Agregar productos")
        print("11. Subir nuevos productos a archivo")
        print("12. Stock por marca")
        print("13. Crear un csv listado con el nombre de producto y el stock de aquellos productos que tengan 2 o menos unidades de stock.")
        print("14. Salir")
        opcion = int(input("ingrese opcion:"))

        if opcion == 1:
            archivo=input("ingrese el nombre del archivo al que le gustaria cargar los datos: ")
            datos = leer_datos_csv(archivo)

            opcion_1 = True
        elif opcion == 2:
            if (opcion_1 == False):
                print("primero carga los datos")
            else:
                cantidad_por_marca = obtener_cantidad_por_marca(datos)
                mostrar_cantidad_por_marca(cantidad_por_marca)
        elif opcion == 3:
            if opcion_1 == False:
                print("primero carga los datos")
            else:
                mostrar_insumos_por_marca(datos)
        elif opcion == 4:
            if opcion_1 == False:
                print("primero carga los datos")
            else:
                caracteristica = input("Ingrese una característica: ")
                mostrar_insumos_con_caracteristica(datos, datos, caracteristica)
        elif opcion == 5:
            if opcion_1 == False:
                print("primero carga los datos")
            else:
                ordenar_lista_por_marca_y_precio(datos)
                mostrar_insumos_ordenados_por_marca_y_precio(datos)
        elif opcion == 6:
            if opcion_1 == False:
                print("primero carga los datos")
            else:
                realizar_compra(datos)
        elif opcion == 7:
            if opcion_1 == False:
                print("primero carga los datos")
            else:
                list=[]
                productos_filtrados = filtrar_productos_por_palabra_clave(datos, "Alimento")
                list.append(productos_filtrados)
                archivo = input("ingrese el archivo json al que lo va a guardar: ")
                guardar_datos(list, archivo)
                opcion_7 = False
                print("productos filtrados, para verlos, presione la opcion 8")
        elif opcion == 8:
            if opcion_7 == False:
                print("primero carga los datos")
            else:
                for i in list:
                    print(i)
        elif opcion == 9:
            if opcion_1 == False:
                print("primero carga los datos")
            else:
                aumento(datos)
        elif opcion == 10:
            if opcion_1 == False:
                print("primero carga los datos")
            else:
                list = agregar_elemento("insumos.csv")
                opcion_10 == False
        elif opcion == 11:
            if opcion_10 == False:
                print("primero carga los datos")
            else:
                llenar_archivo(list)
        elif opcion == 12:
            mostrar_stock_marca(datos, "marca", "marca")
        elif opcion == 13:
            archivo=input("ingrese el nombre del archivo al que le gustaria cargar los datos: ")
            csv_menos_de_dos_unidades(datos, archivo)
        elif opcion == 14:
            break
        os.system("pause")