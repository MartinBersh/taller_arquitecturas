class Inventario:
    def __init__(self):
        self.productos = {}

    def agregar_producto(self, producto):
        self.productos[producto.id_producto] = producto

    def eliminar_producto(self, id_producto):
        if id_producto in self.productos:
            del self.productos[id_producto]
        else:
            print("Producto no encontrado en el inventario")

    def obtener_producto(self, id_producto):
        if id_producto in self.productos:
            return self.productos[id_producto]
        else:
            print("Producto no encontrado en el inventario")

    def actualizar_inventario(self, id_producto, cantidad):
        if id_producto in self.productos:
            self.productos[id_producto].cantidad_disponible += cantidad
        else:
            print("Producto no encontrado en el inventario")

    def mostrar_inventario(self):
        print("Inventario:")
        for producto_id, producto in self.productos.items():
            print(producto)