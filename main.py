import turtle
import pygame
import winsound
from pygame import mixer
import random

# Oyun ekranı ve arkaplanı oluşturuluyor.
wn = turtle.Screen()
wn.title("Masa hokeyi")
wn.setup(width=800, height=600)
wn.bgpic("bgg.png")
wn.tracer(0)
pygame.mixer.init()

# Fon müziği
mixer.music.load('ravenwood.wav')
mixer.music.set_volume(0.04)
mixer.music.play()

score_a=0
score_b=0

# Solda bulunan blok 
block_a = turtle.Turtle()
block_a.speed(10)
block_a.shape("square")
block_a.color("#a2ff23")
block_a.shapesize(stretch_wid=5, stretch_len=1)  # blokların boyutları
block_a.penup()
block_a.goto(-350, 0)

# Sağda bulunan blok
block_b = turtle.Turtle()
block_b.speed(10)
block_b.shape("square")
block_b.color("#a2ff23")
block_b.shapesize(stretch_wid=5, stretch_len=1)
block_b.penup()
block_b.goto(350, 0)

# Top oluşturulup başlangıçta rastgele hız değeri belirleniyor.
ball = turtle.Turtle()
ball.shape("circle")
ball.color("#a2ff23")
ball.penup()
ball.goto(0, 0)
ball.dx = random.randint(15,20)/100
ball.dy = random.randint(1,2)/10

# Ilk top'a 4 defa vurulduğunda oyuna dahil olan 2.top
ball2 = turtle.Turtle()
ball2.shape("circle")
ball2.color("#a2ff23")
ball2.penup()
ball2.goto(0, 0)
ball2.dx = random.randint(15,20)/100
ball2.dy = random.randint(1,2)/10
vurus = 0

# Skor tablosu çizdiriliyor.
pen=turtle.Turtle()
pen.speed(0)
pen.color("#a2ff23")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write(" OyuncuA: 0   OyuncuB: 0 ", align="center",font=("Courier", 24, "normal"))


# Her 2 bloğun hareketleri ve sınırları tanımlanıyor.
def block_a_up():
    y = block_a.ycor()
    if y > 230:
        y = 230
    y += 30
    block_a.sety(y)

def block_a_down():
    y = block_a.ycor()
    if y < -230:
        y = -230
    y -= 30
    block_a.sety(y)

def block_b_up():
    y = block_b.ycor()
    if y > 230:
        y = 230
    y += 30
    block_b.sety(y)

def block_b_down():
    y = block_b.ycor()
    if y < -230:
        y = -230
    y -= 30
    block_b.sety(y)

def block_a_left():
    x=block_a.xcor()
    if x>-380 and x<0:
        x -=30
        block_a.setx(x)

def block_a_right():
    x = block_a.xcor()
    if x >-400 and x<-30:
        x +=30
        block_a.setx(x)

def block_b_left():
    x=block_b.xcor()
    if x>30 and x<420:
        x -=30
        block_b.setx(x)

def block_b_right():
    x = block_b.xcor()
    if x >0 and x<370:
        x +=30
        block_b.setx(x)

# Gol gerçekleştiğinde skor tablosuna yazdırma işlemi
def block_b_goal():
    pen.clear()
    pen.write(" OyuncuA: {}   OyuncuB: Goal ".format(score_a), align="center", font=("Courier", 24, "normal"))
    pen.clear()

def block_a_goal():
    pen.clear()
    pen.write(" OyuncuA: Goal   OyuncuB: {}  ".format(score_b), align="center", font=("Courier", 24, "normal"))
    pen.clear()

# Tuş Dinleme işlemi
wn.listen()
wn.onkeypress(block_a_up, "w")
wn.onkeypress(block_a_down, "s")
wn.onkeypress(block_a_left, "a")
wn.onkeypress(block_a_right, "d")
wn.onkeypress(block_b_up, "Up")
wn.onkeypress(block_b_down, "Down")
wn.onkeypress(block_b_left, "Left")
wn.onkeypress(block_b_right, "Right")

# Main
while True:
    wn.update()
    # Topun hareketi
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Kenarlıklar'a çarpıldığında oluşan ses ve top'un eğimi
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        winsound.PlaySound("arr.wav", winsound.SND_ASYNC)

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        winsound.PlaySound("arr.wav", winsound.SND_ASYNC)

    # Gol'den sonra yeni round'a başlamak için atamalar
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball2.goto(0,0)
        block_b.goto(350, 0)
        block_a.goto(-350, 0)
        ball.dx *= -1
        score_a += 1
        turtle.ontimer(block_a_goal(),2000)
        vurus = 0
        pen.clear()
        pen.write(" OyuncuA: {}   OyuncuB: {} ".format(score_a,score_b), align="center", font=("Courier", 24, "normal"))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball2.goto(0, 0)
        block_b.goto(350, 0)
        block_a.goto(-350, 0)
        ball.dx *= -1
        score_b += 1
        turtle.ontimer(block_b_goal(), 2000)
        vurus = 0
        pen.clear()
        pen.write(" OyuncuA: {}   OyuncuB: {} ".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

    # Top bloğa vurduğu anda yapılacak olanlar
    x = block_b.xcor()-10
    y = block_b.ycor()
    if (ball.xcor() > x and ball.xcor()< x+20) and ( ball.ycor() < y + 50 and ball.ycor() > y - 50):
        ball.setx(x)
        ball.dx *= - 1
        winsound.PlaySound("arr.wav",winsound.SND_ASYNC)
        vurus += 1

    a= block_a.xcor()+10
    b= block_a.ycor()
    if (ball.xcor() < a  and ball.xcor()>a-20) and (ball.ycor() < b + 50 and ball.ycor() > b - 50):
        ball.setx(a)
        ball.dx *= -1
        winsound.PlaySound("arr.wav",winsound.SND_ASYNC)
        vurus += 1

    # 2.top gizlendi
    ball2.hideturtle()

    # Ilk topa 5.defa vurulduğu an 2.top oyuna dahil oluyor.
    if vurus > 4:
        ball2.showturtle()
        ball2.setx(ball2.xcor() + ball2.dx)
        ball2.sety(ball2.ycor() + ball2.dy)

        if ball2.ycor() > 290:
                ball2.sety(290)
                ball2.dy *= -1
                winsound.PlaySound("arr.wav", winsound.SND_ASYNC)

        if ball2.ycor() < -290:
                ball2.sety(-290)
                ball2.dy *= -1
                winsound.PlaySound("arr.wav", winsound.SND_ASYNC)

        if ball2.xcor() > 390:
                ball2.goto(0, 0)
                ball.goto(0,0)
                block_b.goto(350, 0)
                block_a.goto(-350, 0)
                vurus = 0
                turtle.ontimer(block_a_goal(), 2000)
                ball2.dx *= -1
                score_a += 1
                pen.clear()
                pen.write(" OyuncuA: {}   OyuncuB: {} ".format(score_a, score_b), align="center",
                          font=("Courier", 24, "normal"))

        if ball2.xcor() < -390:
                ball2.goto(0, 0)
                ball.goto(0, 0)
                block_b.goto(350, 0)
                block_a.goto(-350, 0)
                vurus=0
                ball2.dx *= -1
                turtle.ontimer(block_b_goal(), 2000)
                score_b += 1
                pen.clear()
                pen.write(" OyuncuA: {}   OyuncuB: {} ".format(score_a, score_b), align="center",
                          font=("Courier", 24, "normal"))

        x = block_b.xcor() - 10
        y = block_b.ycor()
        if (ball2.xcor() > x and ball2.xcor() < x + 20) and (ball2.ycor() < y + 50 and ball2.ycor() > y - 50):
            ball2.setx(x)
            ball2.dx *= -1
            winsound.PlaySound("arr.wav", winsound.SND_ASYNC)
            vurus += 1

        a = block_a.xcor() + 10
        b = block_a.ycor()
        if (ball2.xcor() < a and ball2.xcor() > a - 20) and (ball2.ycor() < b + 50 and ball2.ycor() > b - 50):
            ball2.setx(a)
            ball2.dx *= -1
            winsound.PlaySound("arr.wav", winsound.SND_ASYNC)
            vurus += 1

