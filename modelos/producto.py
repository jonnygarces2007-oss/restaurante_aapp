class Producto:
   

    def __init__(self, codigo: int, nombre: str, categoria: str, precio: float):
        self.codigo = codigo
        self.nombre = nombre.strip().capitalize()
        self.categoria = categoria.strip().capitalize()
        self.precio = round(precio, 2)

    def mostrar_informacion(self) -> str:
     
        return (f"Código: {self.codigo} | Nombre: {self.nombre} | "
                f"Categoría: {self.categoria} | Precio: ${self.precio:.2f}")
