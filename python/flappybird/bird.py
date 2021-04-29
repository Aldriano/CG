'''
 # Aldriano
 # Adaptação/Compilação de diversos estudos
 # Exemplo de código para fins didáticos
'''
import pygame
from pygame.locals import *
import sys
#from  class_bird import Bird

import time
import random

class Variavel():
    SCREEN_WIDTH  = 400
    SCREEN_HEIGHT = 600
    JANELA        = None
    run           = True
    BACKGROUND    = pygame.image.load('img/background.png') 
    BACKGROUND    = pygame.transform.scale(BACKGROUND, (SCREEN_WIDTH,SCREEN_HEIGHT))
    BIRD_GROUP    = None
    bird          = None
    GROUND_GROUP  = None
    ground        = None
    GRAVITY       = 1
    BLUE          = (0,0,255)
    tela          = 0
   
    ADDPIPE       = None
    PIPE_WIDTH    =  80
    PIPE_HEIGHT   = SCREEN_HEIGHT
    PIPE_GROUP    = None
    pipe          = None
    pipe_inverted = None
    PIPE_GAP      = 220

    GROUND_HEIGHT = 100

    TOP           = 0
    BOTTOM        = 0
    SOUNDS        = {}
    score         = 0
    
class Bird(pygame.sprite.Sprite):
    def __init__(self):
        #pygame.sprite.Sprite.__init__(self)
        super().__init__()
        self.image = pygame.image.load('img/passaro.png')  #.convert()
        self.image = pygame.transform.scale( self.image,[32,32])

        self.speed = 10
        
        self.rect    = self.image.get_rect()
        self.rect[0] = Variavel.SCREEN_WIDTH /2
        self.rect[1] = Variavel.SCREEN_HEIGHT /2

        
    def update(self):
        self.speed += Variavel.GRAVITY
        self.rect[1] += self.speed   #coordenada Y - linha

        if self.rect[1] > Variavel.SCREEN_HEIGHT:
            self.rect[1] =  Variavel.SCREEN_HEIGHT /2
            
    def pos(self,y):
        self.rect[1] = y
            
class Ground(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('img/base.png')
        self.image = pygame.transform.scale( self.image,[Variavel.SCREEN_WIDTH * 2,self.image.get_height()])
        
        self.rect    = self.image.get_rect()
        self.rect[0] = 0   #coluna
        self.rect[1] = Variavel.SCREEN_HEIGHT - self.image.get_height()  #linha
        
    def update(self):
        # Movimento do Ground, diminuir -1 na coluna
        self.rect[0] -= 1
        if self.rect[0] <= -Variavel.SCREEN_WIDTH:
           self.rect[0] = 0
 
    '''def update(self):
        # Movimento do Ground, diminuir -1 na coluna
        self.rect[0] -= 1
        if self.rect[0]  *-1 > Variavel.SCREEN_WIDTH:
        
           self.rect[0] = 0'''
    
class Cano(pygame.sprite.Sprite):
    def __init__(self, inverted,ysize):
        #pygame.sprite.Sprite.__init__(self)
        super().__init__()
        
        self.image = pygame.image.load('img/pipe-green.png')
        self.image = pygame.transform.scale(self.image,(Variavel.PIPE_WIDTH, Variavel.PIPE_HEIGHT) )
        
        self.rect    = self.image.get_rect()
        self.rect[0] = Variavel.SCREEN_WIDTH * 2

        #inverter os canos
        if inverted:
            flip_pipe    = pygame.transform.flip(self.image,False,True) # 1parametro vira horizonta, 2 vertical=true 
            self.image   = pygame.transform.scale( flip_pipe,[self.image.get_width(),ysize])
            #print("Class cano:  rect image inverted = ",self.image.get_rect(), " tamanho TOP= ",self.rect[3])
            self.rect[1] =  0  #linha 0 TOP
            Variavel.TOP = self.rect[3]
            #print("ysize ysize=",ysize," self.image.get_width()= ",self.image.get_width())
            
        else:
            self.image   = pygame.transform.scale( self.image,[self.image.get_width(),ysize])
            self.rect[1] = Variavel.SCREEN_HEIGHT - ysize - Variavel.GROUND_HEIGHT
            #print("Class cano:  rect image normal = ",self.image.get_rect()," line= ",self.rect[1],)

        
    def update(self):
        self.rect[0] -=  5 #10

        
       
def randon_pipes():
     size          = random.randint(100,300)
     #print("Tamanho cano Bottom = ",size," Tamanho cano TOP = ",Variavel.SCREEN_HEIGHT - size - Variavel.PIPE_GAP)
     Variavel.pipe          = Cano(False,size)
     Variavel.pipe_inverted = Cano(True, Variavel.SCREEN_HEIGHT - size - Variavel.PIPE_GAP)
     return Variavel.pipe,Variavel.pipe_inverted 

         
def setup():
    pygame.init()
    Variavel.JANELA = pygame.display.set_mode((Variavel.SCREEN_WIDTH,Variavel.SCREEN_HEIGHT))
    pygame.display.set_caption('Flappy Bird')
    
    #Pássaro
    Variavel.BIRD_GROUP = pygame.sprite.Group()
    Variavel.bird       = Bird() # instanciando o classe
    Variavel.BIRD_GROUP.add(Variavel.bird)
    
    ##Ground
    Variavel.GROUND_GROUP = pygame.sprite.Group()
    Variavel.ground       = Ground()
    Variavel.GROUND_GROUP.add(Variavel.ground )

    Variavel.ADDPIPE =  pygame.USEREVENT + 1
    pygame.time.set_timer( Variavel.ADDPIPE,1500) # 250 milesegundos

    Variavel.PIPE_GROUP = pygame.sprite.Group()

    Variavel.SOUNDS['die']    = pygame.mixer.Sound('sound/die.ogg')
    Variavel.SOUNDS['hit']    = pygame.mixer.Sound('sound/hit.ogg')
    Variavel.SOUNDS['point']  = pygame.mixer.Sound('sound/point.ogg')
    Variavel.SOUNDS['swoosh'] = pygame.mixer.Sound('sound/swoosh.ogg')
    Variavel.SOUNDS['wing']   = pygame.mixer.Sound('sound/wing.ogg')


def message(text):
    font = pygame.font.Font('freesansbold.ttf',55)
    imgFont = font.render(text, True, Variavel.BLUE)
    #posição do texto
    imgRect = imgFont.get_rect()
    imgRect.center = ((Variavel.SCREEN_WIDTH/2),(Variavel.SCREEN_HEIGHT/2))

    Variavel.JANELA.blit(imgFont,imgRect)
    
    Variavel.bird.rect[0]  = Variavel.SCREEN_WIDTH/2
    Variavel.bird.rect[1]  = Variavel.SCREEN_HEIGHT/2
    
    Variavel.bird.speed = -10
    
    pygame.display.update()

    waiting = True
    while waiting:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                quit()
            if evento.type == KEYDOWN:
                if evento.key == K_SPACE:
                    waiting = False

def score(score):
    font = pygame.font.Font('freesansbold.ttf',20)
    imgFont = font.render("Score: "+str(score), True, Variavel.BLUE)
    #posição do texto
    imgRect = imgFont.get_rect()
    imgRect.center = ((50),(15))

    Variavel.JANELA.blit(imgFont,imgRect)
    
    pygame.display.update()
    
def game_loop():
    while Variavel.run:
        
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                quit()

            if evento.type == KEYDOWN:
                if evento.key == K_SPACE:
                    Variavel.bird.speed = -10
                    #print(pygame.font.get_fonts())
                    Variavel.SOUNDS['wing'].play()

            if evento.type == Variavel.ADDPIPE:
                pipe = randon_pipes()
                Variavel.PIPE_GROUP.add(pipe[0])
                Variavel.PIPE_GROUP.add(pipe[1])

        

        for cano in Variavel.PIPE_GROUP:
            #print("Group=",cano.rect[0] )
            '''if cano.rect[0] <= Variavel.bird.rect[0] - Variavel.bird.rect[2]*3:  
                print("passou o pássaro ","cano.rect[0]= ",cano.rect[0],"  Variavel.bird.rect[0]= ",Variavel.bird.rect[0]," largura=", Variavel.bird.rect[2]-5,"
                cano.rect", cano.rect)
                Variavel.PIPE_GROUP.remove(cano)
            '''
            # deixando o pássaro passar automáticamente entre os canos
            # cano.rect[0]-50 ->Pega a distância do cano uns 50 pixles e compara com a posção (coluna) do pássaro
            if cano.rect[0]-50 <= Variavel.bird.rect[0]:
                #Variavel.bird[1] = cano[0].rect[3
                #print("- ", cano.rect[3])
                c = cano.image.get_rect() 
                #print(c[2],c[3]) #mostrar largura e altura do cano
                Variavel.bird.pos(c[3]+50) #posiciona o pássaro 50 pixels do tamanho do cano superior
                
            '''if cano.rect[0] <= Variavel.bird.rect[0] - Variavel.bird.rect[2]*3:
                Variavel.PIPE_GROUP.remove(cano) '''
            
            
            if cano.rect[0] + cano.rect[2] < 0:  # Pego o coluna inicial do cano + a largura do cano, isto é quando o cano passar da coluna zero
                Variavel.PIPE_GROUP.remove(cano)  #remove o cano
                #print("Excluiu Cano")
                Variavel.score +=(1/2) #Soma 0.5 pois existe 2 canos de cada vez
       
           

        if Variavel.tela == 0:
            pass
           #print("tela inicial")
           # criar função tela inicial (), semelhante a da menssage
           
           
        Variavel.JANELA.blit(Variavel.BACKGROUND,(0,0))
        
        # Desenha o pássaro
        Variavel.BIRD_GROUP.draw(Variavel.JANELA)

        #Desenha borda no pássaro
        #pygame.draw.rect(Variavel.JANELA,(255,0,0),Variavel.bird.rect,1)
        
        # Desenha a base/terra
        Variavel.GROUND_GROUP.draw(Variavel.JANELA)
        
         # Desenha o cano
        Variavel.PIPE_GROUP.draw(Variavel.JANELA)
        
        # Atualização
        Variavel.BIRD_GROUP.update()
        Variavel.GROUND_GROUP.update()
        Variavel.PIPE_GROUP.update()

        #Colisão com o terra/solo
        if pygame.sprite.groupcollide(Variavel.BIRD_GROUP,Variavel.GROUND_GROUP,False, False, pygame.sprite.collide_mask):
           #print("houve a colisão")
           Variavel.SOUNDS['die'].play()
           message("Game Over")
           Variavel.score = 0

        # Colisão com o cano   
        if pygame.sprite.groupcollide(Variavel.BIRD_GROUP,Variavel.PIPE_GROUP,False, False, pygame.sprite.collide_mask):
           Variavel.SOUNDS['hit'].play()

           
        score(Variavel.score)
        
        pygame.display.update()
        clock.tick(30)



        
clock = pygame.time.Clock()
if __name__ == '__main__':
    setup()
    game_loop()


