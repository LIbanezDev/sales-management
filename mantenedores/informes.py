from typing import Dict

import dto
from .productos import LONGITUD_REGISTRO as LARGO_PRODUCTO, productos_path


def listar_stock_critico():
    FILE = open(productos_path)
    registro = FILE.read(LARGO_PRODUCTO)
    hay_stock_critico = False
    while registro != "":
        if registro[0:5] != '00000':
            producto = dto.Producto(registro)
            if producto.stock < 5:
                hay_stock_critico = True
                print(producto.nombre, 'con precio', producto.precio, 'tiene', producto.stock, 'unidades restantes.')
        registro = FILE.read(LARGO_PRODUCTO)
    if not hay_stock_critico:
        print('No hay stock critico.')


def listar_reacudacion_diaria():
    recaudacion_diaria: Dict[str, int] = {'18/01/2001': 23, '18/01/2002': 30}  # {fecha: recaudacion_total}
    for fecha in recaudacion_diaria:
        print(fecha, ':', recaudacion_diaria[fecha], '$')
    pass


def listar_ventas_por_vendedor():
    ventas_por_vendedor: Dict[str, int] = {'Reiner Braun': 30, 'Annie Leonhart': 34}  # {nombre_vendedor: total_recaudado}
    for vendedor in ventas_por_vendedor:
        print(vendedor, ':', ventas_por_vendedor[vendedor])
    pass
