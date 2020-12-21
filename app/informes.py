from datetime import date, datetime
from typing import Dict

import app
import dto


def listar_stock_critico():
    FILE = open(app.productos.PRODUCTOS_PATH)
    registro = FILE.read(app.productos.LONGITUD_REGISTRO)
    hay_stock_critico = False
    while registro != "":
        if registro[0:5] != '00000':
            producto = dto.Producto(registro)
            if producto.stock < 5:
                hay_stock_critico = True
                print(producto.nombre, 'con precio', producto.precio, 'tiene', producto.stock, 'unidades restantes.')
        registro = FILE.read(app.productos.PRODUCTOS_PATH)
    if not hay_stock_critico:
        print('No hay productos en stock critico.')
    input('Presione enter para continuar...')


def listar_reacudacion_diaria():
    recaudacion_diaria: Dict[int, int] = {}  # {timestamp => recaudacion_total}
    ENC_VTA_FILE = open(app.ventas.ENC_VTA_PATH)
    for linea_enc in ENC_VTA_FILE:
        encabezado = dto.EncabezadoVenta(linea_enc)
        dia, mes, anho = encabezado.fecha.split('/')
        timestamp = int(datetime.timestamp(datetime(int(anho), int(mes), int(dia))))  # Convirtiendo fecha a timestamp para luego listar de menor a mayor.
        if timestamp not in recaudacion_diaria:  # Si la fecha aun no existe, inicializa su recaudacion del dia en 0
            recaudacion_diaria[timestamp] = 0
        recaudacion_diaria[timestamp] += app.ventas.obtener_total_venta(encabezado)
    ENC_VTA_FILE.close()
    if recaudacion_diaria:
        for timestamp in sorted(recaudacion_diaria):  # ordenando los timestamp para listar las recaudaciones de mas antigua a la mas nueva.
            print(date.fromtimestamp(timestamp), ':', recaudacion_diaria[timestamp], '$')
    else:
        print('No hay ventas aun.')
    input('Presione enter para continuar...')


def listar_ventas_por_vendedor():
    ventas_por_vendedor: Dict[str, int] = {}  # {nombre_vendedor: total_recaudado}
    ENC_VTA_FILE = open(app.ventas.ENC_VTA_PATH)
    for linea_enc in ENC_VTA_FILE:
        encabezado = dto.EncabezadoVenta(linea_enc)
        registro_vendedor = app.compartidos.obtener_uno(str(encabezado.cod_vendedor), 'vendedores')[
            1]  # Retorna [posicion, registro] => Obteniendo solo registro
        vendedor = dto.Vendedor(registro_vendedor)
        if vendedor.nombre not in ventas_por_vendedor:  # Si el vendedor aun no existe, inicializa su recaudacion en 0
            ventas_por_vendedor[vendedor.nombre] = 0
        ventas_por_vendedor[vendedor.nombre] += app.ventas.obtener_total_venta(encabezado)
    ENC_VTA_FILE.close()
    for vendedor in ventas_por_vendedor:
        print(vendedor, ':', ventas_por_vendedor[vendedor])
    else:
        print('No hay vendedores aun.')
    input('Presione enter para continuar...')