
import json


lista = []

with open("insumos.csv", "r", encoding="utf-8") as file:
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

js = json.dumps(lista, indent=2)

with open("insumos.json", "w") as file:
    file.write(js)

with open("insumos.json", "r") as file:
    datos=json.load(file)

print(datos)


# cantidad_por_marca = {}  

# for elemento in datos:
#     marca = elemento['marca'] 
    
#     cantidad = cantidad_por_marca.get(marca, 0)
#     cantidad += 1
#     cantidad_por_marca[marca] = cantidad

# for marca in cantidad_por_marca:
#     cantidad = cantidad_por_marca[marca]
#     print(f"Marca: {marca} - Cantidad: {cantidad}")



# # Muestra, para cada marca, el nombre y precio de los insumos correspondientes.

# insumos_por_marca = {}

# for elemento in datos:
#     marca = elemento['marca']
#     nombre = elemento['nombre']
#     precio = elemento['precio']

#     insumos_por_marca [elemento['marca']] = insumos_por_marca.get(elemento['marca'], [])
#     insumos_por_marca[elemento['marca']].append((elemento['nombre'], elemento['precio']))

# for elemento['marca'] in insumos_por_marca:
#     print("Marca:", elemento['marca'])

#     insumos = insumos_por_marca[elemento['marca']]
#     for insumo in insumos:
#         nombre = insumo[0]
#         precio = insumo[1]
#         print("  Nombre:", nombre)
#         print("  Precio:", precio)

# ####################################

# caracteristica = input("Ingrese una característica: ")

# insumos_con_caracteristica = []

# for insumo in lista:
#     caracteristicas = insumo["caracteristicas"]
#     if caracteristica in insumo["caracteristicas"]:
#         insumos_con_caracteristica.append(insumo)

# if insumos_con_caracteristica:
#     print(f"Insumos con la característica '{caracteristica}':")
#     for insumo in insumos_con_caracteristica:
#         print("ID:", insumo["id"])
#         print("Nombre:", insumo["nombre"])
#         print("Marca:", insumo["marca"])
#         print("Precio:", insumo["precio"])
#         print("Características:", insumo["caracteristicas"])
#         print("")
# else:
#     print(f"No se encontraron insumos con la característica '{caracteristica}'.")

# # Muestra el ID, descripción, precio, marca
# # y la primera característica de todos los insumo, ordenados por
# # marca de forma ascendente (A-Z) y, ante marcas iguales, por precio
# # descendente.

# def ordenar_lista(lista):
#     for i in range(len(lista) - 1):
#         for j in range(i + 1, len(lista)):
#             if lista[i]['marca'] > lista[j]['marca']:
#                 lista[i], lista[j] = lista[j], lista[i]
#             elif lista[i]['marca'] == lista[j]['marca'] and lista[i]['precio'] < lista[j]['precio']:
#                 lista[i], lista[j] = lista[j], lista[i]

# ordenar_lista(lista)

# print("Insumos ordenados por marca y precio:")

# for insumo in lista:
#     print("ID:", insumo['id'])
#     print("Descripción:", insumo['nombre'])
#     print("Precio:", insumo['precio'])
#     print("Marca:", insumo['marca'])
#     caracteristicas = insumo['caracteristicas'].split("~")
#     if caracteristicas:
#         print("Primera característica:", caracteristicas[0])
#     print()


# compra = []
# total = 0

# while True:
#     marca = input("Ingrese la marca de los insumo que desea comprar (o 'Salir' para finalizar): ")
#     if marca.lower() == "salir":
#         break

#     print(f"insumo disponibles de la marca {marca}:")
#     for producto in datos:
#         if producto["marca"] == marca:
#             print("Descripción:", producto["nombre"])
#             print("Precio:", producto["precio"])
#             print()

#     producto_nombre = input("Ingrese el ID del producto que desea comprar (o 'Salir' para finalizar la compra): ")
#     if producto_nombre.lower() == "salir":
#         break

#     cantidad = int(input("Ingrese la cantidad deseada: "))

#     producto_encontrado = False
#     subtotal = 0

#     for producto in datos:
#         if producto["nombre"] == producto_nombre:
#             producto_encontrado = True
#             producto["precio"] = float(producto["precio"].replace("$", ""))
#             subtotal = producto["precio"] * cantidad
#             total += subtotal
#             compra.append((producto, cantidad, subtotal))
#             break
#         elif producto_encontrado:
#             print("El producto ingresado no es válido. Intente nuevamente.")
#             continue

#     print(f"Se agregó {cantidad} {producto['nombre']} a la compra.")

# print("=== COMPRA FINALIZADA ===")
# print("Detalles de la compra:")
# for producto, cantidad, subtotal in compra:
#     print(f"{cantidad} {producto['nombre']} - Subtotal: {subtotal}")
# print("Total de la compra:", total)

# with open("factura_de_la_compra.txt", "w") as file:

#     file.write("""Cantidad / Producto / Subtotal
    
#     """)

#     for producto, cantidad, subtotal in compra:
#         file.write(f"""{cantidad} / {producto['nombre']} / {subtotal}\n
        
#         Total: {total}
#         """)


# productos_alimento = []

# for producto in datos:
#     if "Alimento" in producto["nombre"]:
#         productos_alimento.append(producto)


# datos2 = {"productos": productos_alimento}

# with open("productos_alimento.json", "w") as file:
#     json.dump(datos2, file, indent=2)


# with open("productos_alimento.json", "r") as file:
#     dd = json.load(file)

# productos_alimento = dd["productos"]


# for producto in productos_alimento:
#     print("Nombre:", producto["nombre"])
#     print("Marca:", producto["marca"])
#     print("Precio:", producto["precio"])
#     print()


# def aplicar_aumento(lista):
#     for producto in lista:
#         producto["precio"] = producto["precio"].replace("($ | [A-Z])", "")
#         producto["precio"] = float(producto["precio"])
#         precio_actualizado = producto["precio"] * 1.084
#     return producto

# productos_actualizados = list(map(aplicar_aumento,datos))

# print(productos_actualizados)
# def aumento(producto):
#     for producto in datos:
#         pr=producto["precio"]
#         pr=float(pr.strip("$").replace(",",".").replace("[A-Z]", ""))
#         aumento=pr+(pr*0.084)
#         producto["precio"]=pr
#     for producto in datos:
#         print(producto["marca"])
#         print(producto["nombre"])
#         print(producto["precio"])
#         print("-------------")

# aumento()