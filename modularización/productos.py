if __name__ == "__main__":
    pass
else:

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



