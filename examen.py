#Nombre: Martin Valdes
#RUT: 22.353.311-6
#Asignatura Programacion
#Seccion 002D




productos = {
    "8475HD": ["HP", "15.6", "8GB", "DD", "1T", "Intel Core i5", "Nvidia GTX1050"],
    "2175HD": ["Acer", "14", "4GB", "SSD", "512GB", "Intel Core i5", "Nvidia GTX1050"],
    "JjfFHD": ["Asus", "14", "16GB", "SSD", "256GB", "Intel Core i7", "Nvidia RTX2080Ti"],
    "fgdxFHD": ["HP", "15.6", "12GB", "SD", "1TB", "Intel Core i3", "integrada"],
    "GF75HD": ["Asus", "15.6", "12GB", "DD", "1TB", "Intel Core 7", "Nvidia GTX1050"],
    "123FHD": ["Acer", "14", "6GB", "DD", "1TB", "ADM Ryzen 5", "integrada"],
    "324FHD": ["Acer", "15.6", "8GB", "DD", "1TB", "ADM Ryzen 7", "Nvidia GTX1050"],
    "UWU131HD": ["Dell", "15.6", "8GB", "DD", "1TB", "ADM Ryzen 3", "Nvidia GTX1050"],    
}

stock = {
    "8475HD": [387990, 10],
    "2175HD": [327990, 1],
    "JjfFHD": [424990, 1],
    "fgdxFHD": [664990, 21],
    "GF75HD": [749990, 2],
    "123FHD": [290890, 32],
    "324FHD": [444990, 7],
    "UWU131HD": [349990, 1],
    "FS1230HD": [249990, 0]    
}

def stock_marca(marca):
    # suma stock para todos los productos de esa marca, marca insensible a mayus/minus
    marca = marca.lower()
    total_stock = 0
    for modelo, info in productos.items():
        if info[0].lower() == marca:
            # chequear si el modelo está en stock
            if modelo in stock:
                total_stock += stock[modelo][1]
    print(f"El stock es: {total_stock}")

def buscar_precio(p_min, p_max):
    resultados = []
    for modelo, info_stock in stock.items():
        precio = info_stock[0]
        cantidad = info_stock[1]
        if cantidad > 0 and p_min <= precio <= p_max:
            if modelo in productos:
                marca = productos[modelo][0]
                resultados.append(f"{marca}--{modelo}")
    if resultados:
        resultados.sort()
        print(f"Los notebooks entre los precios consultas son: {resultados}")
    else:
        print("No hay notebooks en ese rango de precios.")

def eliminar_producto(modelo):
    if modelo in productos:
        productos.pop(modelo)
        if modelo in stock:
            stock.pop(modelo)
        return True
    else:
        return False

def pedir_entero(mensaje):
    while True:
        try:
            valor = int(input(mensaje))
            return valor
        except:
            print("Debe ingresar valores enteros!!")

def main():
    while True:
        print("\n***MENU PRINCIPAL***")
        print("1. Stock marca.")
        print("2. Busqueda por precio.")
        print("3. Eliminar producto.")
        print("4. Salir.")
        opcion = input("Ingrese opcion: ").strip()

        if opcion == "1":
            marca = input("Ingrese marca a consultar: ").strip()
            stock_marca(marca)

        elif opcion == "2":
            while True:
                p_min = pedir_entero("Ingrese precio minimo: ")
                p_max = pedir_entero("Ingrese precio maximo: ")
                if p_min <= p_max:
                    break
                else:
                    print("El precio minimo debe ser menor o igual al precio maximo. Intente nuevamente.")
            buscar_precio(p_min, p_max)

        elif opcion == "3":
            while True:
                modelo = input("Ingrese modelo a actualizar: ").strip()
                eliminado = eliminar_producto(modelo)
                if eliminado:
                    print("Producto eliminado!!")
                else:
                    print("El modelo no existe!!")
                resp = input("Desea eliminar otro producto (s/n): ").strip().lower()
                if resp != "si" and resp != "s":
                    break

        elif opcion == "4":
            print("Programa finalizado.")
            break

        else:
            print("Debe seleccionar una opcion valida!")

if __name__ == "__main__":
    main()
