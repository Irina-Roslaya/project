import pygame
from random import randint
pygame.init()
win=pygame.display.set_mode((640,360))
pygame.mixer.init()
pygame.mixer.music.load('Project_Game\woods.mp3')
pygame.mixer.music.play(-1)
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
menbg=pygame.image.load("Project_Game\men.jpg")
enemy1 = pygame.image.load('Project_Game\enemy_run_1.png')
enemy2 = pygame.image.load('Project_Game\enemy2.png')
enemy3 = pygame.image.load('Project_Game\enemy4.png')
enemy4 = pygame.image.load('Project_Game\enemy3.png')
enemy5 = pygame.image.load("Project_Game\enemy5.png")
death1=pygame.image.load("Project_Game\death1.jpg")
death2=pygame.image.load("Project_Game\death3.jpg")
death3=pygame.image.load("Project_Game\death5.jpg")
death4=pygame.image.load("Project_Game\death4.jpg")
death5=pygame.image.load("Project_Game\death2.jpg")
tt=pygame.image.load('Project_Game\may.png')
fog=pygame.image.load('Project_Game\og.jpg')
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
HP2=True
hp2=180
HP3=True
hp3=120
HP4=True
hp4=180
HP5=True
hp5=200
f=0
class snaryad():
    def __init__(self,x,y,radius,color ,facing):
        self.x = x
        self.y = y
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
        win.blit(enemy1,(290,295))
        win.blit(tt,(250,220))
        win.blit(tt,(440,160))
        win.blit(tt,(500,295))
        win.blit(tt,(450,5))
        if 280<= x<=310 and y== 280:
            win.blit(death1,(0,0))
        if (240<= x<=270 and y== 210) or (430<= x<=460 and y== 145) or (490<= x<=520 and y== 280) or (440<= x<=470 and y==0):
            win.blit(fog,(0,0))
        pygame.display.update()
    elif HP2:
        win.blit(enemy2,(250,215))
        win.blit(tt,(440,160))
        win.blit(tt,(500,295))
        win.blit(tt,(450,5))
        if 240<= x<=290 and y== 210:
            win.blit(death2,(0,0))
        if (430<= x<=460 and y== 145) or (490<= x<=520 and y== 280) or (440<= x<=470 and y==0):
            win.blit(fog,(0,0))
        pygame.display.update()
    elif HP3:
        win.blit(enemy3,(440,155))
        win.blit(tt,(500,295))
        win.blit(tt,(450,5))
        if 430<= x<=470 and y== 145:
            win.blit(death3,(0,0))
        if (490<= x<=520 and y== 280) or (440<= x<=470 and y==0):
            win.blit(fog,(0,0))
        pygame.display.update()
    elif HP4:
        win.blit(enemy4,(500,295))
        win.blit(tt,(450,5))
        if 490<= x<=520 and y== 280:
            win.blit(death4,(0,0))
        if (440<= x<=470 and y==0):
            win.blit(fog,(0,0))
        pygame.display.update()
    elif HP5:
        win.blit(enemy5,(450,5))
        if 430<= x<=460 and y==0:
            win.blit(death5,(0,0))
        pygame.display.update()
    if HP==False and HP2==False and HP3==False and HP4==False and HP5==False :
        win.blit(menbg,(0,0))
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
             if bullet.x==290 and bullet.y ==320:
                 bullets.pop(bullets.index(bullet))
                 hp=hp-20
                 pygame.mixer.Channel(0).play(pygame.mixer.Sound('Project_Game\death.wav'))
         elif HP2:
             if bullet.x==300 and bullet.y == 250 :
                 bullets.pop(bullets.index(bullet))
                 hp2=hp2-20
                 pygame.mixer.Channel(0).play(pygame.mixer.Sound('Project_Game\death.wav'))
         elif HP3:
            if bullet.x==440 and bullet.y == 185 :
                bullets.pop(bullets.index(bullet))
                hp3=hp3-20
                pygame.mixer.Channel(0).play(pygame.mixer.Sound('Project_Game\death.wav'))
         elif HP4:
            if bullet.x==500 and bullet.y == 320:
                bullets.pop(bullets.index(bullet))
                hp4=hp4-20
                pygame.mixer.Channel(0).play(pygame.mixer.Sound('Project_Game\death.wav'))
         elif HP5:
            if bullet.x==450 and bullet.y == 40:
                bullets.pop(bullets.index(bullet))
                hp5=hp5-20
                pygame.mixer.Channel(0).play(pygame.mixer.Sound('Project_Game\death.wav'))
    if hp<1:
         HP=False
    if hp2<1:
         HP2=False
    if hp3<1:
         HP3=False
    if hp4<1:
         HP4=False
    if hp5<1:
         HP5=False
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
