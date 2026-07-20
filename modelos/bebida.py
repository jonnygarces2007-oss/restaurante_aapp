from modelos.producto import Producto


class Bebida(Producto):
   
    def __init__(self, codigo: int, nombre: str, categoria: str, precio: float, tamaño: str, tipo_envase: str):
        # Llamamos al constructor de la clase padre
        super().__init__(codigo, nombre, categoria, precio)
        # Atributos específicos de bebida
        self.tamaño = tamaño.strip()
        self.tipo_envase = tipo_envase.strip().capitalize()

    def mostrar_informacion(self) -> str:
        info_base = super().mostrar_informacion()
        return f"{info_base} | Tamaño: {self.tamaño} | Envase: {self.tipo_envase}"
