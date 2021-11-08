#abrimos librerias 
import pygame;

Blanco = (255, 255, 255)
Negro = (0, 0, 0)

class Oro(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("img/oro.png").convert()
        self.image.set_colorkey(Negro)
        self.rect = self.image.get_rect()
        
pygame.init() 

screen = pygame.display.set_mode([683, 509])
clock = pygame.time.Clock()

done = False 

oro_list = pygame.sprite.Group()
all_sprite_list = pygame.sprite.Group()

for i in range (100):
    oro = Oro()
    oro.rect.x = 560
    oro.rect.y = 50
oro_list.add(oro)
all_sprite_list.add(oro)
  
fondo = pygame.image.load("img/mapa.png").convert()
player = pygame.image.load("img/crab-1.png").convert()
player.set_colorkey([0, 0, 0])

cofre = pygame.image.load("img/cofre.png").convert()
cofre.set_colorkey([0, 0, 0])



oro_hit_list = pygame.sprite.spritecollide.func = (player, oro_list, True)

# coordenada del player
coord_x = 10
coord_y = 430
#velocidad
x_speed = 0
y_speed = 0
#coordenadas de moneda de oro
coord_oro_x = 530
coord_oro_y = -20


while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        #eventos del teclado
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_speed = -3
            if event.key == pygame.K_RIGHT:
                x_speed = 3
            if event.key == pygame.K_UP:
                y_speed = -3
            if event.key == pygame.K_DOWN:
                y_speed = 3
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                x_speed = 0
            if event.key == pygame.K_RIGHT:
                x_speed = 0
            if event.key == pygame.K_UP:
                y_speed = 0
            if event.key == pygame.K_DOWN:
                y_speed = 0
            
    screen.blit(fondo, [0, 0])
    
    coord_x += x_speed
    
    coord_y += y_speed
    
    all_sprite_list.draw(screen)
    
    screen.blit(player, [coord_x, coord_y])
    
    screen.blit(cofre, [coord_oro_x, coord_oro_y])
    
    pygame.display.flip()
    clock.tick(60)
    
  
    
pygame.quit() 

