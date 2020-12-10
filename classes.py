class Vendedor:
    def __init__(self, codigo: int, nombre: str):
        self.codigo = codigo
        self.nombre = nombre


class Producto:
    def __init__(self, codigo: int, nombre: str, precio: int, stock: int):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        self.stock = stock
