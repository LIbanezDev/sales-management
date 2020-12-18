from os.path import dirname, join, getsize
from typing import Dict

from mantenedores.compartidos import encontrar_espacio, obtener_uno

LONGITUD_REGISTRO = 35

vendedores_path = join(dirname(__file__), '../db/VENDEDORES.dat')


def agregar():
    codigo = input('Ingrese codigo de vendedor: ')
    posicion = encontrar_espacio(codigo, 'vendedores', vendedores_path)
    if posicion == -1:
        print('Vendedor ya ha sido agregado.')
    else:
        FILE = open(vendedores_path, 'r+')
        nombre = input('Ingrese nombre de vendedor: ')[0:30]
        FILE.seek(posicion)
        FILE.write(codigo.zfill(5) + nombre.ljust(30))
        FILE.close()


def modificar(codigo: int, nueva_data: Dict[str, any]):
    pass


def consultar():
    codigo = input('Ingrese codigo de producto a buscar: ')
    vendedor = obtener_uno(codigo, 'vendedores', vendedores_path)
    if vendedor is None:
        print('Vendedor no existe.')
    else:
        nombre = vendedor[5:30].strip()
        print('Nombre de vendedor: ' + nombre)


def eliminar():
    pass


def listar():
    file = open(vendedores_path, 'r')
    archivo_vacio = True
    while file.tell() < getsize(vendedores_path):
        registro_actual = file.read(LONGITUD_REGISTRO)
        codigo = registro_actual[0:5].strip()
        if codigo != '00000':  # Registro no vacio
            nombre = registro_actual[5:30].strip()
            print('Vendedor numero ' + str(int(file.tell() / LONGITUD_REGISTRO)) + ' = Codigo: ' + codigo + ' - Nombre: ' + nombre)
    if archivo_vacio:
        print('El archivo no tiene productos aun. Enter para continuar...')
    else:
        print('Fin del listado. Enter para continuar...')
    file.close()
