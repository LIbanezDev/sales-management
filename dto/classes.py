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
    def __init__(self, registro: str):
        self.codigo = int(registro[0:5])
        self.nombre = registro[5:55].strip()
        self.precio = int(registro[55:61])
        self.stock = int(registro[61:64])
