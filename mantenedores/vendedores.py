import os.path

import dto
import mantenedores.compartidos
import mantenedores.ventas

LONGITUD_REGISTRO = 35

vendedores_path = os.path.join(os.path.dirname(__file__), '../db/VENDEDORES.dat')


def agregar():
    codigo = input('Ingrese codigo de vendedor: ')
    posicion = mantenedores.compartidos.encontrar_espacio(codigo, 'vendedores')
    if posicion == -1:
        print('Vendedor ya ha sido agregado.')
    else:
        FILE = open(vendedores_path, 'r+')
        nombre = input('Ingrese nombre de vendedor: ')[0:30]
        FILE.seek(posicion)
        FILE.write(codigo.zfill(5) + nombre.ljust(30))
        FILE.close()


def modificar():
    codigo = input('Ingrese codigo de vendedor a modificar: ')
    [posicion, registro] = mantenedores.compartidos.obtener_uno(codigo, 'vendedores')
    if registro is None:
        print('Vendedor no existe, no se puede modificar.')
    else:
        vendedor = dto.Vendedor(registro)
        print('Codigo:', vendedor.codigo, '- Nombre:', vendedor.nombre)
        print('-- Nuevos datos --')
        nombre = input('Nombre: ')
        FILE = open(vendedores_path, 'r+')
        FILE.seek(posicion)
        FILE.write(codigo.zfill(5) + nombre.ljust(30))
        FILE.close()


def consultar():
    codigo = input('Ingrese codigo de vendedor a buscar: ')
    registro = mantenedores.compartidos.obtener_uno(codigo, 'vendedores')[1]  # Retorna [posicion, registro] => [1] = Obteniendo registro
    if registro is None:
        print('Vendedor no existe.')
    else:
        vendedor = dto.Vendedor(registro)
        print('Nombre de vendedor: ' + vendedor.nombre)


def eliminar():
    codigo = input('Ingrese codigo de vendedor: ')
    [posicion, registro] = mantenedores.compartidos.obtener_uno(codigo, 'vendedores')
    if registro is None:
        print('Vendedor no existe.')
    else:
        vendedor = dto.Vendedor(registro)
        print('Nombre:', vendedor.nombre)
        if mantenedores.ventas.existe_vendedor_en_ventas(codigo):
            print('El vendedor ha hecho ventas, asi que no se puede eliminar.')
        else:
            FILE = open(vendedores_path, 'r+')
            FILE.seek(posicion)
            FILE.write('00000' + " " * (LONGITUD_REGISTRO - 5))
            FILE.close()
            print(vendedor.nombre, 'eliminado satisfactoriamente.')


def listar():
    file = open(vendedores_path, 'r')
    archivo_vacio = True
    while file.tell() < os.path.getsize(vendedores_path):
        registro_actual = file.read(LONGITUD_REGISTRO)
        codigo = registro_actual[0:5].strip()
        if codigo != '00000':  # Registro no vacio
            nombre = registro_actual[5:30].strip()
            archivo_vacio = False
            print('Codigo:', int(codigo), '- Nombre:', nombre)
    if archivo_vacio:
        print('El archivo no tiene vendedores aun. Enter para continuar...')
    else:
        print('Fin del listado. Enter para continuar...')
    file.close()
