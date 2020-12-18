from datetime import date
from os.path import dirname, join
from typing import Dict

from dto.classes import EncabezadoVenta
from mantenedores import productos, vendedores, compartidos


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
    names_file = open(join(dirname(__file__), '../db/ENC_VTA.dat'), 'r')
    last = ""
    for line in names_file:
        last = line
    names_file.close()
    if last == "":
        return None
    numero, fecha, vendedor, estado = last.split(';')  # 00001;18/01/2013;12345;V
    return EncabezadoVenta(int(numero), fecha, int(vendedor), estado)


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
        cod_vendedor = input("Codigo de vendedor: ")
        vendedor = vendedores.obtener_uno(cod_vendedor, 'vendedores')
        if vendedor is None:
            raise Exception('Vendedor no existe...')

        productos_dict: Dict[int, int] = {}  # {codigo: cantidad}
        while True:
            codigo = input("Ingrese codigo de producto, 0 para finalizar: ")
            if codigo == 0:
                break
            if codigo in productos_dict:
                print("Producto ya ha sido agregado, intente nuevamente")
                continue  # Reintentando la venta
            producto = compartidos.obtener_uno(codigo, 'productos')
            if producto is None:
                print('Producto no existe en el registro, intente nuevamente.')
                continue
            print("Precio unitario de", producto.nombre, ":", producto.stock)
            cantidad_a_comprar = int(input("Cantidad a comprar: "))
            if producto.stock < cantidad_a_comprar:
                print("Solo quedan", producto.stock, "de", producto.nombre)
                continue
            productos_dict[int(codigo)] = cantidad_a_comprar

        # Pasó todas las validaciones
        encabezados_file = open(join(dirname(__file__), '../db/ENC_VTA.dat'), 'a')
        detalles_file = open(join(dirname(__file__), '../db/DET_VTA.dat'), 'a')
        for cod_producto in productos_dict:
            detalles_file.write(str(ultimo_codigo).rjust(5) + ';' + str(cod_producto) + ';' + str(productos_dict[cod_producto]) + '\n')
            productos.modificar(cod_producto, {'cantidad': productos_dict[cod_producto]})
        encabezados_file.write(str(ultimo_codigo).rjust(5) + ';' + fecha + ';' + str(cod_vendedor) + ';' + 'V' + '\n')
        encabezados_file.close()
        detalles_file.close()

    except Exception as e:
        print(e)


def consultar_venta():
    pass


def anular_venta():
    pass
