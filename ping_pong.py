
from pygame import *
from time import time as timer
#Parent class for other sprites
class GameSprite(sprite.Sprite):
#Class constructor
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
      #Call the class constructor (Sprite):
        sprite.Sprite.__init__(self)
      #Each sprite must store an image property - an image
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
      #Each sprite must store the rect property - the rectangle in which it is inscribed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
#Method that draws the hero on the window
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
#Main player class
class Player(GameSprite):
#Method for controlling a sprite with keyboard arrows
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 100:
            self.rect.y += self.speed
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - 100:
            self.rect.y += self.speed

back = (255, 255, 255)
win_width = 600
win_height = 500
programIcon = image.load('icon.png')
display.set_icon(programIcon)
display.set_caption('Ping-Pong')
window = display.set_mode((win_width, win_height))

window.fill(back)

game = True
finish = False
clock = time.Clock()
FPS = 60

firsty = 200
firstx = 0
secondx = 520

racket1 = Player('racket.png', firstx, firsty, 100, 100, 5)
racket2 = Player('racket1.png', secondx, firsty, 100, 100, 5)
ball = GameSprite('tenis_ball.png', 200, 200, 50, 50, 150)

font.init()
font = font.SysFont("Arial", 35)
lost1 = font.render('PLAYER 1 LOSE', True, (180, 0, 0))
lost2 = font.render('PLAYER 2 LOSE', True, (180, 0, 0))

mixer.init()
ping_sound = mixer.Sound('ping.ogg')
lose_sound = mixer.Sound('lose.ogg')

speed_x = 3
speed_y = 3


while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:
        window.fill(back)
        racket1.update_l()
        racket2.update_r()
        ball.rect.x += speed_x
        ball.rect.y += speed_y
        if sprite.collide_rect(racket1, ball) or sprite.collide_rect(racket2, ball):
            speed_x *= -1
            ping_sound.play()
        if ball.rect.y > win_height - 50:
            speed_y *= -1
        if ball.rect.y <= win_height - (win_height - 20):
            speed_y *= -1
        if ball.rect.x < -50:
            lose_sound.play()
            finish = True
            speed_x = 3
            window.blit(lost1, (200, 200))
        if ball.rect.x > win_width:
            lose_sound.play()
            finish = True
            speed_x = -3
            window.blit(lost2, (200,200))
        racket1.reset()
        racket2.reset()
        ball.reset()
        display.update()
    else:
        racket1.rect.x = firstx
        racket1.rect.y = firsty
        racket2.rect.x = secondx
        racket2.rect.y = firsty
        ball.rect.x = firsty
        ball.rect.y = firsty
        speed_y = 3
        finish = False
        time.delay(3000)
    time.delay(15)









