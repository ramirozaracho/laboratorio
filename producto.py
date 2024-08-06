#Desafío 1: Sistema de Gestión de Productos
#Objetivo: Desarrollar un sistema para manejar productos en un inventario.

#Requisitos:

#Crear una clase base Producto con atributos como nombre, precio, cantidad en stock, etc.
#Definir al menos 2 clases derivadas para diferentes categorías de productos (por ejemplo, ProductoElectronico, ProductoAlimenticio) con atributos y métodos específicos.
#Implementar operaciones CRUD para gestionar productos del inventario.
#Manejar errores con bloques try-except para validar entradas y gestionar excepciones.
#Persistir los datos en archivo JSON.


import json

class Producto:
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

    def to_dict(self):
        return {
            'nombre': self.nombre,
            'precio': self.precio,
            'cantidad': self.cantidad
        }

    @classmethod
    def from_dict(cls, data):
        return cls(data['nombre'], data['precio'], data['cantidad'])

class ProductoElectronico(Producto):
    def __init__(self, nombre, precio, cantidad, garantia):
        super().__init__(nombre, precio, cantidad)
        self.garantia = garantia

    def to_dict(self):
        data = super().to_dict()
        data['garantia'] = self.garantia
        return data

    @classmethod
    def from_dict(cls, data):
        return cls(data['nombre'], data['precio'], data['cantidad'], data['garantia'])

class ProductoAlimenticio(Producto):
    def __init__(self, nombre, precio, cantidad, fecha_expiracion):
        super().__init__(nombre, precio, cantidad)
        self.fecha_expiracion = fecha_expiracion

    def to_dict(self):
        data = super().to_dict()
        data['fecha_expiracion'] = self.fecha_expiracion
        return data

    @classmethod
    def from_dict(cls, data):
        return cls(data['nombre'], data['precio'], data['cantidad'], data['fecha_expiracion'])

class Inventario:
    def __init__(self, archivo='inventario.json'):
        self.archivo = archivo
        self.productos = self.cargar_datos()

    def cargar_datos(self):
        try:
            with open(self.archivo, 'r') as f:
                datos = json.load(f)
                return [self.crear_producto(p) for p in datos]
        except FileNotFoundError:
            return []
        except json.JSONDecodeError:
            return []

    def crear_producto(self, datos):
        tipo = datos.get('tipo')
        if tipo == 'electronico':
            return ProductoElectronico.from_dict(datos)
        elif tipo == 'alimenticio':
            return ProductoAlimenticio.from_dict(datos)
        else:
            raise ValueError("Tipo de producto desconocido")

    def guardar_datos(self):
        try:
            with open(self.archivo, 'w') as f:
                json.dump([p.to_dict() for p in self.productos], f, indent=4)
        except IOError as e:
            print(f"Error al guardar los datos: {e}")

    def agregar_producto(self, producto):
        self.productos.append(producto)
        self.guardar_datos()

    def eliminar_producto(self, nombre):
        self.productos = [p for p in self.productos if p.nombre != nombre]
        self.guardar_datos()

    def actualizar_producto(self, nombre, **kwargs):
        for p in self.productos:
            if p.nombre == nombre:
                if 'precio' in kwargs:
                    p.precio = kwargs['precio']
                if 'cantidad' in kwargs:
                    p.cantidad = kwargs['cantidad']
                if isinstance(p, ProductoElectronico) and 'garantia' in kwargs:
                    p.garantia = kwargs['garantia']
                if isinstance(p, ProductoAlimenticio) and 'fecha_expiracion' in kwargs:
                    p.fecha_expiracion = kwargs['fecha_expiracion']
                self.guardar_datos()
                break
        else:
            print("Producto no encontrado")

    def listar_productos(self):
        for p in self.productos:
            print(f"Nombre: {p.nombre}, Precio: {p.precio}, Cantidad: {p.cantidad}")
            if isinstance(p, ProductoElectronico):
                print(f"  Garantía: {p.garantia}")
            elif isinstance(p, ProductoAlimenticio):
                print(f"  Fecha de Expiración: {p.fecha_expiracion}")



