from os.path import join, dirname

productos_path = join(dirname(__file__), '../db/PRODUCTOS.dat')
vendedores_path = join(dirname(__file__), '../db/VENDEDORES.dat')


# Retorna el hashing, siendo el mismo algoritmo en ambos casos.
def obtener_hashing(codigo: str, tipo: str) -> int:
    posicion = 0
    for digito in codigo:
        posicion += int(digito)
    return 64 if tipo == 'productos' else 35 * (posicion - 1)


# Funcion para buscar un registro tanto en el archivo vendedores como en productos.
# Esto gracias a que comparten la gran parte de su estructura, (codigo, hashing, area de datos y overflow).
def encontrar_espacio(codigo: str, tipo: str) -> int or None:
    LONGITUD_REGISTRO = 64 if tipo == 'productos' else 35
    PATH = productos_path if tipo == 'productos' else vendedores_path
    FILE = open(PATH)
    posicion = obtener_hashing(codigo, tipo)
    FILE.seek(posicion)
    registro = FILE.read(LONGITUD_REGISTRO)
    if registro[0:5] == '00000':  # Ubicacion libre en el area de datos
        return posicion
    elif int(registro[0:5]) == int(codigo):
        return -1
    else:  # Buscando en el area de overflow
        posicion = 45 * LONGITUD_REGISTRO
        FILE.seek(posicion)
        registro = FILE.read(LONGITUD_REGISTRO)
        while registro != '' and int(registro[0:5]) != int(codigo):
            registro = FILE.read(LONGITUD_REGISTRO)
            posicion += + LONGITUD_REGISTRO
        FILE.close()
        if registro != '':
            return -1
        return posicion


# Funcion para buscar un registro tanto en el archivo vendedores como en productos.
def obtener_uno(codigo: str, tipo: str) -> str or None:
    LONGITUD_REGISTRO = 64 if tipo == 'productos' else 35
    PATH = productos_path if tipo == 'productos' else vendedores_path
    FILE = open(PATH)
    posicion = obtener_hashing(codigo, tipo)
    FILE.seek(posicion)
    registro = FILE.read(LONGITUD_REGISTRO)
    if int(codigo) == int(registro[0:5]):
        FILE.close()
        return registro
    else:
        posicion = 45 * LONGITUD_REGISTRO
        FILE.seek(posicion)
        registro = FILE.read(LONGITUD_REGISTRO)
        while registro != "" and int(codigo) != int(registro[0:5]):
            registro = FILE.read(LONGITUD_REGISTRO)
        FILE.close()
        if registro == "":
            return None
        else:
            return registro
