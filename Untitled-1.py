from pygame import *
window = display.set_mode((700, 500))
display.set_caption("Шутер")
back = (200, 200, 200)
game = True
finish = False

while game:
    for e in event.get():
        if e.type == QUIT:
           game = False
    if not finish:
        window.fill(back)
        display.update()
    time.delay(50)