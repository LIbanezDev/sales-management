"""
 Data Transfer Objects
 Estas clases tienen el objetivo de facilitar el manejo de los datos contenidos en los archivos,
 en lugar de manejar un substring del registro se pasa completo el registro al constructor de la clase y este se encarga
 de mapear cada substring a un atributo del objeto, por ejemplo codigo en el registro es registro[0:5], pero para evitar este manejo el constructor lo convierte
 iguala a un atributo de objeto, pasando a ser Instancia.codigo
"""


class DetalleVenta:
    def __init__(self, registro: str):  # num_boleta;codigo_producto;cantidad
        registro_arr = registro.strip().split(';')
        self.num_boleta = int(registro_arr[0])
        self.cod_producto = int(registro_arr[1])
        self.cantidad = int(registro_arr[2])


class EncabezadoVenta:
    def __init__(self, registro: str):  # num_boleta;fecha;codigo_vendedor;estado
        registro_arr = registro.strip().split(';')
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
