from os.path import dirname, join, getsize

from dto.classes import Producto
from mantenedores.compartidos import encontrar_espacio, obtener_uno

LONGITUD_REGISTRO = 64

productos_path = join(dirname(__file__), '../db/PRODUCTOS.dat')


def restar_stock(codigo: str, cantidad: int):
    [posicion, registro] = obtener_uno(codigo, 'productos')
    stock_actual = int(registro[61:64])
    nuevo_stock = stock_actual - cantidad
    registro_editado = registro[0:61] + str(nuevo_stock).zfill(3)
    FILE = open(productos_path, 'r+')
    FILE.seek(posicion)
    FILE.write(registro_editado)
    FILE.close()


def agregar():
    codigo = input('Ingrese codigo de producto: ')
    posicion = encontrar_espacio(codigo, 'productos')
    if posicion == -1:
        print('Producto ya ha sido agregado.')
    else:
        print('Ingrese los datos restantes del producto.')
        nombre = input('Nombre: ')[0:50]
        precio = input('Precio: ')[0:6]
        stock = input('Stock: ')[0:3]
        FILE = open(productos_path, 'r+')
        FILE.seek(posicion)
        FILE.write(codigo.zfill(5) + nombre.ljust(50) + precio.zfill(6) + stock.zfill(3))
        FILE.close()


def modificar():
    codigo = input('Ingrese codigo de producto a modificar: ')
    [posicion, registro] = obtener_uno(codigo, 'productos')
    if registro is None:
        print('Producto no existe, no se puede modificar.')
    else:
        print('Modificando en la posicion', posicion)
        producto = Producto(registro)
        print('Nombre:', producto.nombre, '- Precio:', producto.precio, '- Stock:', producto.stock)
        print('-- Nuevos datos --')
        nombre = input('Nombre: ')
        precio = input('Precio: ')
        stock = input('Stock: ')
        FILE = open(productos_path, 'r+')
        FILE.seek(posicion)
        FILE.write(str(codigo).zfill(5) + nombre.ljust(50) + precio.zfill(6) + stock.zfill(3))
        FILE.close()


def consultar():
    codigo = input('Ingrese codigo de producto: ')
    [pos, producto] = obtener_uno(codigo, 'productos')
    if producto is None:
        print('Producto no existe.')
    else:
        nombre = producto[5:55].strip()
        precio = int(producto[55:61])
        stock = int(producto[61:64])
        print('Nombre: ' + nombre + ' - Precio:', precio, ' - Stock:', stock)


def eliminar():
    codigo = input('Ingrese codigo de producto: ')
    [pos, producto] = obtener_uno(codigo, 'productos')
    if producto is None:
        print('Producto no existe.')
    else:
        print('Eliminando producto.')


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
