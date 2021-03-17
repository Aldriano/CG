#Documentação: https://www.pygame.org/docs/ref/display.html
import sys,pygame #importa o pacote com todos os módulos PyGame disponíveis. 
from pygame import gfxdraw
from pygame.locals import *  #submódulo locals, contêm as variáveis de eventos (mouse, teclado, joystick)

# Verificando erros de inicializacao
check_errors = pygame.init() #inicializa cada um desses módulos.
if check_errors[1] > 0:
    print("(!) Ops, {0} o Pygame iniciou com algum problema..." . format(check_errors[1]))
    sys.exit(-1)
else:
    print("(+) O Pygame foi inicializado com sucesso!")

#"display.set_mod()" cria um novo objeto Surface que representa o gráficos mostrados atualmente
#Qualquer desenho que você fizer a este Surface se tornará visível no monitor.
#Criar a tela onde o jogo vai acontecer. Para isso a gente vai criar uma variável que chamamos de “tela”
# e vamos dar para ela um tamanho de 50 x 50:

screen = pygame.display.set_mode((50,50)) #cria uma janela gráfica
#pintar a cor do fundo da tela
screen.fill((255,255,255)) #background white

screen.set_at((10,10),(255,0,0)) #urface.set_at () para plotar um único pixel em sua superfície.
screen.set_at((20,20),(0,255,0))
screen.set_at((20,10),(0,0,255))
pygame.display.flip() #atualiza toda área da superfície

pygame.display.set_caption('Primitivas') #define um título na janela

while 1: #oop inifinito, jogo pronto para rodar
  for event in pygame.event.get(): #captura qualquer evento
    # se ocorrer o evento de fechar, executa o método sys.quit()
    #irá garantir que o programa feche sem mais complicações
    if event.type == pygame.QUIT: sys.exit()  
    if event.type == pygame.MOUSEBUTTONDOWN: 
       x,y = pygame.mouse.get_pos()
       print(x,y)
       screen.set_at((x,y),(255,0,0))
    pygame.display.update()
