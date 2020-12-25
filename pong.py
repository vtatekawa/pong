# Jogo criado em Python inspirado no classico Pong desenvolvido pela Atari em 1972

# By Vitor Tatekawa

import turtle
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
sound_path = os.path.join(dir_path, 'bounce.wav')

# Criando a tela onde o jogo será projetado
wn = turtle.Screen()
wn.title('Pong by Vitor Tatekawa')
wn.bgcolor('black')
wn.setup(width=800, height=600)
wn.tracer(0)


# Criando os objetos que aparecerão na tela

# Controle A
controle_a = turtle.Turtle()
controle_a.speed(0)
controle_a.shape('square')
controle_a.color('white')
controle_a.shapesize(stretch_wid=5, stretch_len=1)
controle_a.penup()
controle_a.goto(-350, 0)

# Controle B
controle_b = turtle.Turtle()
controle_b.speed(0)
controle_b.shape('square')
controle_b.color('white')
controle_b.shapesize(stretch_wid=5, stretch_len=1)
controle_b.penup()
controle_b.goto(350, 0)

# Bolinha
bolinha = turtle.Turtle()
bolinha.speed(0)
bolinha.shape('square')
bolinha.color('white')
bolinha.penup()
bolinha.goto(0, 0)
bolinha.dx = 0.4
bolinha.dy = -0.4

# Placar
pen = turtle.Turtle()
pen.speed(0)
pen.color('white')
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write('Jogador 1: 0  Jogador 2: 0', align='center', font=('Courier', 24, 'normal'))

placar_a = 0
placar_b = 0


# Criando as funções de movimentação dos controles A

def controle_a_up():
    y = controle_a.ycor()
    y += 20
    controle_a.sety(y)

def controle_a_down():
    y = controle_a.ycor()
    y -= 20
    controle_a.sety(y)

# Criando as funções de movimentação dos controles B

def controle_b_up():
    y = controle_b.ycor()
    y += 20
    controle_b.sety(y)

def controle_b_down():
    y = controle_b.ycor()
    y -= 20
    controle_b.sety(y)

# Funções de teclado do controle A e B
wn.listen()
wn.onkeypress(controle_a_up, 'w')
wn.onkeypress(controle_a_down, 's')
wn.onkeypress(controle_b_up, 'Up')
wn.onkeypress(controle_b_down, 'Down')

#Loop do jogo principal

while True:
    wn.update()

    # Movimento bolinha
    bolinha.setx(bolinha.xcor() + bolinha.dx)
    bolinha.sety(bolinha.ycor() + bolinha.dy)

    # Bordas da tela

    # borda superior
    if bolinha.ycor() > 290:
        bolinha.sety(290)
        bolinha.dy *= -1
        os.system('afplay "{}"&'.format(sound_path))
    
    # Borda inferior
    if bolinha.ycor() < -290:
        bolinha.sety(-290)
        bolinha.dy *= -1
        os.system('afplay "{}"&'.format(sound_path))

    # borda direita
    if bolinha.xcor() > 390:
        bolinha.goto(0, 0)
        bolinha.dx *= -1
        placar_a += 1
        pen.clear()
        pen.write('Jogador 1: {}  Jogador 2: {}'.format(placar_a, placar_b), align='center', font=('Courier', 24, 'normal'))
    
    # Borda esquerda
    if bolinha.xcor() < -390:
        bolinha.goto(0, 0)
        bolinha.dx *= -1
        placar_b += 1
        pen.clear()
        pen.write('Jogador 1: {}  Jogador 2: {}'.format(placar_a, placar_b), align='center', font=('Courier', 24, 'normal'))

    # Contato bolinha e controles
    if (bolinha.xcor() > 340 and bolinha.xcor() < 350) and (bolinha.ycor() < controle_b.ycor() + 40 and bolinha.ycor() > controle_b.ycor() - 40):
        bolinha.setx(340)
        bolinha.dx *= -1
        os.system('afplay "{}"&'.format(sound_path))
    
    if (bolinha.xcor() < -340 and bolinha.xcor() > -350) and (bolinha.ycor() < controle_a.ycor() + 40 and bolinha.ycor() > controle_a.ycor() - 40):
        bolinha.setx(-340)
        bolinha.dx *= -1
        os.system('afplay "{}"&'.format(sound_path))

    # Inteligência Artificial
    # Caso queira deixar os controles manuais, só comentar os códigos abaixo

    #######################################
    #Controle B
    if controle_b.ycor() < bolinha.ycor() and abs(controle_b.ycor() - bolinha.ycor()) > 10:
        controle_b_up()

    elif controle_b.ycor() > bolinha.ycor() and abs(controle_b.ycor() - bolinha.ycor()) > 10:
        controle_b_down()
    
    #Controle A
    #if controle_a.ycor() < bolinha.ycor() and abs(controle_a.ycor() - bolinha.ycor()) > 10:
        #controle_a_up()

    #elif controle_a.ycor() > bolinha.ycor() and abs(controle_a.ycor() - bolinha.ycor()) > 10:
        #controle_a_down()
    ########################################
