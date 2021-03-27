#importing libariers
import pygame
import sys
import random
pygame.mixer.init()
#lets create a music for background
pygame.mixer.music.load('cute.mp3')
pygame.mixer.music.play()
score=0
clock = pygame.time.Clock()
#lets put this all in a function
def run_game():
    def score_increment():
        global score
        score+=1
    global score
    #intilizing the screen
    pygame.init()
    #making screen
    screen_width=400
    screen_height=600
    screen= pygame.display.set_mode((screen_width,screen_height))
    #bg title and icon
    icon=pygame.image.load('bird.png')
    pygame.display.set_icon(icon)
    pygame.display.set_caption('flappy bird by raheel')
    bg=pygame.image.load('bg.png')
    #creating sound
    flap=pygame.mixer.Sound('sfx_wing.wav')
    point=pygame.mixer.Sound('sfx_point.wav')
    hit=pygame.mixer.Sound('sfx_hit.wav')
    #score
    font=pygame.font.SysFont('comicsans',60,True)
    def big():
        screen.blit(bg,(0,0))
    #gameover
    tomato=pygame.font.SysFont('comicsans',60,True)
    def gameover():
        score=0
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        run_game()
            pygame.display.flip()
            screen.fill((0,0,0))
            over=tomato.render('Game over',1,(255,255,255))
            screen.blit(over,(80,250))
    #player
    pxpos=int(0)
    pypos=int(screen_height/2)
    def player(x,y):
        screen.blit(icon,(int(x),int(y)))
    #making velocityfor the pipes
    vel=1
    #Object1
    ob1 = pygame.image.load('ob1.png')
    ob1posx = 400
    e = random.randrange(100,200)
    ob1posy=e-ob1.get_height()+100
    def obj1 (x,y):
        screen.blit(ob1,(x,y))

    #Object2
    ob2 = pygame.image.load('ob2.png')
    ob2posx = 400
    m = random.randrange(150,300)
    ob2posy=ob2.get_height()+m-150

    def obj2 (x,y):
        screen.blit(ob2,(x,y))

    #main loop
    run=True
    while run:
        clock.tick(200)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    flap.play()
                    pypos -= 60       
           
        # update display
        pygame.display.flip()
        big()
        tile=font.render('score: '+str(score),1,(0,0,0))
        screen.blit(tile,(60,60))
        player(pxpos,pypos)
        obj1(ob1posx,ob1posy)
        obj2(ob2posx,ob2posy)
        #this is for checking
    #collision
        pome=icon.get_rect(topleft=(int(pxpos),int(pypos)))
        pol=ob1.get_rect(topleft=(ob1posx,ob1posy))
        pol2=ob2.get_rect(topleft=(ob2posx,ob2posy))
        colliding=pome.colliderect(pol)
        colliding2=pome.colliderect(pol2)
        pypos += 1
        ob1posx -= vel
        ob2posx -= vel
        if colliding or colliding2 or pypos >= 600-64 or pypos < 0:
            score=0
            hit.play()
            gameover()
        if ob1posx <= 0:
            score_increment()
            point.play()
            run_game()

run_game()
