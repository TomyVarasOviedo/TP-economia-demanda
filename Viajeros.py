import pandas as pd
import matplotlib.pyplot as plt

info = pd.read_csv('viajeros-hospedados-residentes-y-no-residentes.csv')

# FUNCIONES
def covarianza(precio:pd, cantidad):
    return ((precio - precio.mean())*(cantidad - cantidad.mean())).mean()

def variancia(data:pd):
    return ((data - data.mean())**2).mean()

def ordenada(dependiente:pd, pendiente:float, independiente:pd):
    return dependiente.mean() - pendiente * independiente.mean()
def mostrarGrafico():
    plt.scatter(periodos,info['viajeros'], color='blue')
    plt.plot(periodos, pendiente*periodos + ordenadaViajeros, color='red', label='Demanda precio')
    plt.xlabel('Periodos')
    plt.ylabel('Cantidad de viajeros')
    plt.legend()
    plt.show()
# FUNCIONES
periodos = pd.to_datetime(info['indice_tiempo'])
periodos = (periodos - periodos.min()).dt.days

pendiente=covarianza(info['viajeros'], periodos)/variancia(periodos)
ordenadaViajeros=ordenada(info['viajeros'],pendiente, periodos)



