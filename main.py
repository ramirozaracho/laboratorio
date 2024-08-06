import os
import platform

from producto import (
    ProductoElectronico,
    ProductoAlimenticio,
    Inventario,
)

def limpiar_pantalla():
    ''' Limpiar la pantalla según el sistema operativo'''
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear') # Para Linux/Unix/MacOs

def mostrar_menu():
    print("========== Menú de Productos ==========")
    print('1. Agregar Producto Electronico')
    print('2. Agregar Producto Alimenticio')
    print('3. Buscar Producto por Precio')
    print('4. Actualizar Producto')
    print('5. Eliminar Producto')
    print('6. Mostrar Todos los Productos')
    print('7. Salir')
    print('======================================================')

def agregar_producto(gestion, tipo_producto):
    try:        
        nombre = input('Ingrese nombre del producto: ')
        precio = float(input('Ingrese precio del producto: '))
        cantidad = int(input('Ingrese cantidad de productos: '))
        

        if tipo_producto == '1':
            garantia = input('Ingrese la garantia del producto: ')
            producto = ProductoElectronico(nombre, precio, cantidad, garantia)
        elif tipo_producto == '2':
            fecha_expiracion = int(input('Ingrese la fecha de vencimiento: '))
            producto = ProductoAlimenticio(nombre, precio, cantidad, fecha_expiracion)
        else:
            print('Opción inválida')
            return

        gestion.crear_producto(producto)
        input('Presione enter para continuar...')

    except ValueError as e:
        print(f'Error: {e}')
    except Exception as e:
        print(f'Error inesperado: {e}')

def buscar_producto_por_nombre(gestion):
    nombre = input('Ingrese el nombre del producto a buscar: ')
    gestion.listar_productos(nombre)
    input('Presione enter para continuar...')

def actualizar_producto(gestion):
    tipo = input('Ingrese el tipo de producto para actualizar: ')
    cantidad = int(input('Ingrese la cantidad de productos'))
    gestion.actualizar_producto(tipo, cantidad)
    input('Presione enter para continuar...')

def eliminar_producto(gestion):
    nombre = input('Ingrese el nombre del producto a eliminar: ')
    gestion.eliminar_producto(nombre)
    input('Presione enter para continuar...')

def mostrar_todos_los_productos(gestion):
    print('=============== Listado completo de los Productos ==============')
    for producto in gestion.guardar_datos().values():
        if 'garantia' in producto:
            print(f"{producto['nombre']} - garantia {producto['garantia']}")
        else:
            print(f"{producto['nombre']} - fecha expiracion {producto['fecha_expiracion']}")
    print('=====================================================================')
    input('Presione enter para continuar...')


if __name__ == "__main__":
    archivo_productos = 'inventario.json'
    gestion = Inventario(archivo_productos)

    while True:
        limpiar_pantalla()
        mostrar_menu()
        opcion = input('Seleccione una opción: ')

        if opcion == '1' or opcion == '2':
            agregar_producto(gestion, opcion)
        
        elif opcion == '3':
            buscar_producto_por_nombre(gestion)

        elif opcion == '4':
            actualizar_producto(gestion)

        elif opcion == '5':
            eliminar_producto(gestion)

        elif opcion == '6':
            mostrar_todos_los_productos(gestion)

        elif opcion == '7':
            print('Saliendo del programa...')
            break
        else:
            print('Opción no válida. Por favor, seleccione una opción válida (1-7)')