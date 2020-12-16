from typing import Dict, List

from dto.classes import Vendedor


def obtener_uno(codigo: int) -> Vendedor or None:
    return Vendedor(12345, "Lucas con 30 caracteres".zfill(30))


def obtener_todos() -> List[Vendedor]:
    return []


def agregar():
    pass


def eliminar():
    pass


def modificar(codigo: int, nueva_data: Dict[str, any]):
    pass
