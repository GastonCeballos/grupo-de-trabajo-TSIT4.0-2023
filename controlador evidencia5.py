import evidencia5


def listarproducto():
    con = modelo.conectar()
    listado = con.listarproducto()
    print("\n| id_producto   |   codigo_producto    |   nombre_producto |   stock   |   precio   |  id_recetas   |")
    for producto in listado:
        print(' ',producto[0],"\t\t",producto[1],"\t\t",str(producto[2])+"\t\t"+str(producto[3]),"\t\t $"+str(producto[4]),"\t\t",producto[5])
    input("Para continuar presione enter")

def InsertarProducto():
    con = modelo.conectar()

    nombre_producto = input("\ningrese el nombre del producto: ")
    codigo_producto = input("\ningrese el codigo del producto: ")
    stock = int(input("\ningrese el stock del producto: " ))
    precio= int(input("\ningrese el precio del producto: "))

    nuevoproducto= modelo.producto(0,codigo_producto,nombre_producto,stock,precio,0)

    con.insertarproducto(nuevoproducto)
    input("Para continuar presione enter")
