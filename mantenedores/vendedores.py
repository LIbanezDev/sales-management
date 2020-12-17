from typing import Dict, List
from os.path import dirname, join, getsize
from dto.classes import Vendedor

LONGITUD_REGISTRO = 35

dirname = dirname(__file__)

vendedores_path = join(dirname, '../db/VENDEDORES.dat')


def obtener_hashing(codigo: str) -> int:
    posicion = 0
    for digito in codigo:
        posicion += int(digito)
    return posicion - 1


def validar_existencia() -> bool:
    return False


def obtener_uno(codigo: int) -> Vendedor or None:
    return Vendedor(12345, "Lucas con 30 caracteres".zfill(30))


def listar():
    file = open(vendedores_path, 'r')
    contador = 0
    while file.tell() < getsize(vendedores_path):
        registro_actual = file.read(LONGITUD_REGISTRO)
        codigo = registro_actual[0:5].strip()
        nombre = registro_actual[5:30].strip()
        if not (len(codigo) == 5):  # Registro no vacio
            print('Vendedor numero ' + str(int(contador + 1)) + ' = Codigo: ' + codigo + ' - Nombre: ' + nombre)
        contador += 1
    file.close()


def agregar():
    codigo = input('Ingrese codigo de vendedor: ')[0:5]
    existe = validar_existencia()
    if existe:
        print('Vendedor ya ha sido agregado.')
    else:
        nombre = input('Ingrese nombre de vendedor: ')[0:30]
        f = open(vendedores_path, 'r+')
        posicion = obtener_hashing(codigo)
        f.seek(LONGITUD_REGISTRO * posicion)
        f.write(codigo.ljust(5) + nombre.ljust(30))
        f.close()


def eliminar():
    pass


def modificar(codigo: int, nueva_data: Dict[str, any]):
    pass
