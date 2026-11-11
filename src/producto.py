class Producto:
    def __init__(self, codigo, nombre, precio, existencia):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        self.existencia = existencia

    def mostrar_informacion(self):
        print(f"--- Información del Producto ---")
        print(f"Código: {self.codigo}")
        print(f"Nombre: {self.nombre}")
        print(f"Precio: ${self.precio}")
        print(f"Existencia en inventario: {self.existencia}")

# Prueba local rápida
if __name__ == "__main__":
    p1 = Producto("P001", "Teclado Mecánico", 45.99, 15)
    p1.mostrar_informacion()