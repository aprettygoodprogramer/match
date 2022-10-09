#imports random
import random
#imports pygame
import pygame
#import time
import time
#gets key words for mpygame
from pygame.locals import *
#inits pygame
pygame.init()
#gets the mouse poss
mx, my = pygame.mouse.get_pos()
#makes mosue hit box
mouse_hitbox = (mx, my, 20, 20)
mouse_rect = pygame.Rect(mouse_hitbox)
#gets the image comp
comp = pygame.image.load("COMP.png")
#gets the image keyboard
keyboard = pygame.image.load("KEYBOARD.png")
#gets the image mine
mine = pygame.image.load("MINE.png")
#gets the image mosue
mouse = pygame.image.load("MOUSE.png")
#gets the image py
py =  pygame.image.load("PY.png")
#gets the image r_cube
r_cube = pygame.image.load("r_cube.png")
#makes the screen
screen=pygame.display.set_mode((1000, 1000))
#fills the screen
screen.fill((255, 255,  255))
#updates the screen
pygame.display.flip()
#all the x cords
list_of_cords_x = [850, 850, 850, 850, 745, 640, 535, 430, 745, 440, 535, 640]
#all the y cords
list_of_cords_y = [755, 650, 545, 440, 850, 850, 850, 850, 745, 440, 545, 650]
#sets runnig to false
running = True
#sets flag to False
flag = False
#sets the windows name
pygame.display.set_caption("match")
#sets the cards fliped to a empty list
cards_fliped = []

#the main card class
#you have to pass in a x, y and a pic
class card:
    def __init__(self,  pic, x, y, dupe, has_been_clicked, index_num):
        self.pic = pic
        #resizes the pic
        self.pic = pygame.transform.scale(self.pic,(100,100))
        self.x = x
        self.y = y
        self.dupe = dupe
        self.has_been_clicked = has_been_clicked
        #the stats for the back of the card
        self.back_of_card_stat = (x, y, 100, 100)
        #the real rect
        self.back_of_card = pygame.Rect(self.back_of_card_stat)
        self.index_num = index_num
        self.show = True
    def Display(self):
        
        #Displays the image
        #if has been click = True show front of card else show back
        if self.has_been_clicked == False and self.show == True:

            pygame.draw.rect(screen, (100, 78, 200), self.back_of_card)
        elif self.has_been_clicked == True and self.show == True:

            screen.blit(self.pic, (self.x, self.y))
    #returns has been cliked
    def get_has_been_clicked(self):
        return self.has_been_clicked
    #makes has_been_clikes to True
    def change_has_been_click_True(self):
        self.has_been_clicked = True
    def change_has_been_click_True(self):
        self.has_been_clicked = True
    #makes has_been_clikes to False
    def change_has_been_click_False(self):
        self.has_been_clicked = False
    #retruns the back of the card
    def get_back_of_card(self):
        return self.back_of_card
    def get_index(self):
        #returns the index
        return self.index_num
    def get_show(self):
        #retruns show
        return self.show
    def change_show(self):
        #changes show
        self.show = False
    #returs dupe
    def get_dupe(self):
        return self.dupe
#makes every card
#each card will take in a pic a x a y and if its a duplacate card or the first card then if its fliped
#it chooses the x and y from a list the removes it
#then we put it all in to a list to be used
#comp1 
wich = random.randint(1, 12)
wich-=1
comp1 = card(comp, list_of_cords_x[wich], list_of_cords_y[wich], False, False, 1)
list_of_cords_x.pop(wich)
list_of_cords_y.pop(wich)

wich = random.randint(1, 11)
wich-=1

#keyboard1
keyboard1 = card(keyboard, list_of_cords_x[wich], list_of_cords_y[wich], False, False,2  )
list_of_cords_x.pop(wich)
list_of_cords_y.pop(wich)
#mine 1
wich = random.randint(1, 10)
wich-=1
mine1 = card(mine, list_of_cords_x[wich], list_of_cords_y[wich], False, False, 3)
list_of_cords_x.pop(wich)
list_of_cords_y.pop(wich)
#mouse 1
wich = random.randint(1, 9)
wich-=1
mouse1 = card(mouse, list_of_cords_x[wich], list_of_cords_y[wich], False, False, 4)
list_of_cords_x.pop(wich)
list_of_cords_y.pop(wich)

wich = random.randint(1, 8)
wich-=1
#comp 2
comp2 = card(comp, list_of_cords_x[wich], list_of_cords_y[wich], True, False, 1)
list_of_cords_x.pop(wich)
list_of_cords_y.pop(wich)
#keyboard 2
wich = random.randint(1, 7)
wich-=1
keyboard2 = card(keyboard, list_of_cords_x[wich], list_of_cords_y[wich], True, False, 2)
list_of_cords_x.pop(wich)
list_of_cords_y.pop(wich)
#mine 2
wich = random.randint(1, 6)
wich-=1
mine2 = card(mine, list_of_cords_x[wich], list_of_cords_y[wich], True, False, 3)
list_of_cords_x.pop(wich)
list_of_cords_y.pop(wich)
#mouse 2
wich = random.randint(1, 5)
wich-=1
mouse2 = card(mouse, list_of_cords_x[wich], list_of_cords_y[wich], True, False, 4)
list_of_cords_x.pop(wich)
list_of_cords_y.pop(wich)
wich = random.randint(1, 4)
wich-=1
#py 1
py1 = card(py, list_of_cords_x[wich], list_of_cords_y[wich],False, False, 5)
list_of_cords_x.pop(wich)
list_of_cords_y.pop(wich)
wich = random.randint(1, 3)
wich-=1
#py 2
py2 = card(py, list_of_cords_x[wich], list_of_cords_y[wich],True, False, 5)
list_of_cords_x.pop(wich)
list_of_cords_y.pop(wich)
wich = random.randint(1, 2)
wich-=1
#r cube 1
r_cube1 = card(r_cube, list_of_cords_x[wich], list_of_cords_y[wich], False, False, 6)
list_of_cords_x.pop(wich)
list_of_cords_y.pop(wich)
wich = 1
wich-=1
#r cube 2
r_cube2 = card(r_cube, list_of_cords_x[wich], list_of_cords_y[wich], True, False, 6)
list_of_cords_x.pop(wich)
list_of_cords_y.pop(wich)
#all the cards
all_card_1 = [comp1, keyboard1, mine1, mouse1, py1, r_cube1]
all_card_2 = [comp2, keyboard2, mine2, mouse2, py2, r_cube2]
def collide():
    #al card in 1
    for i in all_card_1:
        #all cards in 2
        for x in all_card_2:
            #checks if your mosue collides and if you click and if its not already showing for bolth list
            if i.get_back_of_card().colliderect(mouse_rect) and event.type == pygame.MOUSEBUTTONDOWN and i.get_has_been_clicked() == False and i.get_show() == True:
                ##flips the card over
                i.change_has_been_click_True()
                #appends to the cards you fliped over
                cards_fliped.append(i)
            elif x.get_back_of_card().colliderect(mouse_rect) and event.type == pygame.MOUSEBUTTONDOWN and x.get_has_been_clicked() == False and i.get_show() == True:
                #flips card over
                cards_fliped.append(x)
                #appends to the cards you fliped over
                x.change_has_been_click_True()


while running == True:
    #gets the mouse poss
    mx, my = pygame.mouse.get_pos()
    #makes the screen
    screen=pygame.display.set_mode((1000, 1000))
    #fills the screen with white
    screen.fill((255, 255,  255))
    #updates the mouse hitbox
    mouse_hitbox = (mx, my, 20, 20)
    mouse_rect = pygame.Rect(mouse_hitbox)
    #draws mouse hitbox
    pygame.draw.rect(screen, (0, 0, 0), mouse_rect, 2)
    #if the X is hit close pygame
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
    #displays all the cards in card 1
    for i in all_card_1:
        i.Display()



    #displays all the cards in card 2
    for i in all_card_2:
        i.Display()
    #if the player hit 3 or more cards flip them back over
    if len(cards_fliped) >= 3:
            cards_fliped[0].change_has_been_click_False()
            cards_fliped[1].change_has_been_click_False()
            cards_fliped[2].change_has_been_click_False()
            cards_fliped = []
    #if player has fliped 3 cards then start timer to show card for 1 second
    if len(cards_fliped) == 2 and flag == False:
        starttime = pygame.time.get_ticks()
        flag = True
    #shows card for 1 second
    elif len(cards_fliped) == 2 and pygame.time.get_ticks() - starttime >= 1000:
        if cards_fliped[0].get_index() == cards_fliped[1].get_index():
            #says what side
            #rmoves if they got card right
            #it checks dupe and that tell wich one they hit first therfor I know wich card to remove from wich list 
            if cards_fliped[0].get_dupe() == False:
                all_card_2.remove(cards_fliped[1])
                all_card_1.remove(cards_fliped[0])

            else:
                all_card_2.remove(cards_fliped[0])
                all_card_1.remove(cards_fliped[1])
        else:
            #if they got cards wrong flip them back over
            cards_fliped[0].change_has_been_click_False()
            cards_fliped[1].change_has_been_click_False()
        cards_fliped = []

        flag = False
    #runs collide func
    collide()
    #updates screen
    pygame.display.update()
pygame.quit()