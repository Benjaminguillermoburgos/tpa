class Producto:
    def __init__(self, nombre, cantidad):
        self.nombre = nombre
        self.cantidad = cantidad

class Inventario:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def buscar_producto(self, nombre):
        for producto in self.productos:
            if producto.nombre == nombre:
                return producto
        return None

    def actualizar_cantidad(self, nombre, cantidad):
        producto = self.buscar_producto(nombre)
        if producto:
            producto.cantidad += cantidad
        else:
            print("El producto no existe en el inventario.")

    def mostrar_inventario(self):
        print("Inventario:")
        for producto in self.productos:
            print(f"Producto: {producto.nombre}, Cantidad: {producto.cantidad}")


# Ejemplo de uso
inventario = Inventario()

# Agregar productos al inventario
inventario.agregar_producto(Producto("Manzanas", 10))
inventario.agregar_producto(Producto("Naranjas", 5))
inventario.agregar_producto(Producto("Plátanos", 7))

# Actualizar la cantidad de un producto
inventario.actualizar_cantidad("Manzanas", 3)

# Mostrar el inventario
inventario.mostrar_inventario()