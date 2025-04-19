from pygame import *
import sys

window = display.set_mode((1680, 950)) 
display.set_caption('Plat')
background = transform.scale(image.load('background.png'), (2000, 1840))

clock = time.Clock()
FPS = 60

class GameSprite(sprite.Sprite):
    def __init__(self, img, x, y, speed, widht, height, direction='right'):
        super().__init__()
        self.img = transform.scale(image.load(img), (widht, height))
        self.rect = self.img.get_rect()
        self.speed = speed
        self.rect.x = x
        self.rect.y = y
        self.direction = direction
        self.isleftdir = None
        self.isrightder = None




    def reset(self):
        window.blit(self.img, self.rect)

class Platform(sprite.Sprite):
    def __init__(self, colors, width,height, x, y):
        super().__init__()
        self.colors = colors
        self.width = width
        self.height= height
        self.wall = Surface((self.width, self.height))
        self.wall.fill(self.colors)
        self.rect = self.wall.get_rect()
        self.rect.x = x
        self.rect.y = y

    def draw_plat(self):
        window.blit(self.wall, self.rect)



class Player(GameSprite):
    def __init__(self, img, x, y, speed, widht, height, direction='left'):
        super().__init__(img, x, y, speed, widht, height)
        self.velocity_y = 0
        self.jump = False
        self.jump_power = -15
        self.on_ground = True
        self.direction = direction

    def change_direction(self):
        self.img = transform.flip(self.img, True, False)


    def update(self):
        self.velocity_y += 0.5
        self.rect.y += self.velocity_y
        
        pressed = key.get_pressed()
        if pressed[K_a] and self.rect.x > 5: 
            self.rect.x -= self.speed
            if self.direction == 'right':
                self.direction = 'left'
                self.change_direction()
        if pressed[K_d] and self.rect.x < 1640:
            self.rect.x += self.speed
            if self.direction == 'left':
                self.direction = 'right'
                self.change_direction()                
        if pressed[K_SPACE]:
            self.jumping()
         
    def jumping(self):        
        if self.on_ground:
            self.velocity_y = -12
            self.jump = True
            self.on_ground = False

    def gravity(self, platform):
        if sprite.collide_rect(self, platform) and self.velocity_y > 0:
            self.rect.bottom = platform.rect.top
            self.velocity_y = 0
            self.on_ground = True           
            self.jump = False


#platform = Platform((5, 255, 5), 150, 25, 350, 450)
#Как поставить картинку для платформы?


#all_sprites = sprite.Group()
#platforms = sprite.Group()
#
# platform1 = Platform((5, 255, 5),150, 25, 450, 350)




#platforms.add(platform)
#all_sprites.add(platform)
platforms = [
    Platform((5, 255, 5),150, 25, 150, 250),
    Platform((5, 255, 5),150, 25, 250, 270),
    Platform((5, 255, 5),150, 25, 350, 290),
    Platform((5, 255, 5),150, 25, 450, 310)
]


player = Player('avatar.png', 425, 296, 6, 50, 75)


game = True
finish = False

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
        

    if not finish:

        window.blit(background,(0,0))
        player.update()
        player.reset()

        for pl in platforms:
            pl.draw_plat()
            player.gravity(pl)
        # player.gravity(platform1)
        # platform1.draw_plat()
        #




    display.update()
    clock.tick(FPS)

