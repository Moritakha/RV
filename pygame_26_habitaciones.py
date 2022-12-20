import pygame
import copy
from tkinter import *
import speech_recognition as sr
import pyttsx3
# Inicializar
pygame.init()
pygame.display.set_caption("RV")
myfont = pygame.font.SysFont("monospace", 15)
root = Tk()
# Medidas
ANCHO = 1280
ALTO = 720

# Mapa


mapa1 = [
    "H            H  ",
    "                ",
    "                ",
    "                ",
    "P               ",
    "                ",
    "H            H  ",
    "                ",
    "                "
]
mapa2 = [
    "H     H      H  ",
    "                ",
    "                ",
    "                ",
    "P               ",
    "                ",
    "H            H  ",
    "                ",
    "                "
]
mapa3 = [
    "H            HF ",
    "                ",
    "                ",
    "                ",
    "P               ",
    "                ",
    "H               ",
    "                ",
    "                "
]

mapa4 = [
    "H     H      H  ",
    "                ",
    "                ",
    "                ",
    "P               ",
    "                ",
    "H            H  ",
    "              F ",
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
            x += 80
        x = 0
        y += 80
    return limites, frutas, puertas, cuarto


# Ventana

ventana = pygame.display.set_mode((ANCHO, ALTO))
reloj = pygame.time.Clock()
imagen_fondo = pygame.image.load(
    "./imgs/fondo.jpg").convert()
baldosa_cuarto = pygame.image.load(
    "./imgs/images3.jpg").convert_alpha()
baldosa_puerta = pygame.image.load(
    "./imgs/baldosa_puerta.png").convert_alpha()
baldosa_manzana = pygame.image.load(
    "./imgs/baldosa_manzana.png").convert_alpha()


jugador0_par = pygame.image.load(
    ".\imgs\par_0.png").convert_alpha()
jugador1_der = pygame.image.load(
    ".\imgs\der_1.png").convert_alpha()
jugador2_der = pygame.image.load(
    ".\imgs\der_2.png").convert_alpha()
jugador3_der = pygame.image.load(
    ".\imgs\der_3.png").convert_alpha()
jugador4_der = pygame.image.load(
    "./imgs\der_4.png").convert_alpha()
jugador1_izq = pygame.image.load(
    "./imgs\izq_1.png").convert_alpha()
jugador2_izq = pygame.image.load(
    "./imgs\izq_2.png").convert_alpha()
jugador3_izq = pygame.image.load(
    "./imgs\izq_3.png").convert_alpha()
jugador4_izq = pygame.image.load(
    "./imgs\izq_4.png").convert_alpha()
jugador1_arr = pygame.image.load(
    "./imgs/arr_1.png").convert_alpha()
jugador2_arr = pygame.image.load(
    "./imgs/arr_2.png").convert_alpha()
jugador3_arr = pygame.image.load(
    "./imgs/arr_3.png").convert_alpha()
jugador4_arr = pygame.image.load(
    "./imgs/arr_4.png").convert_alpha()
jugador1_baj = pygame.image.load(
    "./imgs/baj_1.png").convert_alpha()
jugador2_baj = pygame.image.load(
    "./imgs/baj_2.png").convert_alpha()
jugador3_baj = pygame.image.load(
    "./imgs/baj_3.png").convert_alpha()
jugador4_baj = pygame.image.load(
    "./imgs/baj_4.png").convert_alpha()

jugador_imagen = jugador0_par


# Datos

piso1 = construir_mapa(ventana, mapa1)
piso2 = construir_mapa(ventana, mapa2)
piso3 = construir_mapa(ventana, mapa3)
piso4 = construir_mapa(ventana, mapa4)

piso = piso1

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


def rv():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio, language="es-US")
            print('Has dicho: {}'.format(text))
            print(text)
            if "324" in text or "1045" in text or "6982" in text or "10765" in text:
                jugador_rectangulo.x = 100
                jugador_rectangulo.y = 0
            elif "3456" in text or "13876" in text:
                jugador_rectangulo.x = 550
                jugador_rectangulo.y = 0
            elif "456" in text or "2670" in text or "8450" in text or "12890" in text:
                jugador_rectangulo.x = 1150
                jugador_rectangulo.y = 0
            elif "678" in text or "4983" in text or "9123" in text or "1489" in text:
                jugador_rectangulo.x = 100
                jugador_rectangulo.y = 480
            elif "899" in text or "5266" in text or "15000" in text:
                jugador_rectangulo.x = 1150
                jugador_rectangulo.y = 480
            elif "puerta" in text:
                jugador_rectangulo.x = 100
                jugador_rectangulo.y = 300
            elif "piso" in text:
                jugador_rectangulo.x = 20
                jugador_rectangulo.y = 350
        except:
            engine = pyttsx3.init()
            voices = engine.getProperty('voices')
            engine.setProperty('voice', voices[0].id)
            engine.say("No entendi")
            engine.runAndWait()
            #print("No entendi")


while jugando:
    reloj.tick(60)
    winmensaje = pygame.font.SysFont("Comic Sans", 90)
    aula = pygame.font.Font(None, 30)
    texto1 = aula.render("324", 0, (0, 0, 0), (255, 255, 255))
    texto2 = aula.render("456", 0, (0, 0, 0), (255, 255, 255))
    texto3 = aula.render("678", 0, (0, 0, 0), (255, 255, 255))
    texto4 = aula.render("899", 0, (0, 0, 0), (255, 255, 255))
    texto5 = aula.render("1045", 0, (0, 0, 0), (255, 255, 255))
    texto6 = aula.render("2670", 0, (0, 0, 0), (255, 255, 255))
    texto7 = aula.render("3456", 0, (0, 0, 0), (255, 255, 255))
    texto8 = aula.render("4983", 0, (0, 0, 0), (255, 255, 255))
    texto9 = aula.render("5266", 0, (0, 0, 0), (255, 255, 255))
    texto10 = aula.render("6982", 0, (0, 0, 0), (255, 255, 255))
    texto11 = aula.render("8450", 0, (0, 0, 0), (255, 255, 255))
    texto12 = aula.render("9123", 0, (0, 0, 0), (255, 255, 255))
    texto13 = aula.render("10765", 0, (0, 0, 0), (255, 255, 255))
    texto14 = aula.render("12890", 0, (0, 0, 0), (255, 255, 255))
    texto15 = aula.render("13876", 0, (0, 0, 0), (255, 255, 255))
    texto16 = aula.render("1489", 0, (0, 0, 0), (255, 255, 255))
    texto17 = aula.render("15000", 0, (0, 0, 0), (255, 255, 255))
    textowin = winmensaje.render("AULA LIMPIA", 0, (255, 255, 255), (0, 0, 0))

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

    for limite in piso[0]:
        if jugador_rectangulo.colliderect(limite[1]):
            jugador_rectangulo.x -= jugador_vel_x
            jugador_rectangulo.y -= jugador_vel_y

    for fruta in copy.copy(piso[1]):
        if jugador_rectangulo.collidepoint(fruta[1].centerx, fruta[1].centery):
            piso[1].remove(fruta)

    for puerta in piso[2]:
        if jugador_rectangulo.collidepoint(puerta[1].centerx, puerta[1].centery):
            if piso == piso1:
                piso = piso2
                jugador_rectangulo.x = 100
                jugador_rectangulo.y = 300
            elif piso == piso2:
                piso = piso3
                jugador_rectangulo.x = 100
                jugador_rectangulo.y = 300
            elif piso == piso3:
                piso = piso4
                jugador_rectangulo.x = 100
                jugador_rectangulo.y = 300
            elif piso == piso4:
                piso = piso1
                jugador_rectangulo.x = 100
                jugador_rectangulo.y = 300

    # Dibujos
    ventana.blit(imagen_fondo, [0, 0])
    for elemento in piso:
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
    if piso == piso1:
        ventana.blit(texto1, (120, 0))
        ventana.blit(texto2, (1150, 0))
        ventana.blit(texto3, (120, 480))
        ventana.blit(texto4, (1150, 480))
    elif piso == piso2:
        ventana.blit(texto5, (120, 0))
        ventana.blit(texto6, (1150, 0))
        ventana.blit(texto7, (590, 0))
        ventana.blit(texto8, (120, 480))
        ventana.blit(texto9, (1150, 480))
    elif piso == piso3:
        ventana.blit(texto10, (120, 0))
        ventana.blit(texto11, (1150, 0))
        ventana.blit(texto12, (120, 480))
    elif piso == piso4:
        ventana.blit(texto13, (120, 0))
        ventana.blit(texto14, (1150, 0))
        ventana.blit(texto15, (590, 0))
        ventana.blit(texto16, (120, 480))
        ventana.blit(texto17, (1150, 480))
    # Posiciones de Aulas Limpias
    # Piso1
    if piso == piso1:
        if jugador_rectangulo.x == 100 and jugador_rectangulo.y == 0:
            ventana.blit(textowin, (400, 300))
        if jugador_rectangulo.x == 1150 and jugador_rectangulo.y == 0:
            ventana.blit(textowin, (400, 300))
        if jugador_rectangulo.x == 100 and jugador_rectangulo.y == 480:
            ventana.blit(textowin, (400, 300))
        if jugador_rectangulo.x == 1150 and jugador_rectangulo.y == 480:
            ventana.blit(textowin, (400, 300))
    # Piso2
    if piso == piso2:
        if jugador_rectangulo.x == 100 and jugador_rectangulo.y == 0:
            ventana.blit(textowin, (400, 300))
        if jugador_rectangulo.x == 1150 and jugador_rectangulo.y == 0:
            ventana.blit(textowin, (400, 300))
        if jugador_rectangulo.x == 550 and jugador_rectangulo.y == 0:
            ventana.blit(textowin, (400, 300))
        if jugador_rectangulo.x == 100 and jugador_rectangulo.y == 480:
            ventana.blit(textowin, (400, 300))
        if jugador_rectangulo.x == 1150 and jugador_rectangulo.y == 480:
            ventana.blit(textowin, (400, 300))
    # Piso3
    if piso == piso3:
        if jugador_rectangulo.x == 100 and jugador_rectangulo.y == 0:
            ventana.blit(textowin, (400, 300))
        if jugador_rectangulo.x == 1150 and jugador_rectangulo.y == 0:
            ventana.blit(textowin, (400, 300))
        if jugador_rectangulo.x == 100 and jugador_rectangulo.y == 480:
            ventana.blit(textowin, (400, 300))
    # Piso4
    if piso == piso4:
        if jugador_rectangulo.x == 100 and jugador_rectangulo.y == 0:
            ventana.blit(textowin, (400, 300))
        if jugador_rectangulo.x == 1150 and jugador_rectangulo.y == 0:
            ventana.blit(textowin, (400, 300))
        if jugador_rectangulo.x == 550 and jugador_rectangulo.y == 0:
            ventana.blit(textowin, (400, 300))
        if jugador_rectangulo.x == 100 and jugador_rectangulo.y == 480:
            ventana.blit(textowin, (400, 300))
        if jugador_rectangulo.x == 1150 and jugador_rectangulo.y == 480:
            ventana.blit(textowin, (400, 300))
    # Prueba de Posicion
    if pulsado[pygame.K_q] and piso == piso1:
        piso = piso2
    if pulsado[pygame.K_w] and piso == piso2:
        piso = piso3
    if pulsado[pygame.K_e] and piso == piso3:
        piso = piso4
    if pulsado[pygame.K_r] and piso == piso4:
        piso = piso1
    # Reco de Voz
    if pulsado[pygame.K_SPACE] and piso == piso1:
        rv()
    elif pulsado[pygame.K_SPACE] and piso == piso2:
        rv()
    elif pulsado[pygame.K_SPACE] and piso == piso3:
        rv()
    elif pulsado[pygame.K_SPACE] and piso == piso4:
        rv()
    # Actualizar
    pygame.display.update()


# Salir
pygame.quit()
