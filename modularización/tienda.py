from modularización.productos import *

if __name__ == "__main__":
    pass
else:

    class Tienda:
        def __init__(self, name):
            self.name = name
            self.producto = [Producto("", 0, "")]

        def add_product(self, new_product):
            self.producto.append(Producto(new_product.name, new_product.precio, new_product.categoria))
            if self.producto[0].name == "" and self.producto[0].precio == 0 and self.producto[0].categoria == "":
                self.producto.pop(0)

        def sell_product(self, id):
            print("-" * 50, "\n", "Se ha vendido el producto:", self.producto[id - 1].name)
            self.producto[id - 1].print_info()
            self.producto.pop(id - 1)

        def inflation(self, percent_increase):
            for x in range(len(self.producto)):
                self.producto[x].update_price(percent_increase, True)

        def set_clearance(self, category, percent_discount):
            for x in range(len(self.producto)):
                if self.producto[x].categoria == category:
                    self.producto[x].update_price(percent_discount, False)

        def ver_inventario(self, tienda1):
            for i in range(len(tienda1.producto)):
                print("*" * 50, "\nNombre del Producto:", tienda1.producto[i].name, "\nPrecio:",
                      tienda1.producto[i].precio, "\nCategoria:", tienda1.producto[i].categoria, "\n")



