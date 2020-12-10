import unittest
from tarea_2 import agregar_encabezado_venta, obtener_ultimo_codigo_enc_vta


class Tarea2TestCase(unittest.TestCase):
    def test_agregar_encabezado(self):
        agrego_uno = agregar_encabezado_venta("18/02/2009", 12345, "V")
        last = obtener_ultimo_codigo_enc_vta()
        agrego_dos = agregar_encabezado_venta("18/02/2010", 23345, "V")
        new_last = obtener_ultimo_codigo_enc_vta()
        self.assertEqual(agrego_uno, False, 'should be false because of invalid date')
        self.assertEqual(agrego_dos, True, 'should be true')
        self.assertEqual(new_last, last + 1, 'should have a correlative code')


if __name__ == '__main__':
    unittest.main()
