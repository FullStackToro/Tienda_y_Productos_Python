from modularización.tienda import *


if __name__ == "__main__":

    producto1 = Producto("Mesa", 450000, 'comedor')
    producto2 = Producto("Silla", 75000, "comedor")
    producto3 = Producto("Escritorio", 150000, "oficina")
    producto4 = Producto("Repisa", 120000, "oficina")
    producto5 = Producto("Bares", 350000, "comedor")
    producto1.print_info()

    tienda1 = Tienda("Pallabelia")
    tienda1.add_product(producto1)
    tienda1.add_product(producto2)
    tienda1.add_product(producto3)
    tienda1.add_product(producto4)
    tienda1.add_product(producto5)

    tienda1.ver_inventario(tienda1)

    tienda1.inflation(20)
    tienda1.ver_inventario(tienda1)

    tienda1.set_clearance("oficina", 50)
    tienda1.ver_inventario(tienda1)

    tienda1.sell_product(1)
    tienda1.ver_inventario(tienda1)


