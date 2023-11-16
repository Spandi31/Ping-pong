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
    
    def __init__(self, path, x, y, speed_x, speed_y, width, height):
        super().__init__(path, x, y, width, height)
        self.speed_x = speed_x
        self.speed_y = speed_y
    
    def update(self):
        self.rect.y += self.speed_y
        self.rect.x += self.speed_x
        self.collisions(bot)
    def collisions(self, bot):
        if self.rect.top <= 0 or self.rect.bottom >= screen_height:
            knock.play()
            self.speed_y *= -1
        if self.rect.left <= 0 or self.rect.right >= screen_width:
            knock.play()
            self.speed_x *= -1 
        if sprite.spritecollide(self, platforms, False):

            knock_platform.play()
            self.speed_x *= -1
        
class Bot(GameSprite):
    def __init__(self, path, x, y, speed, width, height):
        super().__init__(path, x, y, width, height)
        self.speed = speed
    def update(self, ball):
        if ball.rect.top > self.rect.bottom:
            self.rect.y += self.speed
        if ball.rect.bottom < self.rect.top:
            self.rect.y -= self.speed
mixer.init()
knock = mixer.Sound("knock.ogg")
knock_platform = mixer.Sound("knockplatform2.ogg")
FPS = 120
screen_width = 1280
screen_height = 650
platforms = sprite.Group()
background = transform.scale(image.load('background.png'), (screen_width, screen_height))
player = Player('platform.png', 60, 300, 25, 150)
platforms.add(player)
bot = Bot("platform.png", 1200, 300, 8, 25, 150)
platforms.add(bot)
ball = Ball("ball.png", 640, 325, 3, 3, 100, 100)
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
    ball.reset()
    ball.update()
    platforms.draw(screen)
    bot.update(ball)
    player.update()
    player.check()
    display.update()
    clock.tick(FPS)