from tkinter import *
from tkinter import messagebox
#variables

work_time=25*60
tiempo_descanso=5*60
BG_COLOR_TRABAJO= "#f26419"
BG_COLOR_DESCANSO = "#86bbd8"

class ventana:
    def __init__(self,interfaz):
        self.ventana=interfaz
        self.ventana.config(bg=BG_COLOR_TRABAJO)
        self.ventana.geometry("250x250")
        self.ventana.title("Pomodoro")
        self.ventana.resizable(width=False,height=False)
        self.header_T()
        self.timer_text()
        self.paused()
        self.btn_start()


    def header_T(self):
        self.header=Label(self.ventana,text="Pomodoro",font=('roboto',35,'bold'))
        self.header.pack(side=TOP,pady=10)
        self.header.config(bg=BG_COLOR_TRABAJO,fg='#fff')

    def timer_text(self):
        self.timer_str=StringVar()
        self.timer_str.set("25:00")
        self.timer_t=Label(self.ventana,font=('roboto', 70, 'bold'),textvariable=self.timer_str)
        self.timer_t.config(bg=BG_COLOR_TRABAJO,fg="#fff")
        self.timer_t.pack(anchor="center")

    def btn_start(self):
        btn=Button(self.ventana,text="Inicio",font=('roboto',20,'bold'),command=lambda: self.C_time(int(work_time)))
        btn.config(bg="#f6ae2d",fg="#000",borderwidth=0)
        btn.pack(side=BOTTOM,pady=5)

    def paused(self):
        self.edo_str=StringVar()
        self.edo_str.set("PAUSADO")
        self.str_p=Label(self.ventana,textvariable=self.edo_str,font="roboto 15")
        self.str_p.config(bg=BG_COLOR_TRABAJO,fg='#fff',padx=0,pady=0)
        self.str_p.pack()

    def cambiar_color(self,color="#fff"):
        self.timer_t.config(bg=color,fg="#fff")
        self.ventana.config(bg=color)
        self.header.config(bg=color,fg="#fff")
        self.str_p.config(bg=color,fg="#fff")

    def C_time(self,tiempo,Primera_ejecucion=True):
        if Primera_ejecucion:
            self.edo_str.set("Trabajando")
        if tiempo<=0:
            if self.edo_str.get()=="Trabajando":
                messagebox.showinfo(message="Hora de descansar!", title="Alerta")
                tiempo=tiempo_descanso
                self.edo_str.set("Descanso")
                self.cambiar_color(BG_COLOR_DESCANSO)
                self.ventana.update_idletasks()
            else:
                messagebox.showinfo(message="Hora de Trabajar!", title="Alerta")
                tiempo=work_time
                self.cambiar_color(BG_COLOR_TRABAJO)
                self.edo_str.set("Trabajando")
                self.ventana.update_idletasks()
        mins,secs=divmod(tiempo,60)
        Contador='{:02d}:{:02d}'.format(mins,secs)
        self.timer_str.set(Contador)
        self.ventana.update_idletasks()
        tiempo-=1
        self.ventana.after(1000,self.C_time,tiempo,False)









