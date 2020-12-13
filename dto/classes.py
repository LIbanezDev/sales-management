class Vendedor:
    def __init__(self, codigo: int, nombre: str):
        self.codigo = codigo
        self.nombre = nombre


class DetalleVenta:
    def __init__(self, num_boleta: int, cod_producto: int, cantidad: int):
        self.numero_boleta = num_boleta
        self.cod_producto = cod_producto
        self.cantidad = cantidad


class EncabezadoVenta:
    def __init__(self, num_boleta: int, fecha: str, cod_vendedor: int, estado: str):
        self.num_boleta = num_boleta
        self.fecha = fecha
        self.cod_vendedor = cod_vendedor
        self.estado = estado


class Producto:
    def __init__(self, codigo: int, nombre: str, precio: int, stock: int):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        self.stock = stock
