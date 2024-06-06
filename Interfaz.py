import customtkinter as ctk

import Main
import Viajeros

def graficoElectrodomesticos():
    Main.mostrarGrafico()
def graficoViajeros():
    Viajeros.mostrarGrafico()
ventana = ctk.CTk()
ventana.title("Estimacion de la demanda")
ventana.geometry("400x300")

frame = ctk.CTkFrame(ventana)
frame.pack(pady=20)
titulo = ctk.CTkLabel(master=ventana,text="Estimacion de la demanda", font=("Roboto", 16))
titulo.pack(side="top",padx=20)

boton1 = ctk.CTkButton(frame, text="Demanda de electrodomesticos", command=graficoElectrodomesticos)
boton2 = ctk.CTkButton(frame, text="Demanda de hoteles", command=graficoViajeros)

boton1.pack(side="left", padx=10)
boton2.pack(side="left", padx=10)

ventana.mainloop()