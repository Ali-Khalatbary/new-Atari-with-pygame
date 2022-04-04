import pygame
from random import randint

pygame.init()
window = pygame.display.set_mode((800,500))
flag2 = 0
#bg
bg = pygame.image.load('bg.JPG')

#Rocket
Rocket = pygame.image.load('Rocket.PNG')
Rocket = pygame.transform.scale(Rocket,(70 , 100))
x_Rocket = 380

#bullet
bullet = pygame.image.load('tir.PNG')
bullet = pygame.transform.scale(bullet,(40 , 50))
y_bullet = 400
flag = 0
flag3 = True
x_bullet = x_Rocket+20

#golabi
golabi = pygame.image.load('golabi.PNG')
golabi = pygame.transform.scale(golabi,(80 , 70))
golabies = []
x_golabi = 0
y_golabi = 10

for i in range(15):
    alaki = []
    y_golabi = 80
    for i in range(4):
        alaki.append([x_golabi , y_golabi])
        y_golabi += 80
    golabies.append(alaki)
    x_golabi += 52

#go
game_over = pygame.image.load('game over.JPG')
game_over = pygame.transform.scale(game_over,(800 , 500))

#bomb
bomb = pygame.image.load('bomb.SVG')
bomb = pygame.transform.scale(bomb,(70 , 50))    
bomb_y = 461

#ghalb
joon = pygame.image.load('joon.SVG')
joon = pygame.transform.scale(joon,(50,50))
joons = [[0,0] , [ 70 , 0] , [140 , 0]]

#win
win = pygame.image.load('win.JPG')
win = pygame.transform.scale(win,(800,500))

r = True
while r:

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            r = False
        if e.type == pygame.KEYDOWN and flag2 == 0 :
            if e.key == pygame.K_RIGHT :
                x_Rocket += 20
            if e.key == pygame.K_LEFT :
                x_Rocket -= 20
            if e.key == pygame.K_SPACE:
        
                y_bullet = 400
                x_bullet = x_Rocket+20
                window.blit(bullet,(x_bullet , y_bullet))
                sotoon = x_bullet // 52
                baghimande = [golabies[sotoon][:-1]]
                golabies = golabies[:sotoon] + baghimande + golabies[sotoon+1:]
                if bomb_y > 460 :
                    bomb_y = 0
                    bomb_x = randint(30 , 760)
                flag = 1


    window.blit(bg,(0 ,0))
    pygame.time.delay(100)                
    
    for i in golabies:
        for j in i:
            window.blit(golabi,(j[0],j[1]))
    for i in joons :
            window.blit(joon , (i[0] , i[1]))

    if flag == 1 and y_bullet > 0:
        y_bullet -= 70
        window.blit(bullet,(x_bullet , y_bullet))
    window.blit(Rocket,(x_Rocket ,400))
    if flag == 1 and bomb_y < 460  : 
        window.blit(bomb,(bomb_x , bomb_y))
        bomb_y += 50

    if bomb_y >= 500:
        flag3 = False
    if bomb_y > 461 and (x_Rocket < bomb_x <= x_Rocket+70) and (400 <= bomb_y <= 500) and flag3:
        joons = joons[:-1]
        bomb_x,bomb_y = 2000,3000
        flag3 = False
    if joons == [] :
        window.blit(game_over,(0,0))
        flag2 = 1
    if golabies == [[], [] , [] , [] ,[] ,[] , [] , [] , [] , [] , [] , [] , [] , [] , []]:
        window.blit(win,(0,0))

    pygame.display.update()
