import pygame
from time import sleep
from random import randint

pygame.init()

screen = pygame.display.set_mode((600,600))
pygame.display.set_caption('ran san moi')
clock = pygame.time.Clock()

GREY= (150,150,150)
WHITE= (255,255,255)
BLACK = (0, 0, 0)
BLUE= (0,0,255)
GREEN = (0,255,0)
RED = (255,0,0)
DOIMAU = GREEN
running = True


font_small = pygame.font.SysFont('sans', 20)
font_big = pygame.font.SysFont('sans', 50)
score = 0


#toa do moi ran
#duoi-dau
snakes = [[0,6]]
huong = ("right")
ran = True
apple = [randint(0,19),randint(0,19)]
pausing = False



 

while running:
    clock.tick(60)
    screen.fill(BLACK)

    tall_x = snakes[0][0]
    tall_y = snakes[0][1]
    
    #ve ran va tao
    pygame.draw.rect(screen,RED,(apple[0]*30,apple[1]*30,30,30))
    
    for snake in snakes :    
        pygame.draw.rect(screen,DOIMAU,(snake[0]*30,snake[1]*30,30,30))
    #an tao
    if snakes[-1][0] == apple[0] and snakes[-1][1] == apple[1] :
        snakes.insert(0,[tall_x,tall_y])
        apple = [randint(0,19),randint(0,19)]
        score += 1
    
    #an tao   
    

    
        
    if pausing == False :
        if huong == "up" :

            snakes.append([snakes[-1][0], (snakes[-1][1]-1) % 20])
            snakes.pop(0)
        if huong == "down" :
                
            snakes.append([snakes[-1][0], (snakes[-1][1]+1) % 20])
            snakes.pop(0)
        
        if huong == "left":
            snakes.append([(snakes[-1][0]-1) % 20, snakes[-1][1]])
            snakes.pop(0)
        if huong == "right" :
            snakes.append([(snakes[-1][0]+1) % 20, snakes[-1][1]])
            snakes.pop(0)

        for i in range(len(snakes)-1):
            if snakes[-1][0] == snakes[i][0] and snakes[-1][1] == snakes[i][1] :
                pausing = True
                DOIMAU = BLUE
        #thua
    if pausing == True:
        game_over_txt = font_big.render("game over,score:"+str(score),True,WHITE)
        press_space_txt = font_big.render("press space to continue",True,WHITE)
        screen.blit(game_over_txt,(50,200))
        screen.blit(press_space_txt,(50,300))

    game_score = font_small.render("score:"+str(score),True,WHITE)
    screen.blit(game_score,(0,0))
    #toc do
    sleep(0.05)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and huong != "down" :
                huong = "up"
            if event.key == pygame.K_DOWN and huong != "up":
                huong = "down"
            if event.key == pygame.K_LEFT and huong != "right":
                huong = "left"
            if event.key == pygame.K_RIGHT and huong != "left":
                huong = "right"
            
            if event.key == pygame.K_SPACE and pausing == True:
                pausing = False
                snakes = [[0,6]]
                apple = [randint(0,19),randint(0,19)]
                DOIMAU = GREEN
                score = 0

                




            

    pygame.display.flip()

        
                    
   
   
pygame.quit()