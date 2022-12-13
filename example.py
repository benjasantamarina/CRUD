
from cgitb import text
from tkinter import *

raiz=Tk()

mi_frame=Frame()
mi_frame.pack()

#---------------------Pantala--------------------------------------------

numeroPantalla=StringVar()

pantalla=Entry(mi_frame)
pantalla.grid(row=0, column=0, padx=10, pady=10, columnspan=4)
pantalla.config(background="black", fg="#03f943", justify="right")

#---------------------Pulsaciones del teclado----------------------------

def numeroPulsado(num):
    numeroPantalla.set(numeroPantalla.get()+num)

#----------------------Fila 1--------------------------------------------

boton7=Button(mi_frame, text="7", width=3, command=lambda: numeroPulsado("7"))
boton7.grid(row=1, column=0)
boton8=Button(mi_frame, text="8", width=3)
boton8.grid(row=1, column=1)
boton9=Button(mi_frame, text="9", width=3)
boton9.grid(row=1, column=2)
botonDiv=Button(mi_frame, text="/", width=3)
botonDiv.grid(row=1, column=3)

#----------------------Fila 2--------------------------------------------

boton4=Button(mi_frame, text="4", width=3)
boton4.grid(row=2, column=0)
boton5=Button(mi_frame, text="5", width=3)
boton5.grid(row=2, column=1)
boton6=Button(mi_frame, text="6", width=3)
boton6.grid(row=2, column=2)
botonMul=Button(mi_frame, text="X", width=3)
botonMul.grid(row=2, column=3)

#----------------------Fila 3--------------------------------------------

boton1=Button(mi_frame, text="1", width=3)
boton1.grid(row=3, column=0)
boton2=Button(mi_frame, text="2", width=3)
boton2.grid(row=3, column=1)
boton3=Button(mi_frame, text="3", width=3)
boton3.grid(row=3, column=2)
botonRes=Button(mi_frame, text="-", width=3)
botonRes.grid(row=3, column=3)

#----------------------Fila 4--------------------------------------------

boton0=Button(mi_frame, text="0", width=3)
boton0.grid(row=4, column=0)
botonComa=Button(mi_frame, text=",", width=3)
botonComa.grid(row=4, column=1)
botonIgual=Button(mi_frame, text="=", width=3)
botonIgual.grid(row=4, column=2)
botonSum=Button(mi_frame, text="+", width=3)
botonSum.grid(row=4, column=3)




raiz.mainloop()