from pygame import *


FPS = 60
screen_width = 1280
screen_height = 650
screen = display.set_mode((screen_width, screen_height))
display.set_caption('Ping-pong')

while True:
    for one_event in event.get():
        if one_event.type == QUIT:
            quit()

    display.update()
    time.delay(FPS)