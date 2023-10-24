class Producto:
    def __init__(self, codigo, nombre, precio):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio

class Cliente:
    def __init__(self, id, nombre, email):
        self.id = id
        self.nombre = nombre
        self.email = email

class Venta:
    def __init__(self, producto, cliente, cantidad):
        self.producto = producto
        self.cliente = cliente
        self.cantidad = cantidad

productos = []
clientes = []
ventas = []

def registrar_producto():
    codigo = int(input("Ingrese el código del producto: "))
    nombre = input("Ingrese el nombre del producto: ")
    precio = float(input("Ingrese el precio del producto: "))
    producto = Producto(codigo, nombre, precio)
    productos.append(producto)

def registrar_cliente():
    id = int(input("Ingrese el ID del cliente: "))
    nombre = input("Ingrese el nombre del cliente: ")
    email = input("Ingrese el correo electrónico del cliente: ")
    cliente = Cliente(id, nombre, email)
    clientes.append(cliente)

def realizar_venta():
    print("Productos disponibles:")
    for idx, producto in enumerate(productos):
        print(f"{idx + 1}. {producto.nombre}")

    producto_idx = int(input("Seleccione el número del producto a vender: ")) - 1
    cantidad = int(input("Ingrese la cantidad a vender: "))
    cliente_idx = int(input("Ingrese el número de cliente: ")) - 1

    venta = Venta(productos[producto_idx], clientes[cliente_idx], cantidad)
    ventas.append(venta)
    print("Venta registrada correctamente.")

# Menú principal
while True:
    print("\n1. Registrar Producto")
    print("2. Registrar Cliente")
    print("3. Realizar Venta")
    print("4. Mostrar Ventas")
    print("5. Salir")
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        registrar_producto()
    elif opcion == "2":
        registrar_cliente()
    elif opcion == "3":
        realizar_venta()
    elif opcion == "4":
        print("\nVentas realizadas:")
        for venta in ventas:
            print(venta)
    elif opcion == "5":
        print("¡Hasta luego!")
        break
    else:
        print("Opción inválida. Intente nuevamente.")

