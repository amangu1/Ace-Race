import pygame, sys
from pygame.locals import *
import random




pygame.init()
GAMEWORLD = pygame.display.set_mode((1200,600 ))
Sky = (0,255,255)
GAMEWORLD.fill(Sky) #set background color
pygame.display.set_caption('Ace Race')

mainloop = True

pygame.mixer.music.load('Music.mp3')
pygame.mixer.music.set_endevent(pygame.constants.USEREVENT)
pygame.mixer.music.play()

planex=40#plane variables
planey=40
uppressed = 0
downpressed = 0

fpsClock=pygame.time.Clock()
GAMEWORLD.set_alpha(225)

score = 0
font = pygame.font.Font(None, 35)
black = (0,0,0)




PlaneImg1=pygame.image.load('Plane.png').convert_alpha()
PlaneImg2=pygame.image.load('Plane2.png').convert_alpha()
CloudImg=pygame.image.load('Cloud 1.png').convert_alpha()
CloudImg2=pygame.image.load('Cloud 2.png').convert_alpha()
CloudImg3 = pygame.image.load('Cloud 3.png').convert_alpha()
Background = pygame.image.load('Background.png').convert()
BuildingImg1 = pygame.image.load('Building 2.png').convert_alpha()
BuildingImg2 = pygame.image.load('Building.png').convert_alpha()
BuildingImg3 = pygame.image.load('Building 3.png').convert_alpha()
purple = (255,128,255)
GAMEWORLD.set_colorkey(purple)
  

planeanimation = 0
planecycle = 0 #Plane animation

Cloudspawn = random.randrange(0,100)#Cloud Variables
Cloudwait = 80
Cloudwaitbase = 80
Cloudy1 =  random.randrange(25,300)
Cloudx1 = 1300
Cloudy2 =  random.randrange(25,300)
Cloudx2 = 1300
Cloudy3 =  random.randrange(25,300)
Cloudx3 = 1300
Cloudy4 =  random.randrange(25,300)
Cloudx4 = 1300
Cloudy5 =  random.randrange(25,300)
Cloudx5 = 1300
Cloudy6 =  random.randrange(25,300)
Cloudx6 = 1300
Cloud1 = 0
Cloud2 = 0
Cloud3 = 0
Cloud4 = 0
Cloud5 = 0
Cloud6 = 0
Nocloud = 0
cloudspeed = 3
difficultycounter = 0






Buildingx1 = 1300
Buildingy1 = 250
Buildingx2 = 1300
Buildingy2 = 440
Buildingx3 = 1300
Buildingy3 = 230
Buildingx4 = 1300
Buildingy4 = 270
Building1 = 0
Building2 = 0
Building3 = 0
Building4 = 0
Nobuild = 0
Buildwait = 120
Buildwaitbase = 120
Buildspeed = 1






                














while mainloop==True: # main game loop
    GAMEWORLD.blit(Background,[0,0]) #reset background

    score = score+13
    difficultycounter = difficultycounter+1
    displayscore = font.render(str(score),1,black)
    

    
    if(planecycle == 8):
        if(planeanimation == 0):
            GAMEWORLD.blit(PlaneImg2,(planex,planey))#PLANE ANIMATION
            planeanimation = 1
            planecycle = 0
        else:
            GAMEWORLD.blit(PlaneImg1,(planex,planey))
            planeanimation = 0
            planecycle = 0
    else:
        planecycle = planecycle + 1
        if (planeanimation == 0):
            GAMEWORLD.blit(PlaneImg2,(planex,planey))
        elif(planeanimation == 1):
            GAMEWORLD.blit(PlaneImg1,(planex,planey))


            

    if Cloud1 == 1:
        Cloudx1= Cloudx1-cloudspeed
        GAMEWORLD.blit(CloudImg, (Cloudx1,Cloudy1))    #Cloud Movement
        if Cloudx1< -300:
            Cloud1 = 0
            Nocloud = 0
            Cloudx1 = 1250
        
    if Cloud2 == 1:
        Cloudx2 = Cloudx2-cloudspeed
        GAMEWORLD.blit(CloudImg, (Cloudx2,Cloudy2))
        if Cloudx2 < -300:
            Cloud2 = 0
            Nocloud = 0
            Cloudx2 = 1250

    if Cloud3 == 1:
        Cloudx3 = Cloudx3-cloudspeed
        GAMEWORLD.blit(CloudImg2, (Cloudx3,Cloudy3))
        if Cloudx3 < -300:
            Cloud3 = 0
            Nocloud = 0
            Cloudx3 = 1250   
    if Cloud4 == 1:
        Cloudx4 = Cloudx4-cloudspeed
        GAMEWORLD.blit(CloudImg2, (Cloudx4,Cloudy4))
        if Cloudx4 < -300:
            Cloud4 = 0
            Nocloud = 0
            Cloudx4 = 1250
    if Cloud5 == 1:
        Cloudx5 = Cloudx5-cloudspeed
        GAMEWORLD.blit(CloudImg3, (Cloudx5,Cloudy5))
        if Cloudx5 < -300:
            Cloud5 = 0
            Nocloud = 0
            Cloudx5 = 1250
    if Cloud6 == 1:
        Cloudx6 = Cloudx4-cloudspeed
        GAMEWORLD.blit(CloudImg3, (Cloudx6,Cloudy6))
        if Cloudx6 < -300:
            Cloud6 = 0
            Nocloud = 0
            Cloudx6 = 1250





            
    if Building1 == 1:
        Buildingx1= Buildingx1-Buildspeed
        GAMEWORLD.blit(BuildingImg3, (Buildingx1,Buildingy1))    #Building Movement
        if Buildingx1< -300:
            Building1 = 0
            Nobuild = 0
            Buildingx1 = 1250

        
    if Building2 == 1:
        Buildingx2 = Buildingx2-Buildspeed
        GAMEWORLD.blit(BuildingImg2, (Buildingx2,Buildingy2))
        if Buildingx2 < -300:
            Building2 = 0
            Nobuild = 0
            Buildingx2 = 1250

    if Building3 == 1:
        Buildingx3 = Buildingx3-Buildspeed
        GAMEWORLD.blit(BuildingImg1, (Buildingx3,Buildingy3))
        if Buildingx3 < -300:
            Building3 = 0
            Nobuild = 0
            Buildingx3 = 1250
    if Building4 == 1:
        Buildingx4 = Buildingx4-Buildspeed
        GAMEWORLD.blit(BuildingImg3, (Buildingx4,Buildingy4))
        if Buildingx4 < -300:
            Building4 = 0
            Nobuild = 0
            Buildingx4 = 1250











    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == KEYDOWN:
            if (event.key == K_w): #Plane Movement
                uppressed = 1
            elif (event.key == K_s):
                downpressed = 1
        elif event.type == KEYUP:
            if (event.key == K_w):
                uppressed = 0
            elif (event.key == K_s):
                 downpressed = 0
        elif event.type == pygame.constants.USEREVENT:
            pygame.mixer.music.play()
                 
    if (uppressed == 1):
        if (uppressed-downpressed == 0):#if both are pressed nothing happens
            planey=planey
        else:
            planey = planey-3
    elif(downpressed == 1):
        if (downpressed - uppressed == 0):
            planey-=planey
        else:
            planey = planey+5
    else:
        planey = planey





        

    if planey <= -35:  #offscreen collision
        mainloop = False

    if planey >= 560:
        mainloop = False








        
    if (planey<Cloudy1+70 and Cloudy1-10<planey and planex<Cloudx1+90 and Cloudx1-80<planex):
        mainloop = False
         
    if (planey<Cloudy2+70 and Cloudy2-10<planey and planex<Cloudx2+90 and Cloudx2-80<planex):
        mainloop = False
   
    if (planey<Cloudy3+70 and Cloudy3-10<planey and planex<Cloudx3+90 and Cloudx3-80<planex):
        mainloop = False
        
    if (planey<Cloudy4+70 and Cloudy4-10<planey and planex<Cloudx4+90 and Cloudx4-80<planex):#CloudCollision
        mainloop = False

    if (planey<Cloudy5+70 and Cloudy5-10<planey and planex<Cloudx5+90 and Cloudx5-80<planex):
        mainloop = False

    if (planey<Cloudy6+70 and Cloudy6-10<planey and planex<Cloudx6+90 and Cloudx6-80<planex):

        
        mainloop = False
        
    if (planey-60>Buildingy1 and planex-150<Buildingx1 and Buildingx1-20<planex):
        mainloop = False
        
    if (planey+15>Buildingy1 and planex-130<Buildingx1 and Buildingx1+25<planex):
        mainloop = False
    
         
    if (planey+20>Buildingy2 and planex-60<Buildingx2 and Buildingx2-100<planex):
        mainloop = False
        
    if (planey-45>Buildingy3 and planex-150<Buildingx3 and Buildingx3-20<planex):
        mainloop = False
        
    if (planey+40>Buildingy3 and planex-130<Buildingx3 and Buildingx3+35<planex):
        mainloop = False
        
    if (planey-60>Buildingy4 and planex-150<Buildingx4 and Buildingx4-20<planex):
        mainloop = False
        
    if (planey+15>Buildingy4 and planex-130<Buildingx4 and Buildingx4+25<planex):
        mainloop = False








    if Cloudwait <= 0:
        Cloudspawn = random.randrange(1,100)
    
        if Cloudspawn >= 60:
            Cloudwait = Cloudwaitbase #will a cloud be generated?
            if Cloud1 == 1 and Cloud2 == 1 and Cloud3 == 1 and Cloud4 == 1:
                Nocloud = 1
                Cloudwait = Cloudwaitbase
            elif Cloud1 != 1:#does cloud1 exist?
                Cloudy1 =  random.randrange(-50,300)
                
                Cloud1 = 1
                Cloudwait = Cloudwaitbase
            elif Cloud3 !=1:
                Cloudy3 =  random.randrange(-20,300)
                
                Cloud3 = 1#does cloud3 exist
                Cloudwait = Cloudwaitbase
            elif Cloud2 !=1:
                Cloudy2 =  random.randrange(-50,300)
                
                Cloud2 = 1#does cloud2 exist
                Cloudwait = Cloudwaitbase
            elif Cloud6 !=1:
                Cloudy6 =  random.randrange(-20,300)
                
                Cloud6 = 1#does cloud4 exist
                Cloudwait = Cloudwaitbase
            elif Cloud4 !=1:
                Cloudy4 =  random.randrange(-50,250)
                
                Cloud4 = 1#does cloud4 exist
                Cloudwait = Cloudwaitbase
            elif Cloud5 !=1:
                Cloudy5 =  random.randrange(-50,300)
                
                Cloud5 = 1#does cloud4 exist
                Cloudwait = Cloudwaitbase

        else:
            Cloudwait = Cloudwaitbase
            
            
    else:
        Cloudwait = Cloudwait-1

        
            
    if Buildwait <= 0:
        Buildspawn = random.randrange(1,100)
    
        if Buildspawn >= 50:
            Buildwait = Buildwaitbase #will a cloud be generated?
            if Building1 == 1 and Building2 == 1 and Building3 == 1 and Building4 == 1:
                Nobuild = 1
                Buildwait = Buildwaitbase
            elif Building1 != 1:#does cloud1 exist?
                
                Building1 = 1
                Buildwait = Buildwaitbase
            elif Building3 !=1:
                
                Building3 = 1#does cloud2 exist
                Buildwait = Buildwaitbase
            elif Building2 !=1:
                
                Building2 = 1#does cloud3 exist
                Buildwait = Buildwaitbase

            elif Building4 !=1:
                
                Building4 = 1#does cloud4 exist
                Buildwait = Buildwaitbase
        else:
            Buildwait = Buildwaitbase
            
    else:
        Buildwait = Buildwait-1





    




        








    if difficultycounter==500:#exponential difficulty
        difficultycounter = 0
        if Cloudwaitbase>10:
            Cloudwaitbase=Cloudwaitbase-10
        cloudspeed = cloudspeed+1
        Buildspeed = Buildspeed + 1
        if Buildwaitbase>20:
            Buildwaitbase = Buildwaitbase-10






    GAMEWORLD.blit(displayscore,(1000,20))        
    pygame.display.update()
    fpsClock.tick(45)


GAMEWORLD.blit(Background,[0,0])
GAMEWORLD.blit(displayscore,(550,250))
pygame.display.update()
pygame.time.delay(10000)
pygame.quit()               
sys.exit()

