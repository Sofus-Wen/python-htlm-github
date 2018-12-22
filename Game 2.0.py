import pygame
import random
import sys
import time
from PySide2.QtWidgets import QApplication, QPushButton
from pygame.locals import *

pygame.init()


def Klokken():
    import turtle
    from datetime import datetime

    def jump(distanz, winkel=0):
        penup()
        right(winkel)
        forward(distanz)
        left(winkel)
        pendown()

    def hand(laenge, spitze):
        fd(laenge * 1.15)
        rt(90)
        fd(spitze / 2.0)
        lt(120)
        fd(spitze)
        lt(120)
        fd(spitze)
        lt(120)
        fd(spitze / 2.0)

    def make_hand_shape(name, laenge, spitze):
        reset()
        jump(-laenge * 0.15)
        begin_poly()
        hand(laenge, spitze)
        end_poly()
        hand_form = get_poly()
        register_shape(name, hand_form)

    def clockface(radius):
        reset()
        pensize(7)
        for i in range(60):
            jump(radius)
            if i % 5 == 0:
                fd(25)
                jump(-radius - 25)
            else:
                dot(3)
                jump(-radius)
            rt(6)

    def setup():
        global second_hand, minute_hand, hour_hand, writer
        mode("logo")
        make_hand_shape("second_hand", 125, 25)
        make_hand_shape("minute_hand", 130, 25)
        make_hand_shape("hour_hand", 90, 25)
        clockface(160)
        second_hand = turtle.Turtle()
        second_hand.shape("second_hand")
        second_hand.color("gray20", "gray80")
        minute_hand = turtle.Turtle()
        minute_hand.shape("minute_hand")
        minute_hand.color("blue1", "red1")
        hour_hand = turtle.Turtle()
        hour_hand.shape("hour_hand")
        hour_hand.color("blue3", "red3")
        for hand in second_hand, minute_hand, hour_hand:
            hand.resizemode("user")
            hand.shapesize(1, 1, 3)
            hand.speed(0)
        ht()
        writer = turtle.Turtle()
        # writer.mode("logo")
        writer.ht()
        writer.pu()
        writer.bk(85)

    def wochentag(t):
        wochentag = ["Monday", "Tuesday", "Wednesday",
                     "Thursday", "Friday", "Saturday", "Sunday"]
        return wochentag[t.weekday()]

    def datum(z):
        monat = ["Jan.", "Feb.", "Mar.", "Apr.", "May", "June",
                 "July", "Aug.", "Sep.", "Oct.", "Nov.", "Dec."]
        j = z.year
        m = monat[z.month - 1]
        t = z.day
        return "%s %d %d" % (m, t, j)

    def tick():
        t = datetime.today()
        sekunde = t.second + t.microsecond * 0.000001
        minute = t.minute + sekunde / 60.0
        stunde = t.hour + minute / 60.0
        try:
            tracer(False)  # Terminator can occur here
            writer.clear()
            writer.home()
            writer.forward(65)
            writer.write(wochentag(t),
                         align="center", font=("Courier", 14, "bold"))
            writer.back(150)
            writer.write(datum(t),
                         align="center", font=("Courier", 14, "bold"))
            writer.forward(85)
            tracer(True)
            second_hand.setheading(6 * sekunde)  # or here
            minute_hand.setheading(6 * minute)
            hour_hand.setheading(30 * stunde)
            tracer(True)
            ontimer(tick, 100)
        except turtle.Terminator:
            pass  # turtledemo user pressed STOP

    def main():
        tracer(False)
        setup()
        tracer(True)
        tick()
        return "EVENTLOOP"

    if __name__ == "__main__":
        mode("logo")
        msg = main()
        print(msg)
        mainloop()

def Klokken_2():
    Black = 0, 0, 0
    White = 255, 255, 255

    Time = 0
    Second = 0
    Minute = 0
    Hour = 0

    Clock = pygame.time.Clock()
    start_ticks = pygame.time.get_ticks()

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        # Fonts
        Font = pygame.font.SysFont("Trebuchet MS", 25)

        # Hour
        HourFont = Font.render("Hrs." + str(Hour).zfill(2), 1, Black)
        HourFontR = HourFont.get_rect()
        HourFontR.center = (1075, 20)
        # Minute
        MinuteFont = Font.render("Min." + str(Minute).zfill(2), 1, Black)
        MinuteFontR = MinuteFont.get_rect()
        MinuteFontR.center = (1190, 20)
        # Second
        SecondFont = Font.render("Sec." + (str(Second).zfill(2)), 1, Black)
        SecondFontR = SecondFont.get_rect()
        SecondFontR.center = (1317, 20)

        time.sleep(1)
        Second += 1
        screen.blit(SecondFont, SecondFontR)
        screen.blit(MinuteFont, MinuteFontR)
        screen.blit(HourFont, HourFontR)

        if Second == 60:
            Second = 0
            Minute = Minute + 1
        if Minute == 60:
            Minute = 0
            Second = 0
            Hour = Hour + 1

        pygame.display.flip()

        Clock.tick(60)


def Spil_1():
    win = pygame.display.set_mode((500, 480))

    pygame.display.set_caption('First Game')

    walkRight = [pygame.image.load('R1.png'), pygame.image.load('R2.png'), pygame.image.load('R3.png'),
                 pygame.image.load('R4.png'), pygame.image.load('R5.png'), pygame.image.load('R6.png'),
                 pygame.image.load('R7.png'), pygame.image.load('R8.png'), pygame.image.load('R9.png')]
    walkLeft = [pygame.image.load('L1.png'), pygame.image.load('L2.png'), pygame.image.load('L3.png'),
                pygame.image.load('L4.png'), pygame.image.load('L5.png'), pygame.image.load('L6.png'),
                pygame.image.load('L7.png'), pygame.image.load('L8.png'), pygame.image.load('L9.png')]

    bg = pygame.image.load('bg.jpg')
    char = pygame.image.load('standing.png')

    x = 50
    y = 400
    width = 64
    height = 64
    vel = 5
    isJump = False
    jumpCount = 10
    left = False
    right = False
    walkCount = 0

    done = False
    size = W, L = 500, 480
    screen = pygame.display.set_mode(size)

    def redrawGameWindow():
        global walkCount
        win.blit(bg, (0, 0))

        if walkCount + 1 >= 27:
            walkCount = 0

        if left:
            win.blit(walkLeft[walkCount // 3], (x, y))
            walkCount += 1
        elif right:
            win.blit(walkRight[walkCount // 3], (x, y))
            walkCount += 1
        else:
            win.blit(char, (x, y))

        pygame.display.update()

    # mainloop
    run = True
    while run:
        clock.tick(27)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT] and x > vel or keys[pygame.K_a] and x > vel:
            x -= vel
            left = True
            right = False
        elif keys[pygame.K_RIGHT] and x < 500 - width - vel or keys[pygame.K_d] and x < 500 - width - vel:
            x += vel
            right = True
            left = False
        else:
            right = False
            left = False
            walkCount = 0

        if not isJump:
            if keys[pygame.K_SPACE]:
                isJump = True
                right = False
                left = False
                walkCount = 0
        else:
            if jumpCount >= -10:
                neg = 1
                if jumpCount < 0:
                    neg = -1
                y -= (jumpCount ** 2) * 0.5 * neg
                jumpCount -= 1
            else:
                isJump = False
                jumpCount = 10

        if keys[pygame.K_ESCAPE]:
            quit()

        redrawGameWindow()

    pygame.quit()


# It starts here js
pygame.init()

skrn = pygame.display.set_mode((400, 300))
pygame.display.set_caption('Menu')
skrn.fill((255, 255, 255))
menuAtivo = True

start_button = pygame.draw.rect(skrn, (0, 0, 240), (150, 90, 100, 50))
continue_button = pygame.draw.rect(skrn, (0, 244, 0), (150, 160, 100, 50))
quit_button = pygame.draw.rect(skrn, (244, 0, 0), (150, 230, 100, 50))

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        sys_font = pygame.font.SysFont \
            ("None", 60)
        rendered = sys_font.render \
            ('-The Menu-', 0, (0, 0, 0))
        skrn.blit(rendered, (90, 20))
        pygame.display.update()
        while menuAtivo:
            import pygame

            for evento in pygame.event.get():
                print(evento)
                if evento.type == pygame.MOUSEBUTTONDOWN:
                    if pygame.mouse.get_pos()[0] >= 150 and pygame.mouse.get_pos()[1] >= 230:
                        if pygame.mouse.get_pos()[0] <= 250 and pygame.mouse.get_pos()[1] <= 280:
                            pygame.quit()
                    if pygame.mouse.get_pos()[0] >= 150 and pygame.mouse.get_pos()[1] >= 160:
                        if pygame.mouse.get_pos()[0] <= 250 and pygame.mouse.get_pos()[1] <= 210:
                            Klokken()
                    if pygame.mouse.get_pos()[0] >= 150 and pygame.mouse.get_pos()[1] >= 90:
                        if pygame.mouse.get_pos()[0] <= 250 and pygame.mouse.get_pos()[1] <= 140:
                            Spil_1()

                    pygame.display.update()