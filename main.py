from pygame import *
import sys

class GameSprite(sprite.Sprite):
    def __init__(self, path, x, y, width, height):
        super().__init__()
        self.image = transform.scale(image.load(path), (width, height))
        self.rect = self.image.get_rect(center=(x, y))
    def reset(self):
        screen.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def __init__(self, path, x, y, width, height):
        super().__init__(path, x, y, width, height)
        self.speed = 0
        self.height = height
    def update(self):
        self.rect.y -= self.speed
    def check(self):
        if self.rect.y <= 0:
            self.set_speed(0)
            self.rect.y += 5
        if self.rect.y >= screen_height - self.height:
            self.set_speed(0)
            self.rect.y -= 5

    def set_speed(self, new_speed):
        self.speed = new_speed


class Ball(GameSprite):
    def __init__(self, path, x, y, speed_x, speed_y):
        super().__init__(path, x, y)
        self.speed_x = speed_x
        self.speed_y = speed_y


class Bot(GameSprite):
    def __init__(self, path, x, y, speed):
        super().__init__(path, x, y)
        self.speed = speed
FPS = 120
screen_width = 1280
screen_height = 650
background = transform.scale(image.load('background.png'), (screen_width, screen_height))
player = Player('platform.png', 60, 300, 25, 150)
screen = display.set_mode((screen_width, screen_height))
clock = time.Clock()
display.set_caption('Ping-pong')

while True:
    screen.blit(background, (0, 0))
    for one_event in event.get():
        if one_event.type == QUIT:
            quit()
            sys.exit()
        if one_event.type == KEYDOWN:
            if one_event.key == K_UP:
                player.set_speed(5)
            if one_event.key == K_DOWN:
                player.set_speed(-5)
        if one_event.type == KEYUP:
            if one_event.key == K_UP or one_event.key == K_DOWN:
                player.set_speed(0)
    player.reset()
    player.update()
    player.check()
    display.update()
    clock.tick(FPS)
""" изображение платформы
    звук удара мяча о платформу?
    звук попадания
    звук начала игры
    """