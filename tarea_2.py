from datetime import date
from typing import Dict
from classes import Vendedor, Producto


def verificar_fecha(fecha: str) -> [bool, str or None]:
    try:
        day, month, year = fecha.strip().split('/')
        date(int(year), int(month), int(day))  # Si fecha no es valida, date() lanza un ValueError
        if int(year) < 2010 or int(year) > 2020:
            raise Exception('Anio debe estar entre 2010 y 2020', 'year')
        return [True, None]
    except ValueError and Exception as error:
        return [False, error]


def obtener_ultimo_codigo_enc_vta() -> int:
    names_file = open('db/ENC_VTA.dat', 'r')
    last = ""
    for line in names_file:
        last = line
    names_file.close()
    if last == "":
        return 0
    return int(last.split(";")[0])


def agregar_detalle_venta() -> bool:
    productos: Dict[int, int] = {}  # {codigo: cantidad}
    codigo = -1
    try:
        while codigo != 0:
            codigo = int(input("Ingrese codigo de producto, 0 para finalizar: "))
            if codigo in productos:
                raise Exception("Producto ya ha sido agregado")
            producto = obtener_producto(codigo)
            if producto is None:
                raise Exception('Producto no existe en el registro.')
            print("Precio unitario de", producto.nombre, ":", producto.stock)
            cantidad_a_comprar = int(input("Cantidad a comprar: "))
            if producto.stock < cantidad_a_comprar:
                raise Exception("Solo quedan", producto.stock, "de", producto.nombre)
            productos[codigo] = 0
    except ValueError and Exception as e:
        print(e)


def obtener_producto(codigo: int) -> Producto or None:
    return Producto(1, "PRODUCTO", 2300, 120)


def obtener_vendedor(codigo: int) -> Vendedor or None:
    return True


def agregar_encabezado_venta(fecha: str, cod_vendedor: int, estado: str) -> bool:
    encab_file = open('db/ENC_VTA.dat', 'a')
    vendedor = obtener_vendedor(cod_vendedor)
    if vendedor is None:
        print("No existe vendedor con el codigo " + str(cod_vendedor))
        return False
    [fecha_valida, error] = verificar_fecha(fecha)
    if not fecha_valida:
        print("Fecha no es valida. Error: ", error)
        return False
    ultimo_codigo = obtener_ultimo_codigo_enc_vta()
    encab_file.write(str(ultimo_codigo + 1).zfill(5) + ';' + fecha + ';' + str(cod_vendedor) + ';' + estado + '\n')
    encab_file.close()
    return True


agregar_detalle_venta()
