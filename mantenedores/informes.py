from typing import Dict

import dto
from .compartidos import obtener_uno
from .productos import LONGITUD_REGISTRO as LARGO_PRODUCTO, productos_path
from .ventas import ENC_VTA_PATH, obtener_recaudacion_detalle_venta


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
        print('No hay productos en stock critico.')
    input('Presione enter para continuar...')


def listar_reacudacion_diaria():
    recaudacion_diaria: Dict[str, int] = {}  # {fecha: recaudacion_total}
    ENC_VTA_FILE = open(ENC_VTA_PATH)
    for linea_enc in ENC_VTA_FILE:
        encabezado = dto.EncabezadoVenta(linea_enc)
        if encabezado.fecha not in recaudacion_diaria:  # Si la fecha aun no existe, inicializa su recaudacion del dia en 0
            recaudacion_diaria[encabezado.fecha] = 0
        recaudacion_diaria[encabezado.fecha] += obtener_recaudacion_detalle_venta(encabezado)
    ENC_VTA_FILE.close()
    for fecha in recaudacion_diaria:
        print(fecha, ':', recaudacion_diaria[fecha], '$')
    else:
        print('No hay ventas aun.')
    input('Presione enter para continuar...')


def listar_ventas_por_vendedor():
    ventas_por_vendedor: Dict[str, int] = {}  # {nombre_vendedor: total_recaudado}
    ENC_VTA_FILE = open(ENC_VTA_PATH)
    for linea_enc in ENC_VTA_FILE:
        encabezado = dto.EncabezadoVenta(linea_enc)
        registro_vendedor = obtener_uno(str(encabezado.cod_vendedor), 'vendedores')[1]  # Retorna [posicion, registro] => Obteniendo solo registro
        vendedor = dto.Vendedor(registro_vendedor)
        if vendedor.nombre not in ventas_por_vendedor:  # Si el vendedor aun no existe, inicializa su recaudacion en 0
            ventas_por_vendedor[vendedor.nombre] = 0
        ventas_por_vendedor[vendedor.nombre] += obtener_recaudacion_detalle_venta(encabezado)
    ENC_VTA_FILE.close()
    for vendedor in ventas_por_vendedor:
        print(vendedor, ':', ventas_por_vendedor[vendedor])
    else:
        print('No hay vendedores aun.')
    input('Presione enter para continuar...')
