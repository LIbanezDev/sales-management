class DetalleVenta:
    def __init__(self, registro: str):
        registro_arr = registro.split(';')
        self.numero_boleta = int(registro_arr[0])
        self.cod_producto = int(registro_arr[1])
        self.cantidad = int(registro_arr[2])


class EncabezadoVenta:
    def __init__(self, registro: str):  # 00001;18/01/2013;12345;V
        registro_arr = registro.split(';')
        self.num_boleta = int(registro_arr[0])
        self.fecha = registro_arr[1]
        self.cod_vendedor = int(registro_arr[2])
        self.estado = registro_arr[3]


class Vendedor:
    def __init__(self, registro: str):
        self.codigo = int(registro[0:5])
        self.nombre = registro[5:30].strip()


class Producto:
    def __init__(self, registro: str):
        self.codigo = int(registro[0:5])
        self.nombre = registro[5:55].strip()
        self.precio = int(registro[55:61])
        self.stock = int(registro[61:64])
