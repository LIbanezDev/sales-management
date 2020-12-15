from datetime import date
from typing import Dict
from dto.classes import Vendedor, Producto, EncabezadoVenta
from os.path import dirname, join

dirname = dirname(__file__)


def validar_fecha(fecha: str) -> [bool, str or None]:
    try:
        day, month, year = fecha.strip().split('/')
        date(int(year), int(month), int(day))  # Si fecha no es valida, date() lanza un ValueError
        if int(year) < 2010 or int(year) > 2020:
            raise ValueError('Anio debe estar entre 2010 y 2020', 'year')
        return [True, None]
    except ValueError as error:
        return [False, error]


def obtener_ultimo_enc_vta() -> EncabezadoVenta or None:
    names_file = open(join(dirname, '../db/ENC_VTA.dat'), 'r')
    last = ""
    for line in names_file:
        last = line
    names_file.close()
    if last == "":
        return None
    numero, fecha, vendedor, estado = last.split(';')  # 00001;18/01/2013;12345;V
    return EncabezadoVenta(int(numero), fecha, int(vendedor), estado)


def restar_stock_producto(cod_producto: int, cantidad: int):
    productos = open(join(dirname, '../db/PRODUCTOS.dat'))
    productos.close()


def obtener_producto(codigo: int) -> Producto or None:
    return Producto(1, "PRODUCTO", 2300, 120)


def obtener_vendedor(codigo: int) -> Vendedor or None:
    return Vendedor(12345, "Lucas con 30 caracteres".zfill(30))


def realizar_venta():
    try:
        ultimo_enc = obtener_ultimo_enc_vta()
        ultimo_codigo = 0 if ultimo_enc is None else ultimo_enc.num_boleta + 1

        # Validar fecha
        # fecha = input("Fecha de venta: ")
        fecha = "18/01/2011"
        [valida, error] = validar_fecha(fecha)
        if not valida:
            raise Exception(error)

        # Validar vendedor
        cod_vendedor = int(input("Codigo de vendedor: "))
        vendedor = obtener_vendedor(cod_vendedor)
        if vendedor is None:
            raise Exception('Vendedor no existe...')

        productos: Dict[int, int] = {}  # {codigo: cantidad}
        while True:
            codigo = int(input("Ingrese codigo de producto, 0 para finalizar: "))
            if codigo == 0:
                break
            if codigo in productos:
                print("Producto ya ha sido agregado, intente nuevamente")
                continue  # Reintentando la venta
            producto = obtener_producto(codigo)
            if producto is None:
                print('Producto no existe en el registro, intente nuevamente.')
                continue
            print("Precio unitario de", producto.nombre, ":", producto.stock)
            cantidad_a_comprar = int(input("Cantidad a comprar: "))
            if producto.stock < cantidad_a_comprar:
                print("Solo quedan", producto.stock, "de", producto.nombre)
                continue
            productos[codigo] = cantidad_a_comprar

        # Pasó todas las validaciones
        encabezados_file = open(join(dirname, '../db/ENC_VTA.dat'), 'a')
        detalles_file = open(join(dirname, '../db/DET_VTA.dat'), 'a')
        for cod_producto in productos:
            detalles_file.write(str(ultimo_codigo).zfill(5) + ';' + str(cod_producto) + ';' + str(productos[cod_producto]) + '\n')
            restar_stock_producto(cod_producto=cod_producto, cantidad=productos[cod_producto])
        encabezados_file.write(str(ultimo_codigo).zfill(5) + ';' + fecha + ';' + str(cod_vendedor) + ';' + 'V' + '\n')
        encabezados_file.close()
        detalles_file.close()

    except Exception as e:
        print(e)
