from typing import Dict, List
from os.path import dirname, join, getsize
from dto.classes import Producto
from mantenedores.vendedores import obtener_hashing

LONGITUD_REGISTRO = 64

dirname = dirname(__file__)

productos_path = join(dirname, '../db/PRODUCTOS.dat')


def obtener_uno(codigo: int) -> Producto or None:
    return Producto(1, "PRODUCTO", 2300, 120)


def obtener_todos() -> List[Producto]:
    return []


def listar():
    file = open(productos_path, 'r')
    contador = 0
    while file.tell() < getsize(productos_path):
        registro_actual = file.read(LONGITUD_REGISTRO)
        codigo = registro_actual[0:5].strip()
        nombre = registro_actual[5:50].strip()
        precio = registro_actual[50:56].strip()
        stock = registro_actual[56:59].strip()
        if not (len(codigo) == 5):  # Registro no vacio
            print('Producto numero ' + str(int(contador + 1)) + ' = Codigo: ' + codigo + ' - Nombre: ' + nombre + ' - Precio: ' + precio + 'Stock: ' + stock)
        contador += 1
    file.close()


def agregar():
    pass


def eliminar():
    pass


def modificar(codigo: int, nueva_data: Dict[str, any]):
    pass
