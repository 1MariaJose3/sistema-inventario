class Producto:
    def __init__(self, codigo: str, nombre: str, precio: float, existencia: int):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        self.existencia = existencia

    # Agrega self dentro de los paréntesis
    def mostrar_informacion(self) -> str:
        return f"Código: {self.codigo} | Nombre: {self.nombre} | Precio: ${self.precio} | Existencia: {self.existencia}"