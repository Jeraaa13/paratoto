cont = 0
acu_cantidad_unidades_jabon = 0
flag_barbijos = True
flag_mas_unidades = True

while cont < 5:
    producto_sanitario = input("Ingrese barbijo, jabon o alcohol: ")
    while producto_sanitario != "barbijo" and producto_sanitario != "jabon" and producto_sanitario != "alcohol":
        producto_sanitario = input("ERROR, reingrese barbijo, jabon o alcohol: ")
    precio_producto = input("Ingrese el precio del producto: ")
    precio_producto = int(precio_producto)
    while precio_producto < 100 and precio_producto > 300:
        precio_producto = input("ERROR, reingrese el precio del producto: ")
        precio_producto = int(precio_producto)
    cantidad_unidades = input("Ingrese la cantidad de unidades: ")
    cantidad_unidades = int(cantidad_unidades)
    while cantidad_unidades < 1 and cantidad_unidades > 1000:
        cantidad_unidades = input("ERROR, reingrese la cantidad de unidades: ")
        cantidad_unidades = int(cantidad_unidades)
    marca = input("Ingrese la marca: ")
    fabricante = input("Ingrese el fabricante: ")

    if producto_sanitario == "barbijo":
        if flag_barbijos or precio_producto > barbijo_mas_caro:
            barbijo_mas_caro = precio_producto
            barbijo_mas_caro_unidades = cantidad_unidades
            barbijo_mas_caro_fabricante = fabricante
            flag_barbijos = False
    
    if flag_mas_unidades or cantidad_unidades > producto_mas_unidades:
        producto_mas_unidades = cantidad_unidades
        fabricante_mas_unidades = fabricante
    
    if producto_sanitario == "jabon":
        acu_cantidad_unidades_jabon += cantidad_unidades

    cont += 1

print("El mas caro de los barbijos tiene un cantidad de: ", barbijo_mas_caro_unidades, " y es fabricado por: ", barbijo_mas_caro_fabricante)
print("El item con mas unidades tiene: ", producto_mas_unidades, "y el fabricante es: ", fabricante_mas_unidades)
print("La cantidad de jabones es: ", acu_cantidad_unidades_jabon)