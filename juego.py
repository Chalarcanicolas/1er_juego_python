from tkinter import*
import random

BASE=760
ALTURA=460
intervalo = 10
desplazamiento_x = 1
desplazamiento_y = 1


# funciones de los carros


def mover_carros():
    global desplazamiento_x, desplazamiento_y
    
    x0 = c.coords(carrojg1)
    if x0 < 0 > BASE: 
        desplazamiento_x = -desplazamiento_x
    c.move(carrojg1,desplazamiento_x,1)
    frame_juego.after(10,mover_carros)
#
    c.move(carrojg2,desplazamiento_y,0)
    frame_juego.after(10,mover_carros)
    



#ventana del juego
ventana_principal = Tk()
ventana_principal.title("JUEGO")
ventana_principal.geometry("800x500")
ventana_principal.resizable(False, False)
ventana_principal.config(bg="white")
# centro del juego
frame_juego = Frame(ventana_principal)
frame_juego.config(bg="gray", width=780 , height=480 )
frame_juego.place(x=10 , y=10)
c = Canvas(frame_juego, width=BASE, height=ALTURA)
c.config(bg="gray")
c.place(x=10, y=10)

rect_4 = c.create_rectangle(BASE/2-380,ALTURA/2-100,BASE/2+360,ALTURA/2-220,fill="white", outline="black")


# punto de inicio del carro 1
logo = PhotoImage(file="IMG/carrojg1.png")
carrojg1 = Label(frame_juego, image=logo, bg="white")
carrojg1.place(x=10,y=40)

# punto de inicio del carro 2
logo1 = PhotoImage(file="IMG/carrojg2.png")
carrojg2 = Label(frame_juego, image=logo1, bg="white")
carrojg2.place(x=10,y=300)

# boton para jugar 
bt_convertir = Button(frame_juego,text="Jugar", command=mover_carros)
bt_convertir.place(x=350, y=450, width=100, height=30)

# cartel de salida
lb_salida = Label(ventana_principal, text="S", bg="gray", fg="blue", font=("Helvetica", 20))
lb_salida.place(x=280, y=150)
lb_salida = Label(ventana_principal, text="A", bg="gray", fg="blue", font=("Helvetica", 20))
lb_salida.place(x=280, y=175)
lb_salida = Label(ventana_principal, text="L", bg="gray", fg="blue", font=("Helvetica", 20))
lb_salida.place(x=280, y=200)
lb_salida = Label(ventana_principal, text="I", bg="gray", fg="blue", font=("Helvetica", 20))
lb_salida.place(x=280, y=225)
lb_salida = Label(ventana_principal, text="D", bg="gray", fg="blue", font=("Helvetica", 20))
lb_salida.place(x=280, y=245)
lb_salida = Label(ventana_principal, text="A", bg="gray", fg="blue", font=("Helvetica", 18))
lb_salida.place(x=280, y=275)
#carreta para el carro 1

# cartel de meta 
lb_salida = Label(ventana_principal, text="M", bg="gray", fg="blue", font=("Helvetica", 20))
lb_salida.place(x=720, y=150)
lb_salida = Label(ventana_principal, text="E", bg="gray", fg="blue", font=("Helvetica", 20))
lb_salida.place(x=720, y=190)
lb_salida = Label(ventana_principal, text="T", bg="gray", fg="blue", font=("Helvetica", 20))
lb_salida.place(x=720, y=230)
lb_salida = Label(ventana_principal, text="A", bg="gray", fg="blue", font=("Helvetica", 20))
lb_salida.place(x=720, y=270)

# carretera para el carro 2
rect_4 = c.create_rectangle(BASE/2-380,ALTURA/2+50,BASE/2+360,ALTURA/2+140,fill="white", outline="black")

ventana_principal.mainloop()