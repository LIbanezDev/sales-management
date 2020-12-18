# Retorna el hashing, siendo el mismo algoritmo en ambos casos.
def obtener_hashing(codigo: str, tipo: str) -> int:
    posicion = 0
    for digito in codigo:
        posicion += int(digito)
    return 64 if tipo == 'productos' else 35 * (posicion - 1)


# Funcion para buscar un registro tanto en el archivo vendedores como en productos.
# Esto gracias a que comparten la gran parte de su estructura, (codigo, hashing, area de datos y overflow).
def encontrar_espacio(codigo: str, tipo: str, file_path: str) -> int or None:
    LONGITUD_REGISTRO = 64 if tipo == 'productos' else 35
    FILE = open(file_path)
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
        if registro != '':
            return -1
        return posicion


# Funcion para buscar un registro tanto en el archivo vendedores como en productos.
def obtener_uno(codigo: str, tipo: str, file_path: str) -> str or None:
    LONGITUD_REGISTRO = 64 if tipo == 'productos' else 35
    file = open(file_path)
    posicion = obtener_hashing(codigo, tipo)
    file.seek(posicion)
    registro = file.read(LONGITUD_REGISTRO)
    if int(codigo) == int(registro[0:5]):
        file.close()
        return registro
    else:
        posicion = 45 * LONGITUD_REGISTRO
        file.seek(posicion)
        registro = file.read(LONGITUD_REGISTRO)
        while registro != "" and int(codigo) != int(registro[0:5]):
            registro = file.read(LONGITUD_REGISTRO)
        file.close()
        if registro == "":
            return None
        else:
            return registro
