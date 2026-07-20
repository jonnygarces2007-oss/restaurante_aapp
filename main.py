from servicios.restaurante import Restaurante
from modelos.producto import Producto
from modelos.bebida import Bebida
from modelos.cliente import Cliente


def mostrar_menu() -> None:
    print("\n========================================")
    print("        SISTEMA DE RESTAURANTE")
    print("========================================")
    print("1. Registrar producto")
    print("2. Registrar bebida")
    print("3. Registrar cliente")
    print("----------------------------------------")
    print("4. Listar productos")
    print("5. Listar clientes")
    print("----------------------------------------")
    print("6. Salir")
    print("========================================")


def main():
    restaurante = Restaurante(nombre="Sabor Andino")

    while True:
        mostrar_menu()
        try:
            opcion = int(input("Seleccione una opción: "))
        except ValueError:
            print("⚠️ Ingrese un número válido.")
            continue

        # 1. Registrar producto
        if opcion == 1:
            print("\n--- Registrar Producto ---")
            try:
                codigo = int(input("Código único: "))
                nombre = input("Nombre: ")
                categoria = input("Categoría: ")
                precio = float(input("Precio: $"))

                nuevo = Producto(codigo, nombre, categoria, precio)
                if restaurante.registrar_producto(nuevo):
                    print("✅ Producto registrado.")
                else:
                    print("❌ Error: código ya existe.")
            except ValueError:
                print("❌ Datos inválidos.")

        # 2. Registrar bebida
        elif opcion == 2:
            print("\n--- Registrar Bebida ---")
            try:
                codigo = int(input("Código único: "))
                nombre = input("Nombre: ")
                categoria = input("Categoría: ")
                precio = float(input("Precio: $"))
                tamaño = input("Tamaño (ej: 500ml, 1L): ")
                envase = input("Tipo de envase (ej: Botella, Vaso): ")

                nueva = Bebida(codigo, nombre, categoria, precio, tamaño, envase)
                if restaurante.registrar_producto(nueva):
                    print("✅ Bebida registrada.")
                else:
                    print("❌ Error: código ya existe.")
            except ValueError:
                print("❌ Datos inválidos.")

        # 3. Registrar cliente
        elif opcion == 3:
            print("\n--- Registrar Cliente ---")
            try:
                id_cliente = int(input("Identificación: "))
                nombre = input("Nombre completo: ")
                correo = input("Correo: ")

                nuevo = Cliente(id_cliente, nombre, correo)
                if restaurante.registrar_cliente(nuevo):
                    print("✅ Cliente registrado.")
                else:
                    print("❌ Error: identificación ya existe.")
            except ValueError:
                print("❌ Datos inválidos.")

        # 4. Listar productos
        elif opcion == 4:
            restaurante.listar_productos()

        # 5. Listar clientes
        elif opcion == 5:
            restaurante.listar_clientes()

        # 6. Salir
        elif opcion == 6:
            print("👋 Saliendo del sistema...")
            break

        else:
            print("⚠️ Opción no válida.")


if __name__ == "__main__":
    main()
