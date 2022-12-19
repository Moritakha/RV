import pygame
import copy
# import cv2
import tkinter as tk
from tkinter import *
import speech_recognition as sr
# import pyttsx3
# Inicializar
pygame.init()
pygame.display.set_caption("RV")
myfont = pygame.font.SysFont("monospace", 15)
root = Tk()
# Medidas
ANCHO = 1280
ALTO = 720

"""# Colores
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
VERDE = (0, 255, 0)
MARRON = (77, 38, 0)
AZUL = (0, 0, 255)
GRIS = (184, 184, 184)"""

# Mapa


mapa1 = [
    " H           H  ",
    "                ",
    "                ",
    "                ",
    "P               ",
    "                ",
    " H           H  ",
    "                ",
    "                "
]
mapa2 = [
    " H     H     H  ",
    "                ",
    "                ",
    "                ",
    "P               ",
    "                ",
    " H           H  ",
    "                ",
    "                "
]
mapa3 = [
    " H           H  ",
    "                ",
    "                ",
    "                ",
    "P              F",
    "                ",
    " H              ",
    "                ",
    "                "
]

mapa4 = [
    " H     H     H  ",
    "                ",
    "                ",
    "                ",
    "P            F   ",
    "                ",
    " H           H  ",
    "                ",
    "                "
]

# Funciones


def construir_mapa(superficie, mapa):
    limites = []
    frutas = []
    puertas = []
    cuarto = []
    x = 0
    y = 0
    for linea in mapa:
        for baldosa in linea:
            if baldosa == "P":
                puertas.append([baldosa_puerta, pygame.Rect(x, y, 80, 80)])
            elif baldosa == "H":
                cuarto.append([baldosa_cuarto, pygame.Rect(x, y, 80, 80)])
            elif baldosa == "F":
                frutas.append([baldosa_manzana, pygame.Rect(x, y, 80, 80)])
            """if baldosa == "M":
                limites.append([baldosa_muro, pygame.Rect(x, y, 80, 80)])
            elif baldosa == "S":
                limites.append([baldosa_agua, pygame.Rect(x, y, 80, 80)])
            elif baldosa == "A":
                limites.append([baldosa_arbol, pygame.Rect(x, y, 80, 80)])"""
            x += 80
        x = 0
        y += 80
    return limites, frutas, puertas, cuarto


# Ventana

ventana = pygame.display.set_mode((ANCHO, ALTO))
reloj = pygame.time.Clock()
imagen_fondo = pygame.image.load(
    "./pygame_26/fondo.png").convert()
baldosa_cuarto = pygame.image.load(
    "./pygame_26/images.jpg").convert_alpha()
baldosa_puerta = pygame.image.load(
    "./pygame_26/baldosa_puerta.png").convert_alpha()
baldosa_manzana = pygame.image.load(
    "./pygame_26/baldosa_manzana.png").convert_alpha()
"""baldosa_muro = pygame.image.load(
    "./pygame_26/baldosa_muro.png").convert()
baldosa_agua = pygame.image.load(
    "./pygame_26/baldosa_agua.png").convert()
baldosa_arbol = pygame.image.load(
    "./pygame_26/baldosa_arbol.png").convert_alpha()"""


jugador0_par = pygame.image.load(
    ".\pygame_26\par_0.png").convert_alpha()
jugador1_der = pygame.image.load(
    ".\pygame_26\der_1.png").convert_alpha()
jugador2_der = pygame.image.load(
    ".\pygame_26\der_2.png").convert_alpha()
jugador3_der = pygame.image.load(
    ".\pygame_26\der_3.png").convert_alpha()
jugador4_der = pygame.image.load(
    "./pygame_26\der_4.png").convert_alpha()
jugador1_izq = pygame.image.load(
    "./pygame_26\izq_1.png").convert_alpha()
jugador2_izq = pygame.image.load(
    "./pygame_26\izq_2.png").convert_alpha()
jugador3_izq = pygame.image.load(
    "./pygame_26\izq_3.png").convert_alpha()
jugador4_izq = pygame.image.load(
    "./pygame_26\izq_4.png").convert_alpha()
jugador1_arr = pygame.image.load(
    "./pygame_26/arr_1.png").convert_alpha()
jugador2_arr = pygame.image.load(
    "./pygame_26/arr_2.png").convert_alpha()
jugador3_arr = pygame.image.load(
    "./pygame_26/arr_3.png").convert_alpha()
jugador4_arr = pygame.image.load(
    "./pygame_26/arr_4.png").convert_alpha()
jugador1_baj = pygame.image.load(
    "./pygame_26/baj_1.png").convert_alpha()
jugador2_baj = pygame.image.load(
    "./pygame_26/baj_2.png").convert_alpha()
jugador3_baj = pygame.image.load(
    "./pygame_26/baj_3.png").convert_alpha()
jugador4_baj = pygame.image.load(
    "./pygame_26/baj_4.png").convert_alpha()

jugador_imagen = jugador0_par


# Datos

habitacion1 = construir_mapa(ventana, mapa1)
habitacion2 = construir_mapa(ventana, mapa2)
habitacion3 = construir_mapa(ventana, mapa3)
habitacion4 = construir_mapa(ventana, mapa4)

habitacion = habitacion1

jugador_rectangulo = jugador_imagen.get_rect()
print(jugador_rectangulo)
jugador_rectangulo.x = 100
jugador_rectangulo.y = 300
print(jugador_rectangulo)
jugador_vel_x = 0
jugador_vel_y = 0
frames_jugador = 0
# Bucle principal
jugando = True
"""r = sr.Recognizer()
listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)"""
while jugando:
    reloj.tick(60)
    piso = pygame.font.Font(None, 30)
    texto1 = piso.render("324", 0, (0, 0, 0), (255, 255, 255))
    texto2 = piso.render("456", 0, (0, 0, 0), (255, 255, 255))
    texto3 = piso.render("678", 0, (0, 0, 0), (255, 255, 255))
    texto4 = piso.render("899", 0, (0, 0, 0), (255, 255, 255))
    texto5 = piso.render("1045", 0, (0, 0, 0), (255, 255, 255))
    texto6 = piso.render("2670", 0, (0, 0, 0), (255, 255, 255))
    texto7 = piso.render("3456", 0, (0, 0, 0), (255, 255, 255))
    texto8 = piso.render("4983", 0, (0, 0, 0), (255, 255, 255))
    texto9 = piso.render("5266", 0, (0, 0, 0), (255, 255, 255))
    texto10 = piso.render("6982", 0, (0, 0, 0), (255, 255, 255))
    texto11 = piso.render("8450", 0, (0, 0, 0), (255, 255, 255))
    texto12 = piso.render("9123", 0, (0, 0, 0), (255, 255, 255))
    texto13 = piso.render("10765", 0, (0, 0, 0), (255, 255, 255))
    texto14 = piso.render("12890", 0, (0, 0, 0), (255, 255, 255))
    texto15 = piso.render("13876", 0, (0, 0, 0), (255, 255, 255))
    texto16 = piso.render("1489", 0, (0, 0, 0), (255, 255, 255))
    texto17 = piso.render("15000", 0, (0, 0, 0), (255, 255, 255))
    # Eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            jugando = False

    moviendose_derecha = False
    moviendose_izquierda = False
    moviendose_arriba = False
    moviendose_abajo = False

    jugador_vel_x = 0
    jugador_vel_y = 0

    pulsado = pygame.key.get_pressed()

    if pulsado[pygame.K_LEFT] and not pulsado[pygame.K_RIGHT]:
        jugador_vel_x = -3
        moviendose_izquierda = True
    if pulsado[pygame.K_RIGHT] and not pulsado[pygame.K_LEFT]:
        jugador_vel_x = 3
        moviendose_derecha = True
    if pulsado[pygame.K_UP] and not pulsado[pygame.K_DOWN]:
        jugador_vel_y = -3
        moviendose_arriba = True
    if pulsado[pygame.K_DOWN] and not pulsado[pygame.K_UP]:
        jugador_vel_y = 3
        moviendose_abajo = True

    # Lógica

    jugador_rectangulo.x += jugador_vel_x
    jugador_rectangulo.y += jugador_vel_y

    if jugador_rectangulo.x > ANCHO - 60:
        jugador_rectangulo.x = ANCHO - 60
    if jugador_rectangulo.x < 0:
        jugador_rectangulo.x = 0
    if jugador_rectangulo.y > ALTO - 60:
        jugador_rectangulo.y = ALTO - 60
    if jugador_rectangulo.y < 0:
        jugador_rectangulo.y = 0

    for limite in habitacion[0]:
        if jugador_rectangulo.colliderect(limite[1]):
            jugador_rectangulo.x -= jugador_vel_x
            jugador_rectangulo.y -= jugador_vel_y

    for fruta in copy.copy(habitacion[1]):
        if jugador_rectangulo.collidepoint(fruta[1].centerx, fruta[1].centery):
            habitacion[1].remove(fruta)

    for puerta in habitacion[2]:
        if jugador_rectangulo.collidepoint(puerta[1].centerx, puerta[1].centery):
            if habitacion == habitacion1:
                habitacion = habitacion2
                jugador_rectangulo.x = 100
                jugador_rectangulo.y = 300
            elif habitacion == habitacion2:
                habitacion = habitacion3
                jugador_rectangulo.x = 100
                jugador_rectangulo.y = 300
            elif habitacion == habitacion3:
                habitacion = habitacion4
                jugador_rectangulo.x = 100
                jugador_rectangulo.y = 300
            elif habitacion == habitacion4:
                habitacion = habitacion1
                jugador_rectangulo.x = 100
                jugador_rectangulo.y = 300

    # Dibujos
    ventana.blit(imagen_fondo, [0, 0])
    for elemento in habitacion:
        for baldosa in elemento:
            ventana.blit(baldosa[0], baldosa[1])

    if moviendose_derecha:
        frames_jugador += 1
        if frames_jugador >= 21:
            frames_jugador = 1
        if frames_jugador < 6:
            jugador_imagen = jugador1_der
        elif frames_jugador < 11:
            jugador_imagen = jugador2_der
        elif frames_jugador < 16:
            jugador_imagen = jugador3_der
        elif frames_jugador < 21:
            jugador_imagen = jugador4_der

        ventana.blit(jugador_imagen, jugador_rectangulo)

    elif moviendose_izquierda:
        frames_jugador += 1
        if frames_jugador >= 21:
            frames_jugador = 1
        if frames_jugador < 6:
            jugador_imagen = jugador1_izq
        elif frames_jugador < 11:
            jugador_imagen = jugador2_izq
        elif frames_jugador < 16:
            jugador_imagen = jugador3_izq
        elif frames_jugador < 21:
            jugador_imagen = jugador4_izq

        ventana.blit(jugador_imagen, jugador_rectangulo)

    elif moviendose_arriba:
        frames_jugador += 1
        if frames_jugador >= 21:
            frames_jugador = 1
        if frames_jugador < 6:
            jugador_imagen = jugador1_arr
        elif frames_jugador < 11:
            jugador_imagen = jugador2_arr
        elif frames_jugador < 16:
            jugador_imagen = jugador3_arr
        elif frames_jugador < 21:
            jugador_imagen = jugador4_arr

        ventana.blit(jugador_imagen, jugador_rectangulo)

    elif moviendose_abajo:
        frames_jugador += 1
        if frames_jugador >= 21:
            frames_jugador = 1
        if frames_jugador < 6:
            jugador_imagen = jugador1_baj
        elif frames_jugador < 11:
            jugador_imagen = jugador2_baj
        elif frames_jugador < 16:
            jugador_imagen = jugador3_baj
        elif frames_jugador < 21:
            jugador_imagen = jugador4_baj

        ventana.blit(jugador_imagen, jugador_rectangulo)

    else:
        jugador_imagen = jugador0_par
        ventana.blit(jugador_imagen, jugador_rectangulo)
    # Etiquetas
    if habitacion == habitacion1:
        ventana.blit(texto1, (200, 0))
        ventana.blit(texto2, (1150, 0))
        ventana.blit(texto3, (200, 480))
        ventana.blit(texto4, (1150, 480))
    elif habitacion == habitacion2:
        ventana.blit(texto5, (200, 0))
        ventana.blit(texto6, (1150, 0))
        ventana.blit(texto7, (675, 0))
        ventana.blit(texto8, (200, 480))
        ventana.blit(texto9, (1150, 480))
    elif habitacion == habitacion3:
        ventana.blit(texto10, (200, 0))
        ventana.blit(texto11, (1150, 0))
        ventana.blit(texto12, (200, 480))
    elif habitacion == habitacion4:
        ventana.blit(texto13, (200, 0))
        ventana.blit(texto14, (1150, 0))
        ventana.blit(texto15, (675, 0))
        ventana.blit(texto16, (200, 480))
        ventana.blit(texto17, (1150, 480))
        # Reconocimiento de voz (se traba xd)
    r = sr.Recognizer()
    listener = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio, language="es-US")
            print('Has dicho: {}'.format(text))
            print(text)
            if "324" in text:
                jugador_rectangulo.x = 200
                jugador_rectangulo.y = 10
        except:
            print("No entendi")
    # Actualizar
    pygame.display.update()


# Salir
pygame.quit()
