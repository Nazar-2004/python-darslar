# turtle dan yuklab olgin Turtle classi, Screen classi. Turtle - chizmalarni chizish uchun, Screen - oynani hosil qilish uchun.

from turtle import Turtle, Screen, bgcolor       # turtle kutubxonasini dasturimizda yuklab oldik.
from random import randint


window = Screen()    # Alohida oyna ochamiz,ya'ni o'zgaruvchi nomini window deb nomlaymiz.
window.title('My snake game') # oynaning nomi (sarlavhasi)
bgcolor('forestgreen')

turtle1 = Turtle()
turtle1.shape('turtle')
turtle1.color('yellow')
turtle1.penup() # ko'chish chizig'ini yo'q qilish uchun ushbu penup() funksiyasidan foydalanamiz.
turtle1.goto(-250, 100)  # boshqa joyga ko'chishi uchun
turtle1.pendown() # keyinchalik harakatga keltirish uchun


turtle2 = Turtle()
turtle2.shape('turtle')
turtle2.color('blue')
turtle2.penup() # ko'chish chizig'ini yo'q qilish uchun ushbu penup() funksiyasidan foydalanamiz.
turtle2.goto(-250, 50)  # boshqa joyga ko'chishi uchun
turtle2.pendown() # keyinchalik harakatga keltirish uchun


turtle3 = Turtle()
turtle3.shape('turtle')
turtle3.color('red')
turtle3.penup() # ko'chish chizig'ini yo'q qilish uchun ushbu penup() funksiyasidan foydalanamiz.
turtle3.goto(-250, 0)  # boshqa joyga ko'chishi uchun
turtle3.pendown() # keyinchalik harakatga keltirish uchun

finish = Turtle()
finish.up()
finish.speed(0)
finish.hideturtle()
finish.color('black')
finish.pensize(5)
finish.goto(200,150)
finish.down()
finish.goto(200,-50)

# forward() - bu harakatga keltirish uchun
while True:
    tezlik_1 = randint(1,5)
    tezlik_2 = randint(1,5)
    tezlik_3 = randint(1,5)
    turtle1.forward(tezlik_1)
    turtle2.forward(tezlik_2)
    turtle3.forward(tezlik_3)
    # xcor() - funksiyasi bu x ning kordinatasi qayerga ekanligini  qaytaradi.ya'ni chegaraga (200) kelganda dastur to'xtaydi.
    if turtle1.xcor() >= 200:
        turtle1.up()  # ya'ni g'olib pastga tushadi.
        turtle1.goto(0,-120)
        break
    elif turtle2.xcor() >= 200:
        turtle2.up()
        turtle2.goto(0,-120)
        break
    elif turtle3.xcor() >= 200:
        turtle3.up()
        turtle3.goto(0, -120)
        break

window.mainloop() # oynani ekranga ushlab turish uchun
