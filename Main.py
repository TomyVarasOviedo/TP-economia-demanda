import pandas as pd
import matplotlib.pyplot as plt

info = pd.read_csv('dataset_demanda_electrodomesticos.csv')

# FUNCIONES
def covarianza():
    return ((precio - precio.mean())*(cantidad - cantidad.mean())).mean()

def variancia(data:pd):
    return ((data - data.mean())**2).mean()

def ordenada(dependiente:pd, pendiente:float, independiente:pd):
    return dependiente.mean() - pendiente * independiente.mean()
def mostrarGrafico():
    plt.scatter(info['cantidad'],info['precio'], color='blue')
    plt.plot(info['cantidad'], pendienteCantidad*info['cantidad'] + ordenadaCantidad, color='red', label='Demanda precio')
    plt.xlabel('Precio')
    plt.ylabel('Cantidad')
    plt.legend()
    plt.show()
# FUNCIONES

precio = info['precio']
cantidad=info['cantidad']
pendientePrecio = covarianza()/variancia(precio)
pendienteCantidad = covarianza()/variancia(cantidad)
ordenadaCantidad = ordenada(precio, pendienteCantidad, cantidad)
ordenadaPrecio=ordenada(cantidad, pendientePrecio, precio)
