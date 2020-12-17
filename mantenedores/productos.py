from typing import Dict, List
from os.path import dirname, join, getsize
from dto.classes import Producto
from mantenedores.vendedores import obtener_hashing

LONGITUD_REGISTRO = 64

productos_path = join(dirname(__file__), '../db/PRODUCTOS.dat')


def obtener_uno(codigo: int) -> Producto or None:
    return Producto(1, "PRODUCTO", 2300, 120)


def obtener_todos() -> List[Producto]:
    return []


def listar():
    file = open(productos_path, 'r')
    while file.tell() < getsize(productos_path):
        registro_actual = file.read(LONGITUD_REGISTRO)
        if '\x00' not in registro_actual:  # Registro no vacio
            codigo = registro_actual[0:5].strip()
            nombre = registro_actual[5:50].strip()
            precio = registro_actual[50:56].strip()
            stock = registro_actual[56:59].strip()
            print('Producto numero ' + str(int(file.tell() / LONGITUD_REGISTRO)) +
                  ' = Codigo: ' + codigo + ' - Nombre: ' + nombre + ' - Precio: ' + precio + 'Stock: ' + stock)
    file.close()


def agregar():
    pass


def eliminar():
    pass


def modificar(codigo: int, nueva_data: Dict[str, any]):
    pass
