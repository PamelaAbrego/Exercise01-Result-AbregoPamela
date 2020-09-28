"""Porgrama que introduce registros en una lista de diccionarios, pide el número de registros que se desean introducir,
y llena cada registro con los elementos: nombreCliente, nombreProducto y costoProducto. Luego, cada registro lo introduce
en una lista llamada listaRegistro. Por último, se imprime el costo total de los registros introducidos y el reporte de
cada registro introducido."""

listaPedidos = []
continuar = True
costoTotal = 0

while continuar is True:
    nomreCliente = input("Ingrese el nombre del cliente: ")
    nombreProducto = input("Ingrese nombre del producto: ")
    costoProducto = float(input("Ingrese el costo del producto($0.00): "))
    pedido = dict(cliente=nomreCliente, producto=nombreProducto, costo=costoProducto)
    listaPedidos.append(pedido)
    costoTotal += costoProducto
    continuar = input("¿Desea introducir otro pedido? Introduzca 'sí' o 'no': ")
    if continuar == "sí":
        continuar = True
    else:
        continuar = False

print("El costo total de los pedidos es de " + str(costoTotal) + " dólares.")

print("El reporte de los pedidos ingresados es: ")
for pedidoIngresado in listaPedidos:
    print(pedidoIngresado)
