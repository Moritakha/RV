import tkinter
from tkinter import messagebox, Button, Frame
from tkinter.ttk import Progressbar
import random

ventana = tkinter.Tk()
ancho = 720
alto = 640
x_ventana = ventana.winfo_screenwidth() // 2 - ancho // 2
ventana.geometry(f"{ancho}x{alto}+{x_ventana}+0")


def helloCallBack():
   messagebox.showinfo("Hello Python", "Hello World")


frame1 = Frame(ventana, bg='black', width=600, height=350)
frame1.grid(column=0, row=0, sticky='nsew')
frame2 = Frame(ventana, bg='black', width=600, height=50)
frame2.grid(column=0, row=1, sticky='nsew')
frame3 = Frame(ventana, bg='black', width=600, height=50)
frame3.grid(column=0, row=1, sticky='nsew')

barra1 = Progressbar(frame1, orient='vertical', length=300,  maximum=300,
                     style="Vertical.TProgressbar")  # ,takefocus=True mode='determinate',
barra1.grid(column=0, row=0, padx=1)
barra2 = Progressbar(frame1, orient='vertical', length=300,
                     maximum=300, style="Vertical.TProgressbar")
barra2.grid(column=1, row=0, padx=1)
barra3 = Progressbar(frame1, orient='vertical', length=300,
                     maximum=300, style="Vertical.TProgressbar")
barra3.grid(column=2, row=0, padx=1)
barra4 = Progressbar(frame1, orient='vertical', length=300,
                     maximum=300, style="Vertical.TProgressbar")
barra4.grid(column=3, row=0, padx=1)
barra5 = Progressbar(frame1, orient='vertical', length=300,
                     maximum=300, style="Vertical.TProgressbar")
barra5.grid(column=4, row=0, padx=1)
barra6 = Progressbar(frame1, orient='vertical', length=300,
                     maximum=300, style="Vertical.TProgressbar")
barra6.grid(column=5, row=0, padx=1)
barra7 = Progressbar(frame1, orient='vertical', length=300,
                     maximum=300, style="Vertical.TProgressbar")  # ,takefocus=True
barra7.grid(column=6, row=0, padx=1)
barra8 = Progressbar(frame1, orient='vertical', length=300,
                     maximum=300, style="Vertical.TProgressbar")
barra8.grid(column=7, row=0, padx=1)
barra9 = Progressbar(frame1, orient='vertical', length=300,
                     maximum=300, style="Vertical.TProgressbar")
barra9.grid(column=8, row=0, padx=1)
barra10 = Progressbar(frame1, orient='vertical', length=300,
                      maximum=300, style="Vertical.TProgressbar")
barra10.grid(column=9, row=0, padx=1)
barra11 = Progressbar(frame1, orient='vertical', length=300,
                      maximum=300, style="Vertical.TProgressbar")
barra11.grid(column=10, row=0, padx=1)
barra12 = Progressbar(frame1, orient='vertical', length=300,
                      maximum=300, style="Vertical.TProgressbar")
barra12.grid(column=11, row=0, padx=1)
barra13 = Progressbar(frame1, orient='vertical', length=300,
                      maximum=300, style="Vertical.TProgressbar")
barra13.grid(column=12, row=0, padx=1)
barra14 = Progressbar(frame1, orient='vertical', length=300,
                      maximum=300, style="Vertical.TProgressbar")
barra14.grid(column=13, row=0, padx=1)
barra15 = Progressbar(frame1, orient='vertical', length=300,
                      maximum=300, style="Vertical.TProgressbar")
barra15.grid(column=14, row=0, padx=1)
barra16 = Progressbar(frame1, orient='vertical', length=300,
                      maximum=300, style="Vertical.TProgressbar")
barra16.grid(column=15, row=0, padx=1)
barra17 = Progressbar(frame1, orient='vertical', length=300,
                      maximum=300, style="Vertical.TProgressbar")
barra17.grid(column=16, row=0, padx=1)
barra18 = Progressbar(frame1, orient='vertical', length=300,
                      maximum=300, style="Vertical.TProgressbar")
barra18.grid(column=17, row=0, padx=1)
barra19 = Progressbar(frame1, orient='vertical', length=300,
                      maximum=300, style="Vertical.TProgressbar")
barra19.grid(column=18, row=0, padx=1)
barra20 = Progressbar(frame1, orient='vertical', length=300,
                      maximum=300, style="Vertical.TProgressbar")
barra20.grid(column=19, row=0, padx=1)

tiempo = Progressbar(frame2, orient='horizontal', length=390,
                     mode='determinate', style="Horizontal.TProgressbar")
tiempo.grid(row=0, columnspan=8, padx=5)
lista = []
for i in range(50, 200, 10):
	lista.append(i)


x = 0
tt = 5


def iniciar_reproduccion():
	# global cancion_actual, direcion, pos, n, actualizar
	barra1['value'] = random.choice(lista)
	barra2['value'] = random.choice(lista)
	barra3['value'] = random.choice(lista)
	barra4['value'] = random.choice(lista)
	barra5['value'] = random.choice(lista)
	barra6['value'] = random.choice(lista)
	barra7['value'] = random.choice(lista)
	barra8['value'] = random.choice(lista)
	barra9['value'] = random.choice(lista)
	barra10['value'] = random.choice(lista)
	barra11['value'] = random.choice(lista)
	barra12['value'] = random.choice(lista)
	barra13['value'] = random.choice(lista)
	barra14['value'] = random.choice(lista)
	barra15['value'] = random.choice(lista)
	barra16['value'] = random.choice(lista)
	barra17['value'] = random.choice(lista)
	barra18['value'] = random.choice(lista)
	barra19['value'] = random.choice(lista)
	barra20['value'] = random.choice(lista)
	actualizar = ventana.after(100, iniciar_reproduccion)
    # if x== tt:
    #     ventana.after_cancel(actualizar)
	# if x == tt:
    #     ventana.after_cancel(actualizar)
    #     detener_efecto()
    #     x = 0
    # else:
    #     x+=1


def detener_efecto():
	barra1['value'] = 50
	barra2['value'] = 60
	barra3['value'] = 70
	barra4['value'] = 80
	barra5['value'] = 90
	barra6['value'] = 100
	barra7['value'] = 90
	barra8['value'] = 80
	barra9['value'] = 70
	barra10['value'] = 60
	barra11['value'] = 60
	barra12['value'] = 70
	barra13['value'] = 80
	barra14['value'] = 90
	barra15['value'] = 100
	barra16['value'] = 90
	barra17['value'] = 80
	barra18['value'] = 70
	barra19['value'] = 60
	barra20['value'] = 50

boton1 = Button(frame2, command= iniciar_reproduccion)

boton1.config(text=,)
boton1.place(x=500,y=500,
            height=260,width=260)
ventana.mainloop()


# import pygame
# import copy
# # import cv2
# import tkinter as tk
# from tkinter import *
# import speech_recognition as sr
# # import pyttsx3
# # Inicializar
# pygame.init()
# pygame.display.set_caption("RV")
# myfont = pygame.font.SysFont("monospace", 15)
# root = Tk()

# r = sr.Recognizer()
#     listener = sr.Recognizer()
#     with sr.Microphone() as source:
#         print("Empieza  a reconocer ......................................")
#         seconds = 3
#         audio = r.listen(source,seconds)
#         print(f"Termina en {seconds} segundos ......................................")
#         try:
#             text = r.recognize_google(audio, language="es-US")
#             print('Has dicho: {}'.format(text))
#             print(text)
#             if "324" in text:
#                 jugador_rectangulo.x = 200
#                 jugador_rectangulo.y = 10
#         except:
#             print("No entendi")