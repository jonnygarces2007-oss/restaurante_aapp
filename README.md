# restaurante_aapp
# 📋 Sistema de Gestión de Restaurante - Semana 8

**Asignatura:** Programación Orientada a Objetos  
**Estudiante:** [Tu Nombre Completo]  
**Fecha:** Julio 2026

---

## 🎯 Objetivo
Mejorar el sistema aplicando los primeros tres principios **SOLID**: Responsabilidad Única, Abierto/Cerrado y Sustitución de Liskov, mediante herencia y polimorfismo.

---

## 📁 Estructura y responsabilidades
restaurante_app/
├── modelos/ # Solo definen datos y comportamiento de entidades
│ ├── producto.py # Clase base: atributos y método común
│ ├── bebida.py # Hereda de Producto, agrega datos propios
│ └── cliente.py # Solo representa al cliente
├── servicios/
│ └── restaurante.py # Gestiona listas, validaciones y lógica de negocio
└── main.py # Solo menú, entrada de datos y creación de objetos

---

## 🧩 Relación entre clases
- **`Producto`**: Es la clase base con los datos generales (código, nombre, categoría, precio).
- **`Bebida`**: Es una especialización → **hereda** de `Producto` y agrega `tamaño` y `tipo_envase`.
- **`Cliente`**: Es una entidad independiente, no tiene relación de herencia con productos.

---

## ✅ Principios SOLID aplicados
1. **SRP – Responsabilidad Única**: Cada clase hace una sola cosa: las entidades se definen en `modelos`, la gestión en `servicios` y la interacción en `main.py`.
2. **OCP – Abierto/Cerrado**: Se agregó `Bebida` sin modificar la lógica existente de `Producto` ni de `Restaurante`.
3. **LSP – Sustitución de Liskov**: Una `Bebida` se usa exactamente igual que un `Producto`: se guarda en la misma lista y responde al mismo método `mostrar_informacion()` sin errores.

---

## 🚀 Ejecución
```bash
python main.py
El menú permite registrar productos, bebidas y clientes, y listarlos con su información completa.
Diseñar con principios SOLID hace que el código sea más fácil de ampliar, corregir y entender: al separar responsabilidades y respetar las relaciones entre clases, podemos agregar nuevas funcionalidades sin romper lo que ya funciona.
