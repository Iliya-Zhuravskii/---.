from pygame import *
window = display.set_mode((700, 500))
display.set_caption("Шутер")
back = (200, 200, 200)


class GameSprite(sprite.Sprite):
   def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
       super().__init__()
       self.image = transform.scale(image.load(player_image), (size_x, size_y))
       self.speed = player_speed
       self.rect = self.image.get_rect()
       self.rect.x = player_x
       self.rect.y = player_y
   def reset(self):
       window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
   def update_r(self):
       keys = key.get_pressed()
       if keys[K_UP] and self.rect.y > 5:
           self.rect.y -= self.speed
       if keys[K_DOWN] and self.rect.y < 700 - 80:
           self.rect.y += self.speed
   def update_l(self):
       keys = key.get_pressed()
       if keys[K_w] and self.rect.y > 5:
           self.rect.y -= self.speed
       if keys[K_s] and self.rect.y < 700 - 80:
           self.rect.y += self.speed

racket1 = Player('2ракетка.png', 30, 200, 150, 180, 4)
racket2 = Player('ракетка1.png', 600, 200, 150, 180, 4)
ball = Player('мячик.png', 280, 280,  50, 30, 4)

game = True
finish = False
while game:

    for e in event.get():
        if e.type == QUIT:
           game = False
    if not finish:
        window.fill(back)
        racket1.update_l()
        racket2.update_r()

        racket1.reset()
        racket2.reset()
        ball.reset()

        display.update()
    time.delay(50)
