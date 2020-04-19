import pygame
pygame.init()
win=pygame.display.set_mode((500,500))
pygame.display.set_caption("Игра")
walkRight=[pygame.image.load('Project_Game\walk_1.png'),pygame.image.load('Project_Game\walk_2.png'),pygame.image.load('Project_Game\walk_3.png'),pygame.image.load('Project_Game\walk_4.png'),pygame.image.load('Project_Game\walk_5.png'),pygame.image.load('Project_Game\walk_6.png')]
walkLeft=[pygame.image.load('Project_Game\walk_left_1.png'),pygame.image.load('Project_Game\walk_left_2.png'),pygame.image.load('Project_Game\walk_left_3.png'),pygame.image.load('Project_Game\walk_left_4.png'),pygame.image.load('Project_Game\walk_left_5.png'),pygame.image.load('Project_Game\walk_left_6.png')]
stil=pygame.image.load('Project_Game\stand_up_5.png')
clock=pygame.time.Clock()
x=50
y=425
h=50
w=48
speed=5
isJump=True
Jump=5
left=False
right=False
anim=0
def draw():
    global anim
    win.fill((0,0,0))
    if anim + 1>=30:
        anim=0
    if left:
        win.blit(walkLeft[anim // 5],(x,y))
        anim+=1
    elif right:
        win.blit(walkRight[anim // 5],(x,y))
        anim+=1
    else:
        win.blit(stil,(x,y))
    pygame.display.update()
run=True
while run:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run=False
    keys=pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x > 5:
        x-=speed
        left=True
        right=False
    elif keys[pygame.K_RIGHT] and x < 500-w-5:
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
                y+=(Jump**2)/4
            else:
                y-=(Jump**2)/4
            Jump -=1
        else:
            isJump=False
            Jump=5
    draw()
pygame.quit()
