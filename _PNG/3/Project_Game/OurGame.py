import pygame
from random import randint
pygame.init()
win=pygame.display.set_mode((640,360))
pygame.mixer.music.load('Project_Game\woods.mp3')
pygame.mixer.music.play(-1,0.0)
pygame.display.set_caption("Игра")
walkRight = [pygame.image.load("Project_Game\elf21.png"),pygame.image.load('Project_Game\elf22.png'),pygame.image.load('Project_Game\elf23.png'),pygame.image.load('Project_Game\elf24.png'),pygame.image.load('Project_Game\elf25.png'),pygame.image.load('Project_Game\elf26.png'),pygame.image.load('Project_Game\elf27.png'),pygame.image.load('Project_Game\elf28.png'),pygame.image.load('Project_Game\elf29.png'),pygame.image.load('Project_Game\elf210.png')]
walkLeft=[pygame.image.load('Project_Game\elf11.png'),pygame.image.load('Project_Game\elf12.png'),pygame.image.load('Project_Game\elf13.png'),pygame.image.load('Project_Game\elf14.png'),pygame.image.load('Project_Game\elf15.png'),pygame.image.load('Project_Game\elf16.png'),pygame.image.load('Project_Game\elf17.png'),pygame.image.load('Project_Game\elf18.png'),pygame.image.load('Project_Game\elf19.png'),pygame.image.load('Project_Game\elf110.png')]
stil=pygame.image.load('Project_Game\stay_elf.png')
fon=pygame.image.load('Project_Game\phon.jpg')
portal=pygame.image.load("Project_Game\portal.png")
portal2=pygame.image.load("Project_Game\portal2.png")
portal3=pygame.image.load("Project_Game\portal3.png")
portal4=pygame.image.load("Project_Game\portal4.png")
portal5=pygame.image.load("Project_Game\portal5.png")
portal6=pygame.image.load("Project_Game\portal6.png")
portal7=pygame.image.load("Project_Game\portal7.png")
portal8=pygame.image.load("Project_Game\portal8.png")
portal9=pygame.image.load("Project_Game\portal9.png")
portal10=pygame.image.load("Project_Game\portal10.png")
pl=pygame.image.load("Project_Game\DanTextures.jpg")
clock=pygame.time.Clock()
x=-20
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
f=0
class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, filename):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(filename).convert_alpha()
        self.rect = self.image.get_rect(center=(340, 320))
    def update(self):
        if self.rect.x >= -10:
            self.rect.x -= 2
            f=self.rect.x
        else:
            self.rect.x =340
            f=self.rect.x
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
def func():
    x=y=0
    for row in level:
        for col in row:
            if col=="-":
                win.blit(pl, (x,y))
            x+=30
        y+=30
        x=0
level=["                     ","                     ","    --------------           ","                   ","                   ","                   ","                     ","            -------- ","                  ","     -------","                     ","                     "]
def draw():
    win.blit(fon,(0,0))
    func()
    win.blit(portal10,(420,305))
    win.blit(portal9,(515,5))
    win.blit(portal8,(115,5))
    win.blit(portal7,(575,155))
    win.blit(portal6,(355,155))
    win.blit(portal5,(335,215))
    win.blit(portal4,(140,215))
    win.blit(portal3,(350,305))
    win.blit(portal,(-10,305))
    win.blit(portal2,(620,305))
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
    if keys[pygame.K_LEFT] and x > -41:
        x-=speed
        left=True
        right=False
    elif keys[pygame.K_RIGHT] and x < 601:
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
    if x==-25 and y==280:
        x=575
    if x==590 and y==280:
        x=-10
    if x==345 and y==280:
        x=135
        y=210
    if x==130 and y==210:
        x=345
        y=280
    if x==325 and y==210:
        x=345
        y=145
    if x==340 and y==145:
        x=320
        y=210
    if x==570 and y==145:
        x=110
        y=0
    if x==105 and y==0:
        x=565
        y=145
    if x==505 and y==0:
        x=410
        y=280
    if x==405 and y==280:
        x=500
        y=0
    draw()
pygame.quit()
