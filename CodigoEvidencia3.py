import sys
import datetime
import sqlite3
from sqlite3 import Error
 
yellow = '\033[33m'
white = '\033[37m'
green = '\033[32m'
 
inventario=("Codigo", "Fecha", "Articulo", "Piezas", "Precio","Total")
Lista_articulos = []
switch = True
clave={}
registro = []
total=[]
precio_final = 0
numero_venta=0
 
while switch:
    try:
        with sqlite3.connect("NegocioDeVentasCosméticos.db") as conn:  
            c = conn.cursor()
            c.execute("CREATE TABLE IF NOT EXISTS ventas (folio INTEGER PRIMARY KEY, cantidad INTEGER, articulo TEXT NOT NULL, price float, total float, fecha);")
            print("Tabla creada")
    except Error as e:
        print(e)
        switch = False
    except:
        print(f"Se produjo el siguiente error: {sys.exc_info()[0]}")
        switch = False
    else: 
        print(green + "||| Bienvendio al Menú |||")
        print(white)
        print("¿Que accion vas a realizar?")
        print("1-Registrar ventas")
        print("2-Consultar ventas")
        print("3-Reporte de ventas")
        print("4-Salir del programa")
        opcion = int(input("¿Que opcion vas a elegir?: \n"))
        if opcion == 1:
            print(green + "---Registro de las ventas---")
            print(white)
            
            while opcion == 1:
                numero_venta=numero_venta+1

                folio = int(input("Ingresa el folio de la venta: "))
                cantidad = int(input ("Ingresa la cantidad de piezas adquiridas: \n"))
                articulo=input("¿Que articulo fue vendido? : \n")
                price= float(input(f"¿A que precio fue vendido el {articulo}?: \n"))
                total = cantidad * price
                fecha = datetime.datetime.combine(datetime.date.today(), datetime.datetime.min.time())
                valores = {"folio":folio, "cantidad":cantidad, "articulo":articulo, "price":price, "total":total, "fecha":fecha}
                try:
                    with sqlite3.connect("NegocioDeVentasCosméticos.db") as conn:
                        c = conn.cursor()
                        c.execute("INSERT INTO ventas VALUES (:folio, :cantidad, :articulo, :price, :total, :fecha)",valores)
                        print(f" El total a pagar es: {total}")
                        print("El folio de venta es: {folio}") 
                except Error as e:
                    print(e)   
                except:
                    print(f"El error que se esta presentando es: {sys.exc_info()[0]}")
                else:
                    print("Registro hecho exitosamente")
                opcion = int(input(" Deseas ingresar otra venta: 1.- Si / 0.- No: "))
                if opcion == 0:
                    print(yellow)
                    print(white)
                    Lista_articulos.append(registro)
                    respuestaW=int(input("Desea realizar otra venta?:  1 - Si o 0 - No\n"))
                    if opcion == 0:
                        switch == True
    finally:
        conn.close()