productos = []
producto = None

try:
    producto = {
        "nombre": input("Producto: "),
        "precio": float(input("Precio : $")),
        "stock": int(input("Stock: "))
    }
except:
    print("ERROR! Revisa como ingresaste tu último dato, por favor")
    
if producto != None:
    productos.append(producto)
print(productos)