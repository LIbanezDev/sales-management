from os.path import dirname, join, getsize
from typing import Dict

from dto.classes import Vendedor

LONGITUD_REGISTRO = 35

vendedores_path = join(dirname(__file__), '../db/VENDEDORES.dat')


def obtener_hashing(codigo: str) -> int:
    posicion = 0
    for digito in codigo:
        posicion += int(digito)
    return LONGITUD_REGISTRO * (posicion - 1)


def obtener_posicion(codigo: str) -> int:
    file = open(vendedores_path, 'r')
    posicion = obtener_hashing(codigo)
    file.seek(posicion * LONGITUD_REGISTRO)
    registro = file.read(LONGITUD_REGISTRO)
    if '\x00' in registro or registro == '':  # Registro vacio
        file.close()
        return posicion
    if codigo == registro[0:5].strip():  # Registro ya insertado
        file.close()
        return -1


"""
def Buscar(ID):
    Posicion = Hashing(ID)
    Archivo.seek(Posicion)
    Registro = Archivo.read(LargoRegistro)
    if int(ID) == int(Registro[0:5]):
        return Posicion
    else:
        Posicion = 45 * LargoRegistro
        Archivo.seek(Posicion)
        Registro = Archivo.read(LargoRegistro)
        while Registro != "" and int(ID) != int(Registro[0:5]):
            Registro = Archivo.read(LargoRegistro)
            Posicion = Posicion + LargoRegistro                
        if Registro == "":
            return -1
        else:
            return Posicion

def EncontrarEspacio(ID):
    Posicion = Hashing(ID)
    Archivo.seek(Posicion)
    Registro = Archivo.read(LargoRegistro)
    if Registro[0:5] == "00000":
        return Posicion
    else:
        Posicion = 45 * LargoRegistro
        Archivo.seek(Posicion)
        Registro = Archivo.read(LargoRegistro)
        while Registro != "" and Registro[0:5] != "00000":
            Registro = Archivo.read(LargoRegistro)
            Posicion = Posicion +  LargoRegistro 
        return Posicion
"""


def obtener_uno(codigo: int) -> Vendedor or None:
    return Vendedor(12345, "Lucas con 30 caracteres".zfill(30))


def listar():
    file = open(vendedores_path, 'r')
    while file.tell() < getsize(vendedores_path):
        registro_actual = file.read(LONGITUD_REGISTRO)
        if '\x00' not in registro_actual:  # Registro no vacio
            codigo = registro_actual[0:5].strip()  # Remove NULL
            nombre = registro_actual[5:30].strip()
            print('Vendedor numero ' + str(int(file.tell() / LONGITUD_REGISTRO)) + ' = Codigo: ' + codigo + ' - Nombre: ' + nombre)
    file.close()


def agregar():
    codigo = input('Ingrese codigo de vendedor: ')[0:5]
    posicion = obtener_posicion(codigo)
    if posicion == -1:
        print('Vendedor ya ha sido agregado.')
    else:
        nombre = input('Ingrese nombre de vendedor: ')[0:30]
        f = open(vendedores_path, 'r+')
        f.seek(posicion)
        f.write(codigo.ljust(5) + nombre.ljust(30))
        f.close()


def eliminar():
    pass


def modificar(codigo: int, nueva_data: Dict[str, any]):
    pass
