from datetime import date
from os.path import dirname, join
from typing import Dict

import dto
import mantenedores
from .productos import restar_stock

ENC_VTA_PATH = join(dirname(__file__), '../db/ENC_VTA.dat')
DET_VTA_PATH = join(dirname(__file__), '../db/DET_VTA.dat')


def validar_fecha(fecha: str) -> [bool, str or None]:  # => [es_valida, error or None]
    try:
        day, month, year = fecha.strip().split('/')
        date(int(year), int(month), int(day))  # Si fecha no es valida, date() lanza un ValueError
        if int(year) < 2010 or int(year) > 2020:
            raise ValueError('Anio debe estar entre 2010 y 2020', 'year')
        return [True, None]
    except ValueError as error:
        return [False, error]


def existe_vendedor_en_ventas(codigo_vendedor: str) -> bool:
    """
    Helper para verificar si un vendedor realizado ventas.
    """
    FILE = open(ENC_VTA_PATH)
    existe = False
    registro = FILE.readline()
    while registro != '' and not existe:
        enc_vta = dto.EncabezadoVenta(registro)
        if enc_vta.cod_vendedor == int(codigo_vendedor):
            existe = True
        registro = FILE.read()
    return existe


def existe_producto_en_ventas(codigo_producto: str) -> bool:
    """
    Helper para verificar si un producto ha sido vendido.
    """
    FILE = open(DET_VTA_PATH)
    existe = False
    registro = FILE.readline()
    while registro != '' and not existe:
        enc_vta = dto.DetalleVenta(registro)
        if enc_vta.cod_producto == int(codigo_producto):
            existe = True
        registro = FILE.read()
    return existe


def obtener_ultimo_enc_vta() -> dto.EncabezadoVenta or None:
    ENC_VTA_FILE = open(ENC_VTA_PATH)
    ultimo = ""
    for linea in ENC_VTA_FILE:
        ultimo = linea
    ENC_VTA_FILE.close()
    if ultimo == "":
        return None
    return dto.EncabezadoVenta(ultimo)  # 1;18/01/2013;12345;V


# Helper
def obtener_recaudacion_detalle_venta(encabezado: dto.EncabezadoVenta) -> int:
    """
    Retorna el total de una venta especifica del estilo num_boleta:cod_producto:cantidad
    """
    DET_VTA_FILE = open(DET_VTA_PATH)
    total = 0
    for linea_det in DET_VTA_FILE:
        detalle = dto.DetalleVenta(linea_det)
        if encabezado.num_boleta == detalle.num_boleta:
            registro_producto = mantenedores.compartidos.obtener_uno(str(detalle.cod_producto), 'productos')[
                1]  # Retorna [posicion, registro] => Obteniendo solo registro
            producto = dto.Producto(registro_producto)
            total += producto.precio * detalle.cantidad
    DET_VTA_FILE.close()
    return total


def realizar_venta():
    try:
        ultimo_enc = obtener_ultimo_enc_vta()
        ultimo_codigo = 0 if ultimo_enc is None else ultimo_enc.num_boleta + 1

        # Validar fecha
        fecha = input("Fecha de venta (dd/mm/yyyy): ")
        [valida, error] = validar_fecha(fecha)
        if not valida:
            raise Exception(error)

        # Validar vendedor
        cod_vendedor = input("Codigo de vendedor: ")
        registro_vendedor = mantenedores.compartidos.obtener_uno(cod_vendedor, 'vendedores')[1]
        if registro_vendedor is None:
            raise Exception('Vendedor no existe...')

        productos_dict: Dict[int, int] = {}  # {codigo: cantidad}
        while True:
            codigo = input("Ingrese codigo de producto, 0 para finalizar: ")
            if codigo == "0":
                break

            if codigo in productos_dict:
                print("Producto ya ha sido agregado, intente nuevamente")
                continue  # Reintentando la venta

            registro_producto = mantenedores.compartidos.obtener_uno(codigo, 'productos')[1]
            if registro_producto is None:
                print('Producto no existe en el registro, intente nuevamente.')
                continue

            producto = dto.Producto(registro_producto)
            print("Precio unitario de", producto.nombre, ":", producto.precio)
            cantidad_a_comprar = int(input("Cantidad a comprar: "))
            if producto.stock < cantidad_a_comprar:
                print("Solo quedan", producto.stock, "de", producto.nombre)
                continue
            productos_dict[int(producto.codigo)] = cantidad_a_comprar

        # Pasó todas las validaciones, registrando venta en
        ENC_VTA_FILE = open(ENC_VTA_PATH, 'a')
        DET_VTA_FILE = open(DET_VTA_PATH, 'a')
        for cod_producto in productos_dict:
            DET_VTA_FILE.write(str(ultimo_codigo).rjust(5) + ';' + str(cod_producto) + ';' + str(productos_dict[cod_producto]) + '\n')
            restar_stock(str(cod_producto), productos_dict[cod_producto])
        ENC_VTA_FILE.write(str(ultimo_codigo).rjust(5) + ';' + fecha + ';' + str(cod_vendedor) + ';' + 'V' + '\n')
        ENC_VTA_FILE.close()
        DET_VTA_FILE.close()

    except Exception as e:
        print(e)


def consultar_venta():
    pass


def anular_venta():
    pass
