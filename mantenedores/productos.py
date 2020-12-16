from typing import Dict, List

from dto.classes import Producto


def obtener_uno(codigo: int) -> Producto or None:
    return Producto(1, "PRODUCTO", 2300, 120)


def obtener_todos() -> List[Producto]:
    return []


def agregar():
    pass


def eliminar():
    pass


def modificar(codigo: int, nueva_data: Dict[str, any]):
    pass
