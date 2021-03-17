import pygame
from pygame.locals import *
import sys
#from  class_bird import Bird

class Variavel():
    SCREEN_WIDTH  = 400
    SCREEN_HEIGHT = 600
    JANELA        = None
    run           = True
    BACKGROUND    = pygame.image.load('img/background.png') 
    BACKGROUND    = pygame.transform.scale(BACKGROUND, (SCREEN_WIDTH,SCREEN_HEIGHT))
    BIRD_GROUP    = None
    bird          = None

class Bird(pygame.sprite.Sprite):
    def __init__(self):
        #pygame.sprite.Sprite.__init__(self)
        super().__init__()
        self.image = pygame.image.load('img/passaro.png')
        self.image = pygame.transform.scale( self.image,[32,32])
        
        self.rect    = self.image.get_rect()
        self.rect[0] = Variavel.SCREEN_WIDTH /2
        self.rect[1] = Variavel.SCREEN_HEIGHT /2
        
    def update(self):
        pass
 

def setup():
    pygame.init()
    Variavel.JANELA = pygame.display.set_mode((Variavel.SCREEN_WIDTH,Variavel.SCREEN_HEIGHT))
    pygame.display.set_caption('Flappy Bird')
    
    Variavel.BIRD_GROUP = pygame.sprite.Group()
    Variavel.bird       = Bird()
    Variavel.BIRD_GROUP.add(Variavel.bird)
    
    
    
def game_loop():
    while Variavel.run:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                quit()
   
        Variavel.JANELA.blit(Variavel.BACKGROUND,(0,0))
        Variavel.BIRD_GROUP.draw(Variavel.JANELA)
        pygame.display.update()

  

if __name__ == '__main__':
    setup()
    game_loop()
