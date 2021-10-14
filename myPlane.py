import pygame

#我方飞机
class MyPlane(pygame.sprite.Sprite):
    def __init__(self, bg_size):
        pygame.sprite.Sprite.__init__(self)

        self.image1 = pygame.image.load('image/myPlane1.png').convert_alpha()
        self.image2 = pygame.image.load('image/myPlane2.png').convert_alpha()
        self.destroy_image = pygame.image.load('image/myPlaneDestroy.png').convert_alpha()
        self.rect = self.image1.get_rect()
        self.bg_width, self.bg_height = bg_size[0], bg_size[1]
        self.rect.left, self.rect.top = \
                        (self.bg_width - self.rect.width) // 2, \
                        self.bg_height - self.rect.height - 60 #预留画面下方状态栏位置
        self.speed = 10
        self.is_alive = True#标记战机是否存活
        self.invincible = False #战机无敌状态标记
        self.mask = pygame.mask.from_surface(self.image1) #将图片中的非透明部分标记为mask便于做更好的碰撞检测

    def move(self,num1,num2,num3):
        self.rect.left=(num1*num3)/num2

    def reset(self):
        self.rect.left, self.rect.top = \
                        (self.bg_width - self.rect.width) // 2, \
                        self.bg_height - self.rect.height - 60 #预留画面下方状态栏位置
        self.is_alive = True
        self.invincible = True #仅当战机重生时设置为无敌
        
