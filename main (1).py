import pygame
import sys
import random
import time

from pygame.locals import *
#importing images
bg=pygame.image.load("bg1 (1).png")
menu4=pygame.image.load("bg (1).png")
poke=pygame.image.load("poke1p (1).png")
menu1=pygame.image.load("menu1 (1).png")
menu=pygame.image.load("menu (1).png")
menu2=pygame.image.load("menu2 (1).png")
menu3=pygame.image.load("menu3 (1).png")
destroyer=pygame.image.load("s1 (1).png")
crusier=pygame.image.load("s2 (1).png")
death_star=pygame.image.load("s4 (1).png")
millenium_falcon=pygame.image.load("s3 (1).png")
menu3 = pygame.transform.scale(menu3,(1219, 700))
xpn1=pygame.image.load("explosions1 (1).png")
xpn2=pygame.image.load("explosions2 (1).png")
xpn3=pygame.image.load("explosions3 (1).png")
xpn4=pygame.image.load("explosions4 (1).png")
xpn5=pygame.image.load("explosions5 (1).png")
xpn6=pygame.image.load("explosions6 (1).png")
xpn7=pygame.image.load("explosions7 (1).png")
xpn8=pygame.image.load("explosions8 (1).png")
xpn9=pygame.image.load("explosions9 (1).png")
xpn10=pygame.image.load("explosions10 (1).png")
xpn11=pygame.image.load("explosions11 (1).png")
xpn12=pygame.image.load("explosions12 (1).png")
xpn13=pygame.image.load("explosions13 (1).png")
xpn14=pygame.image.load("explosions14 (1).png")
xpn15=pygame.image.load("explosions15 (1).png")
xpn16=pygame.image.load("explosions16 (1).png")
pygame.init()
#play first song
pygame.mixer.music.load('themesong (1).wav')
pygame.mixer.music.play(-1)       

#colors
BLACK = [0, 0, 0]
WHITE = [255, 255, 255]
RED=[204,0,0]
GREEN=[0,255,0]
DGREEN=[0,140,0]
BLUE=[0,0,255]
LBLUE=[0,191,255]
INDIGO=[75,0,130]
YELLOW=[255,255,0]
GOLD=[255,215,0]
ORANGE=[255,99,71]
GREY=[176,196,222]
SIZE = [1200, 700]
screen = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()
PI=3.14

#intro video
#video=pygame.movie.Movie ("introo (1).mpg")
#screen=pygame.display.set_mode((1200,700))
#video.set_display(screen, (0, 0, 1200, 700))
#video.play()
#pygame.display.flip()

#length=video.get_busy()
#while length:
#    length=video.get_busy()
#    font = pygame.font.SysFont('Impact', 20, False, False)
##    text=font.render("Press enter to skip", True, YELLOW)
##    screen.blit(text, [10,10])
##    pygame.display.flip()
##    clock.tick(1000)
##    for event in pygame.event.get():
##        if event.type == pygame.QUIT: 
##                length=False
##                pygame.quit()
##                sys.exit()
##        if pygame.key.get_pressed()[pygame.K_KP_ENTER]:
##            video.stop()
##            length=False
##      

def box(x,y,action):
    mouse=pygame.mouse.get_pos()
    click=pygame.mouse.get_pressed()
    if x<mouse[0]<x+350 and y<mouse[1]<y+175:
        pygame.draw.rect(screen,RED,[x,y,350,175],1)
        if click[0]==1:
            if action=='ins':
                inst()
            elif action=='play':
                main()
            elif action=='quits':
                pygame.quit()
                sys.exit()
       
def inst():
    screen.blit(menu,(-300,0))
    font = pygame.font.SysFont('Impact', 30, False, False)
    text = font.render("Hold the button to read.",True,WHITE)
    screen.blit(text, [500,300])
    text = font.render("Move the ship with the arrow keys.",True,WHITE)
    screen.blit(text, [500,350])
    text=font.render("Dodge Mini Death Stars coming from all directions.",True,WHITE)
    screen.blit(text, [500,400])
    text=font.render("Collect resources (gold coin) to boost your score.",True,WHITE)
    screen.blit(text, [500,450])
    pygame.draw.ellipse(screen,GOLD,(1100,470,7,7),0)
    text=font.render("Coins are small and a little hard to find.",True,WHITE)
    screen.blit(text, [500,500])
    text=font.render("Press 'p' to pause the game at anytime.",True,WHITE)
    screen.blit(text, [500,550])
    
def choice():
    CHOOSE=True
    while CHOOSE:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                pygame.quit()
                sys.exit()
        screen.blit(menu1,(-500,-200))
        font = pygame.font.SysFont('Impact', 50, False, False)
        text = font.render("Choose your difficulty",True,WHITE)
        screen.blit(text, [350, 350])
        font = pygame.font.SysFont('Impact', 30, False, False)
        text = font.render("Press 'e' for Easy. Press 'm' for Medium 'h' for Hard and 'i' for Insane",True,WHITE)
        screen.blit(text, [200, 450])
        
        if pygame.key.get_pressed()[pygame.K_e]:
            CHOOSE=False
            return 1
        if pygame.key.get_pressed()[pygame.K_m]:
            CHOOSE=False
            return 2
        if pygame.key.get_pressed()[pygame.K_h]:
            CHOOSE=False
            return 3
        if pygame.key.get_pressed()[pygame.K_i]:
            CHOOSE=False
            return 4
                   
        pygame.display.flip()
        clock.tick(20)
        
def Type():    
    TYPE=True
    while TYPE:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                TYPE=False
                pygame.quit()
                sys.exit()
                
        screen.blit(menu2,(-80,0))
        font = pygame.font.SysFont('Impact', 50, False, False)
        text = font.render("Choose your ship",True,WHITE)
        screen.blit(text, [400, 200])
        font = pygame.font.SysFont('Impact', 30, False, False)
        text = font.render("Press 'g' for destroyer. Press 'c' for crusier. 'd' for death star and 'f' for millenium falcon",True,WHITE)
        screen.blit(text, [50, 300])
        screen.blit(crusier,(200,400))
        screen.blit(destroyer,(450,400))
        screen.blit(death_star,(700,400))
        screen.blit(millenium_falcon,(950,400))
        
        if pygame.key.get_pressed()[pygame.K_g]:
            TYPE=False
            return destroyer
        if pygame.key.get_pressed()[pygame.K_c]:
            TYPE=False
            return crusier
        if pygame.key.get_pressed()[pygame.K_d]:
            TYPE=False
            return death_star
        if pygame.key.get_pressed()[pygame.K_f]:
            TYPE=False
            return millenium_falcon
                   
        pygame.display.flip()
        clock.tick(20)
        
def main():    
    pygame.display.set_caption("LOST IN SPACE")
    
    class ship():
        def __init__(self):
            self.x=0
            self.y=0
            self.type=0
        def draw(self,screen):
                screen.blit(self.type,(self.x-6,self.y-5))
                
    #makes bonus coin
    #hard to find it then get it
    def coin(screen,redraw,x,y):
        if redraw==True:
            x=random.randrange(5, 1190)
            y=random.randrange(5, 690)
            pygame.draw.ellipse(screen,GOLD,(x,y,10,10),0)
            redraw=False
        else:
            pygame.draw.ellipse(screen,GOLD,(x,y,10,10),0)
        return x, y, redraw
    
    def coin_collision(x,y,coinx,coiny,multiplier):
        bonus=0
        redraw=False
        if (x)<coinx+3<(x+11)and(y+2)<coiny+3<(y+25):
            bonus=random.randrange(100, 500)
            bonus=bonus**(multiplier/2)
            bonus=int(bonus)
            redraw=True
        return bonus, redraw
      
    score=0
    bullet_list  =[]
    bullet_lists =[]
    bullets_list =[]
    bullets_lists=[]
    def detect_collision(x,y,):
        death=False
        
        for i,v in enumerate(bullet_list):
            if v[0]>(x-5) and v[0]<(x+11) and v[1]>(y+2) and v[1]<(y+25):
                death=True
                
        for i,v in enumerate(bullet_lists):
            if v[0]>(x-5) and v[0]<(x+11) and v[1]>(y+2) and v[1]<(y+25):                
                death=True
            
        for i,v in enumerate(bullets_list):
            if v[0]>(x-5) and v[0]<(x+11) and v[1]>(y+2) and v[1]<(y+25):
                death=True
            
        for i,v in enumerate(bullets_lists):
            if v[0]>(x-5) and v[0]<(x+11) and v[1]>(y+2) and v[1]<(y+25):
                death=True
                
        return death
    
    def bullet_creation(bullet_list):
        for i in range(100):
            x = random.randrange(0, 1200)
            y = random.randrange(0, 600)
            bullet_list.append([x, y])
            
    def bullet_move_vertical(bullet_list,speed):
        for i,v in enumerate(bullet_list):           
            screen.blit(poke,v)

            v[1] += speed
            if v[1] > 700 :
                v[1] = 0
                x = random.randrange(0, 1200)
                v[0] = x
            elif v[1]<0 :
                v[1] = 700
                x = random.randrange(0, 1200)
                v[0] = x
                
    def bullet_move_horizontal(bullet_list,speed):
        for i,v in enumerate(bullet_list):           
            screen.blit(poke,v)
            v[0] += speed
            if v[0] > 1200:
                v[0] = 0
                y = random.randrange(0, 700)
                v[1] = y
            elif v[0] < 0:
                v[0] = 1200
                y = random.randrange(0, 700)
                v[1] = y
    def pause():
        ymove=700
        sped=1.1
        paused=True
        while paused:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pause=False
                    pygame.quit()
                    sys.exit()
            screen.blit(menu3,(0,0))
            
            font = pygame.font.SysFont('Impact', 50, False, False)
            text = font.render("GAME IS PAUSED",True,WHITE)
            screen.blit(text, [425, 50])
            text = font.render("Press space to Unpause",True,WHITE)
            screen.blit(text, [350, 600])
            
            pygame.draw.ellipse(screen,RED,(504,ymove+22,17,30),0)
            pygame.draw.ellipse(screen,ORANGE,(506,ymove+17,13,30),0)
            pygame.draw.ellipse(screen,RED,(255,ymove+22,17,30),0)
            pygame.draw.ellipse(screen,ORANGE,(257,ymove+17,13,30),0)
            pygame.draw.ellipse(screen,RED,(755,ymove+22,17,30),0)
            pygame.draw.ellipse(screen,ORANGE,(757,ymove+17,13,30),0)
            pygame.draw.ellipse(screen,RED,(1004,ymove+22,17,30),0)
            pygame.draw.ellipse(screen,ORANGE,(1006,ymove+17,13,30),0)
            screen.blit(destroyer,(250,ymove))
            screen.blit(crusier,(500,ymove))
            screen.blit(millenium_falcon,(750,ymove))
            screen.blit(death_star,(1000,ymove))
            sped=sped**1.07
            ymove-=sped
            if ymove<-50:
                ymove=710
                sped=1.1
            if pygame.key.get_pressed()[pygame.K_SPACE]:
                paused=False
                pygame.display.flip()
            pygame.display.flip()
            clock.tick(20)
    def explosion(stage,x,y):
        screen.blit(stage,(x-25,y-25))
        pygame.display.flip()
        time.sleep(0.02)
#-------------------------------no more functions-----------------------------------                
    #creates all the bullets
    bullet_creation(bullet_list)
    bullet_creation(bullet_lists)
    bullet_creation(bullets_list)
    bullet_creation(bullets_lists)
    
    redraw=True
    coinx=0
    coiny=0
    ships=ship()
    
    #starting postition
    ships.x=600
    ships.y=650
    
    #speed of bullets
    speed=choice()
    #color of ship
    ships.type=Type()
    p=False
    maine = False
    #---------------------------------------MAIN------------------------------------
    while not maine:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                maine=True
                global INTRO
                INTRO=True
        #pause option
        if pygame.key.get_pressed()[pygame.K_p]:
            pause()
            p=True       
        screen.blit(bg,(-200,0))
        font = pygame.font.SysFont('Impact', 25, False, False)
        text = font.render("Your score is "+str(score),True,RED)
        screen.blit(text, [0, 0])

        #ship movement
        if pygame.key.get_pressed()[pygame.K_UP]:
            if ships.y<0:
                    ships.y+=0
            else:
                    ships.y -= 5
                    pygame.draw.ellipse(screen,RED,(ships.x-2,ships.y+15,17,31),0)
                    pygame.draw.ellipse(screen,ORANGE,(ships.x,ships.y+11,13,31),0)
        if pygame.key.get_pressed()[pygame.K_DOWN]:
            if ships.y>695:
                    ships.y+=0
            else:
                    ships.y += 5
        if pygame.key.get_pressed()[pygame.K_LEFT]:
            if ships.x<0:
                    ships.x+=0
            else:
                ships.x -= 5
                pygame.draw.ellipse(screen,RED,(ships.x-2,ships.y+15,17,30),0)
                pygame.draw.ellipse(screen,ORANGE,(ships.x,ships.y+11,13,30),0)
        if pygame.key.get_pressed()[pygame.K_RIGHT]:
            if ships.x>1195:
                    ships.x+=0
            else:
                ships.x += 5
                pygame.draw.ellipse(screen,RED,(ships.x-2,ships.y+15,17,30),0)
                pygame.draw.ellipse(screen,ORANGE,(ships.x,ships.y+11,13,30),0)
        coins=coin(screen,redraw,coinx,coiny)
        #draws ship
        ships.draw(screen)
        
        #moves bullets in its corisponding directions
        bullet_move_vertical(bullet_list,speed)
        bullet_move_vertical(bullet_lists,-speed)
        bullet_move_horizontal(bullets_list,-speed)
        bullet_move_horizontal(bullets_lists,speed)
        
        coiny=coins[1]
        coinx=coins[0]
        redraw=coins[2]
        bonus=coin_collision(ships.x,ships.y,coinx,coiny,speed)
        #scoring system
        score=score+0.25*speed+bonus[0]
        redraw=bonus[1]
        
        #resets bonus
        bonus=0
        dead=detect_collision(ships.x,ships.y)
        pygame.display.flip()
        if p==True:
            z=4
            for i in range (3):
                screen.blit(bg,(-200,0))
                z-=1
                font = pygame.font.SysFont('Impact', 100, False, False)
                text = font.render("Resuming in "+str(z),True,WHITE)
                screen.blit(text, [300, 300])
                
                ships.draw(screen)
                #moves bullets in its corisponding directions
                bullet_move_vertical(bullet_list,0)
                bullet_move_vertical(bullet_lists,0)
                bullet_move_horizontal(bullets_list,0)
                bullet_move_horizontal(bullets_lists,0)
                
                coiny=coins[1]
                coinx=coins[0]
                redraw=coins[2]
                bonus=coin_collision(ships.x,ships.y,coinx,coiny,speed)
                pygame.display.flip()
                time.sleep(1)
            p=False
        if dead==True:
            
            pygame.mixer.music.load('Explosion_sound (1).wav')
            pygame.mixer.music.play(1)
            pygame.display.flip()
             
            #if dead draws an explosion
            explosion(xpn1,ships.x,ships.y)
            explosion(xpn2,ships.x,ships.y)
            explosion(xpn3,ships.x,ships.y)
            explosion(xpn4,ships.x,ships.y)
            explosion(xpn5,ships.x,ships.y)
            explosion(xpn6,ships.x,ships.y)
            explosion(xpn7,ships.x,ships.y)
            explosion(xpn8,ships.x,ships.y)
            explosion(xpn9,ships.x,ships.y)
            explosion(xpn10,ships.x,ships.y)
            explosion(xpn11,ships.x,ships.y)
            explosion(xpn12,ships.x,ships.y)
            explosion(xpn13,ships.x,ships.y)
            explosion(xpn14,ships.x,ships.y)
            explosion(xpn15,ships.x,ships.y)
            explosion(xpn16,ships.x,ships.y)

            time.sleep(1)
            pygame.mixer.music.load("obiwan (1).wav")
            pygame.mixer.music.play(1)
            pygame.display.flip()
            
            #tells you when you died
            font = pygame.font.SysFont('Impact', 200, False, False)
            text = font.render("You Died!",True,RED)
            screen.blit(text, [200, 200])
            pygame.display.flip()
            
            font = pygame.font.SysFont('Impact', 100, False, False)
            text = font.render("Your score is "+str(score),True,RED)
            screen.blit(text, [200, 400])
            pygame.display.flip()
            time.sleep(2)
            pygame.mixer.music.load('imperial_march (1).wav')
            pygame.mixer.music.play(-1)
            
            #tracks score
            print ("Your score was", score)
            maine=True
                   
            pygame.display.flip()
        clock.tick(20)
    time.sleep(2)
INTRO=False    
#-------------------------------------------menu system----------------------------------------
while INTRO==False:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            INTRO=True
    screen.blit(menu,(-300,0))
    #play box
    rect_playx=100
    rect_playy=100
    play='play'
    
    #instruction box
    rect_insx=700
    rect_insy=100
    instructions='ins'
    
    #quit box
    rect_quitx=100
    rect_quity=400
    quits='quits'
    
    #creates boxes tests if the user clicks on them
    box(rect_insx,rect_insy,instructions)
    box(rect_playx,rect_playy,play)
    box(rect_quitx,rect_quity,quits)
    font = pygame.font.SysFont('Impact', 50, False, False)
    
    #puts the following text on the corrisponding boxes
    text = font.render("PLAY GAME",True,WHITE)
    screen.blit(text, [rect_playx+50, rect_playx+70])
    
    text = font.render("INSTRUCTIONS",True,WHITE)
    screen.blit(text, [rect_insx+15, rect_insy+70])
    
    text = font.render("QUIT",True,WHITE)
    screen.blit(text, [rect_quitx+125, rect_quity+70])
    
    pygame.display.flip()
    clock.tick(20)
pygame.quit()
sys.exit()
