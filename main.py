# Lucas Vergara - Kevin Figueroa 192-B

import os

from app import ventas, productos, vendedores, informes


def create_database():
    files_names = ['ENC_VTA', 'DET_VTA', 'PRODUCTOS', 'VENDEDORES']
    if not os.path.isdir('./db'):
        os.mkdir('./db/')
    for file_name in files_names:
        full_name = 'db/' + file_name + '.dat'
        if not os.path.isfile(full_name):
            file = open(full_name, 'w')
            if file_name == 'PRODUCTOS' or file_name == 'VENDEDORES':
                for i in range(45):
                    file.write("00000" + " " * ((vendedores.LONGITUD_REGISTRO if file_name == 'VENDEDORES' else productos.LONGITUD_REGISTRO) - 5))
            file.close()


if __name__ == '__main__':
    create_database()
    continuar = True
    opt, opt_final = 0, 0
    while opt != 5:
        print('1. Ventas')
        print('2. Vendedores')
        print('3. Productos')
        print('4. Informes')
        print('5. Salir')
        opt = input('Ingrese opcion: ')
        if '0' <= opt <= '9':
            opt = int(opt)
        if opt == 1:
            print('1. Registrar venta')
            print('2. Consultar venta')
            print('3. Anular venta')
            opt_final = input('Ingrese opcion: ')
            if '0' <= opt_final <= '9':
                opt_final = int(opt_final)
            if opt_final == 1:
                ventas.realizar_venta()
            elif opt_final == 2:
                ventas.consultar_venta()
            elif opt_final == 3:
                ventas.anular_venta()
            else:
                print('Opcion no reconocida.')
        elif opt == 2:
            print('1. Agregar vendedor')
            print('2. Modificar vendedor')
            print('3. Consultar vendedor')
            print('4. Eliminar vendedor')
            print('5. Listar vendedores')
            opt_final = input('Ingrese opcion: ')
            if '0' <= opt_final <= '9':
                opt_final = int(opt_final)
            if opt_final == 1:
                vendedores.agregar()
            elif opt_final == 2:
                vendedores.modificar()
            elif opt_final == 3:
                vendedores.consultar()
            elif opt_final == 4:
                vendedores.eliminar()
            elif opt_final == 5:
                vendedores.listar()
            else:
                print('Opcion no reconocida.')
        elif opt == 3:
            print('1. Agregar productos')
            print('2. Modificar productos')
            print('3. Consultar productos')
            print('4. Eliminar productos')
            print('5. Listar productos')
            opt_final = input('Ingrese opcion: ')
            if '0' <= opt_final <= '9':
                opt_final = int(opt_final)
            if opt_final == 1:
                productos.agregar()
            elif opt_final == 2:
                productos.modificar()
            elif opt_final == 3:
                productos.consultar()
            elif opt_final == 4:
                productos.eliminar()
            elif opt_final == 5:
                productos.listar()
            else:
                print('Opcion no reconocida.')
        elif opt == 4:
            print('1. Productos con stock critico')
            print('2. Recaudacion diaria')
            print('3. Ventas por vendedor')
            opt_final = input('Ingrese opcion: ')
            if '0' <= opt_final <= '9':
                opt_final = int(opt_final)
            if opt_final == 1:
                informes.listar_stock_critico()
            elif opt_final == 2:
                informes.listar_reacudacion_diaria()
            elif opt_final == 3:
                informes.listar_ventas_por_vendedor()
            else:
                print('Opcion no reconocida')
        elif opt != 5:
            print('Opcion no reconocida.')
