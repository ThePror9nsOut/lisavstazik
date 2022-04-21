import pygame,random;import mod
pygame.init()
cap = [800, 600];win = pygame.display.set_mode(cap)
pygame.display.set_caption("taziik")
run = True
sprites = [pygame.transform.scale(pygame.image.load("snus.png"), (60,60)), pygame.transform.scale(pygame.image.load("tazik.png"), (60,60))]
def init():
    global player
    global snuses
    global sprites
    global score
    global enemies
    player = [random.randint(0,cap[0]), random.randint(0,cap[1]), 60]
    player.append(pygame.transform.scale(pygame.image.load("lisa.png"), (player[2], player[2])))
    enemies = []
    snuses = []
    score = 0
    for g in range(5):
        enemies.append([random.randint(0,cap[0]),random.randint(0,cap[1]),sprites[1], "l", 5,5])

init()

def clearndraw():
    global win
    global snuses
    global score
    win.fill((0,0,0))
    pygame.time.delay(10)

    keys = pygame.key.get_pressed()

    for index,i in enumerate(snuses):
        win.blit(sprites[0], (int(i[0]), int(i[1])))
        if(mod.colideNS([player[0],player[1], 60,60], [i[0],i[1],60,60])):
            score+=1
            snuses.pop(index)
    for i in enemies:
        win.blit(sprites[1], (int(i[0]), int(i[1])))
        if(i[3] == "e"):
            if (i[0] < player[0]):
                i[0] += 13-player[2]/10
            if (i[0] > player[0]):
                i[0] -= 13-player[2]/10
            if (i[1] < player[1]):
                i[1] += 13-player[2]/10
            if (i[1] > player[1]):
                i[1] -= 13-player[2]/10
        if(i[3] == "l"):
            i[0] += i[4]
            i[1] += i[5]
            if(i[0]<0 or i[0]>cap[0]):
                i[4] = -i[4]
                i[4] += random.randint(-1,1)
                i[5] += random.randint(-1, 1)
            if(i[1]<0 or i[1]>cap[1]):
                i[5] = -i[5]
                i[4] += random.randint(-1,1)
                i[5] += random.randint(-1, 1)

        if (mod.colideNS([player[0], player[1], 60, 60], [i[0], i[1], 30, 30])):
            init()

    mod.text(win, pygame.font.SysFont("arial black", 20), str(score), (50,50), (255,255,255))

    if(random.choice([False, False, False, True,False,False,False,False,False,False,False,False,False])):
        snuses.append([random.randint(0,cap[0]), random.randint(0,cap[1])])

    if(keys[pygame.K_w] and player[1] > 0):
        player[1] -= 15-player[2]/10
    elif(keys[pygame.K_s] and player[1] < cap[1] - player[2]):
        player[1] += 15-player[2]/10
    if(keys[pygame.K_a] and player[0] > 0):
        player[0] -= 15-player[2]/10
    elif(keys[pygame.K_d] and player[0] < cap[0] - player[2]):
        player[0] += 15-player[2]/10

    win.blit(player[3], (int(player[0]),int(player[1])))

    pygame.display.update()

while run:
    clearndraw()
    pygame.time.delay(5)

    for event in pygame.event.get():
        if (event.type == pygame.QUIT):
            run = False
pygame.quit()
