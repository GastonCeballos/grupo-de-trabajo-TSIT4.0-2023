import mysql.connector

class conectar():

    def __init__(self) -> None:
        try:
            self.conexion = mysql.connector.connect(
                host = 'localhost',
                port = 3306,
                user = 'root',
                password = 'Gastc700822',
                db = 'bdbigbreadsa'

            )
        except mysql.connector.error as desciptionError:
            print("No se conecto!",desciptionError)

    def ListarProductos(self):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sentenciaSQL = "selec * FROM Productos"
                cursor.execute(sentenciaSQL)
                resultados = cursor.fetchall()
                self.conexion.close()
                return resultados
            
            except mysql.connector.Error as descriptionError:
                print("No se conecto!",descriptionError)

    def InsertarProducto(self,producto):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sentenciaSQL = "INSERT into productos values(null,%s,%s,%s,%s,null)"

                data = (producto.getnombre_producto(),
                        producto.getcodigo_producto(),
                        producto.getstock(),
                        producto.getprecio()
                        )
                
                cursor.execute(sentenciaSQL,data)

                self.conexion.commit()
                self.conexion.close()
                print("Producto insertado correctamente")

            except mysql.connector.Error as descrptionError:
                print("No se conecto!",descrptionError)

class Producto():
    id_producto =0,
    nombre_producto = "",
    stock =0,
    precio = 0,
    id_receta = 0


    def __init__(self,id_producto, nombre_producto, stock, precio, id_receta):
        self.id_producto = id_producto
        self.nombre_producto = nombre_producto
        self.stock = stock
        self.precio = precio
        self.id_receta = id_receta

    def getid_producto(self):
        return self.id_producto

    def getnombre_producto(self):
        return self.nombre_producto

    def getstock(self):
        return self.stock

    def getprecio(self):
        return self.precio

    def getiD_Receta(self):
        return self.id_receta

    def setiD_Producto(self,id_producto): 
        self.id.producto = id_producto

    def setnombre_producto(self,nombre_producto):
        self.nombre_producto = nombre_producto

    def setstock (self, stock):
        self.stock = stock

    def setprecio(self,precio):
        self.precio = precio

    def setgetunidad_de_medida(self,getunidad_de_medida):
        self.getunidad_de_medida = getunidad_de_medida

    def setiD_Receta(self,id_receta):
        self.id_receta = id_receta
        