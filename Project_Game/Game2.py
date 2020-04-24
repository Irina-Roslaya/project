import pygame
from random import randint
pygame.init()
win=pygame.display.set_mode((640,360))
pygame.display.set_caption("Игра")
walkRight = [pygame.image.load("Project_Game\elf21.png"),pygame.image.load('Project_Game\elf22.png'),pygame.image.load('Project_Game\elf23.png'),pygame.image.load('Project_Game\elf24.png'),pygame.image.load('Project_Game\elf25.png'),pygame.image.load('Project_Game\elf26.png'),pygame.image.load('Project_Game\elf27.png'),pygame.image.load('Project_Game\elf28.png'),pygame.image.load('Project_Game\elf29.png'),pygame.image.load('Project_Game\elf210.png')]
walkLeft=[pygame.image.load('Project_Game\elf11.png'),pygame.image.load('Project_Game\elf12.png'),pygame.image.load('Project_Game\elf13.png'),pygame.image.load('Project_Game\elf14.png'),pygame.image.load('Project_Game\elf15.png'),pygame.image.load('Project_Game\elf16.png'),pygame.image.load('Project_Game\elf17.png'),pygame.image.load('Project_Game\elf18.png'),pygame.image.load('Project_Game\elf19.png'),pygame.image.load('Project_Game\elf110.png')]
stil=pygame.image.load('Project_Game\stay_elf.png')
fon=pygame.image.load('Project_Game\phon.jpg')
clock=pygame.time.Clock()
x=10
y=280
h=80
w=80
speed=5
isJump=True
Jump= 5
left=False
right=False
anim=0
HP=True
hp=120
class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, filename):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(filename).convert_alpha()
        self.rect = self.image.get_rect(center=(640, 320))
    def update(self):
        if self.rect.x >= 0:
            self.rect.x -= 2
        else:
            self.rect.x = 640
enemy1 = Enemy(randint(1, 350), 'Project_Game\enemy_run_1.png')
class snaryad():
    def __init__(self,x,y,radius,color ,facing):
        self.x = x
        self.y=y
        self.radius=radius
        self.color=color
        self.facing=facing
        self.vel=10*facing
    def draw(self,win):
        pygame.draw.circle(win,self.color,(self.x,self.y),self.radius)
def draw():
    win.blit(fon,(0,0))
    global anim
    if anim + 1 >= 30:
        anim=0
    if left:
        win.blit(walkLeft[anim//3],(x,y))
        anim+=1
    elif right:
        win.blit(walkRight[anim//3],(x,y))
        anim+=1
    else:
        win.blit(stil,(x,y))
    for bullet in bullets:
        bullet.draw(win,)
    if HP:
        win.blit(enemy1.image, enemy1.rect)
        pygame.display.update()
        pygame.time.delay(20)
        enemy1.update()
    pygame.display.update()

run=True
bullets=[]
while run:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run=False
    for bullet in bullets:
        if bullet.x<640 and bullet.x>0:
            bullet.x=bullet.x+bullet.vel
        else:
            bullets.pop(bullets.index(bullet))
    keys=pygame.key.get_pressed()
    if keys[pygame.K_z]:
        if len(bullets)<5:
            bullets.append(snaryad(round(x+w//2),round(y+h//2),5,(100,149,237),-1))

    if keys[pygame.K_x]:
        if len(bullets)<5:
            bullets.append(snaryad(round(x+w//2),round(y+h//2),5,(100,149,237),1))
    if keys[pygame.K_LEFT] and x > 5:
        x-=speed
        left=True
        right=False
    elif keys[pygame.K_RIGHT] and x < 640-w-5:
        x+=speed
        left=False
        right=True
    else:
        left=False
        right=False
        anim=0
    if not(isJump):
        if keys[pygame.K_SPACE]:
            isJump = True
    else:
        if Jump>=-5:
            if Jump < 0:
                y+=(Jump**2)
            else:
                y-=(Jump**2)
            Jump -=1
        else:
            isJump=False
            Jump=5
    for bullet in bullets:
         if HP:
             if bullet.x==500:
                 bullets.pop(bullets.index(bullet))
                 hp=hp-20
    if hp<1:
         HP=False

    draw()
pygame.quit()
