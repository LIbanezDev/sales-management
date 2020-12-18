from os.path import dirname, join, getsize
from typing import Dict

from mantenedores.compartidos import encontrar_espacio, obtener_uno

LONGITUD_REGISTRO = 64

productos_path = join(dirname(__file__), '../db/PRODUCTOS.dat')


def agregar():
    codigo = input('Ingrese codigo de producto: ')
    posicion = encontrar_espacio(codigo, 'productos')
    if posicion == -1:
        print('Producto ya ha sido agregado.')
    else:
        FILE = open(productos_path, 'r+')
        print('Ingrese los datos restantes del producto.')
        nombre = input('Nombre: ')[0:50]
        precio = input('Precio: ')[0:6]
        stock = input('Stock: ')[0:3]
        FILE.seek(posicion)
        FILE.write(codigo.zfill(5) + nombre.ljust(50) + precio.zfill(6) + stock.zfill(3))
        FILE.close()


def modificar(codigo: int, nueva_data: Dict[str, any]):
    pass


def consultar():
    codigo = input('Ingrese codigo de producto: ')
    producto = obtener_uno(codigo, 'productos')
    if producto is None:
        print('Producto no existe.')
    else:
        nombre = producto[5:55].strip()
        precio = producto[55:61].strip()
        stock = producto[61:64].strip()
        print('Nombre: ' + nombre + ' - Precio:', int(precio), ' - Stock:', int(stock))


def eliminar():
    pass


def listar():
    file = open(productos_path, 'r')
    archivo_vacio = True
    while file.tell() < getsize(productos_path):
        registro_actual = file.read(LONGITUD_REGISTRO)
        codigo = registro_actual[0:5].strip()
        if codigo != '00000':  # Registro no vacio
            nombre = registro_actual[5:50].strip()
            precio = registro_actual[50:56].strip()
            stock = registro_actual[56:59].strip()
            archivo_vacio = False
            print('Producto numero ' + str(int(file.tell() / LONGITUD_REGISTRO)) +
                  ' = Codigo: ' + codigo + ' - Nombre: ' + nombre + ' - Precio: ' + precio + 'Stock: ' + stock)
    if archivo_vacio:
        print('El archivo no tiene productos aun. Enter para continuar...')
    else:
        print('Fin del listado. Enter para continuar...')
    file.close()
