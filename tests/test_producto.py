import unittest
from src.producto import Producto

class TestProducto(unittest.TestCase):

    # CP01: Crear un producto
    def test_cp01_crear_producto(self):
        p = Producto("P001", "Teclado", 350.0, 10)
        self.assertIsNotNone(p)

    # CP02: Mostrar / verificar el código
    def test_cp02_mostrar_codigo(self):
        p = Producto("P001", "Teclado", 350.0, 10)
        self.assertEqual(p.codigo, "P001")

    # CP03: Mostrar / verificar el nombre
    def test_cp03_mostrar_nombre(self):
        p = Producto("P001", "Teclado", 350.0, 10)
        self.assertEqual(p.nombre, "Teclado")

    # CP04: Mostrar / verificar el precio
    def test_cp04_mostrar_precio(self):
        p = Producto("P001", "Teclado", 350.0, 10)
        self.assertEqual(p.precio, 350.0)

    # CP05: Mostrar / verificar la existencia
    def test_cp05_mostrar_existencia(self):
        p = Producto("P001", "Teclado", 350.0, 10)
        self.assertEqual(p.existencia, 10)

    # CP06: Mostrar información completa
    def test_cp06_mostrar_informacion_completa(self):
        p = Producto("P001", "Teclado", 350.0, 10)
        info = p.mostrar_informacion()
        self.assertIn("P001", info)
        self.assertIn("Teclado", info)
        self.assertIn("350.0", info)
        self.assertIn("10", info)

    # CP07: Crear otro producto (independencia de datos)
    def test_cp07_crear_otro_producto(self):
        p2 = Producto("P002", "Mouse", 180.0, 5)
        self.assertEqual(p2.codigo, "P002")
        self.assertEqual(p2.nombre, "Mouse")
        self.assertEqual(p2.precio, 180.0)
        self.assertEqual(p2.existencia, 5)

if __name__ == "__main__":
    unittest.main()