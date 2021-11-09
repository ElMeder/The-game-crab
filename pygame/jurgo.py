class Enemigos(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("img/tortuga.png").convert()
        self.image.set_colorkey(Negro)
        self.rect = self.image.get_rect()
        self.rect.x = (300 - self.rect.width)
        self.rect.y = (50 - self.rect.height)
        self.velocidad_x = 5
        
        if self.rect.left < 0:
            self.rect.left = 0
            
        if self.rect.right > 683:
            self.rect.right = 683