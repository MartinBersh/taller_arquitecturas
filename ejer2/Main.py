from ejer2 import Producto, Inventario

if __name__ == "__main__":
    inventario = Inventario()

    producto1 = Producto("001", "Camiseta", 15.99, 50)
    producto2 = Producto("002", "Pantalón", 29.99, 30)

    inventario.agregar_producto(producto1)
    inventario.agregar_producto(producto2)

    inventario.mostrar_inventario()

    inventario.actualizar_inventario("001", -10)

    inventario.mostrar_inventario()

    inventario.eliminar_producto("002")

    inventario.mostrar_inventario()
