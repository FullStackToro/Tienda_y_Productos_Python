print(__name__)
if __name__ == "__main__":
    print("El archivo esta siendo ejecutado directamente")


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

        def ver_inventario(self):
            for i in range(len(tienda1.producto)):
                print("*" * 50, "\nNombre del Producto:", tienda1.producto[i].name, "\nPrecio:",
                      tienda1.producto[i].precio, "\nCategoria:", tienda1.producto[i].categoria, "\n")

    class Producto:

        def __init__(self, name, precio, categoria):
            self.name = name
            self.precio = precio
            self.categoria = categoria

        def update_price(self, porcentaje_cambio, se_incrementa):
            if se_incrementa:
                self.precio = int(self.precio * (1 + porcentaje_cambio * 1 / 100))
            elif not se_incrementa:
                self.precio = int(self.precio * (1 - porcentaje_cambio * 1 / 100))
            else:
                print('Debe ingresar True o False en el segundo parámetro')

        def print_info(self):
            print('\nProducto:', self.name, '\nCategoria:', self.categoria, '\nPrecio:', self.precio, "\n", "-" * 50)

    p1 = Producto("producto1", 100, "categoria1")
    p2 = Producto("producto2", 200, "categoria2")
    p3 = Producto("producto3", 300, "categoria3")
    p4 = Producto("producto4", 1000, "categoria1")

    tienda1 = Tienda("tienda1")
    tienda1.add_product(p1)
    tienda1.add_product(p2)
    tienda1.add_product(p3)
    tienda1.add_product(p4)

    tienda1.ver_inventario()
    print("ejercicio1")
    tienda1.inflation(10)
    tienda1.ver_inventario()
    print("ejercicio2")
    tienda1.set_clearance("categoria1", 10)
    tienda1.ver_inventario()

    print("ejercicio3")
    tienda1.sell_product(3)
    tienda1.ver_inventario()
else:
    print(". El archivo se llama: ", __name__)
