# -*- coding: utf-8 -*-
"""
Created on Sun Jan  2 21:05:15 2022

@author: utilisateur
"""

from PIL import Image, ImageTk

class projectile:
    
    def __init__(self, x, y, canvas):
        

        self.__x = x
        self.__y = y
        self.vel = -20
        self.canvas = canvas
        #self.image = canvas.create_rectangle( self.__x+10, self.__y+10, self.__x+20, self.__y+20, fill='yellow')
        self.image = Image.open("Image/rocher.png")
        self.redi_image = ImageTk.PhotoImage(self.image.resize((50,50)))
        self.rocher = self.canvas.create_image(self.__x,self.__y, image = self.redi_image, anchor='nw' )
        self.height = 10
        self.width = 10
        self.degats = -1
        self.vie = 1

        
    def run(self, lst_projectiles):
        """ déplacement du projectile jusqu'en haut de l'écran et l'éfface(visuel et liste projectile dans player) une fois sortit de l'écran
            lst_projectile : la liste de player conenant tt les projectiles lancés"""
        #print('on est dans run projectile')
        
        if self.__y >= 1 and self.vie >= 1:
            # si on est dans la fenêtre on continue de faire bouger le rocher
            self.canvas.move(self.rocher, 0, self.vel)
            self.__y = self.canvas.coords(self.rocher)[1]
            self.canvas.after(55, self.run, lst_projectiles)
 
        else :
            
            # on n'affiche plus le projectile
            self.canvas.delete(self.rocher)
            del lst_projectiles[0]


    def collision(self, enemy):
        

        x_1 = self.canvas.bbox(self.rocher)[0] 
        x_2 = self.canvas.bbox(self.rocher)[2] 
        y_1 = self.canvas.bbox(self.rocher)[1] 
        y_2 = self.canvas.bbox(self.rocher)[3] 
        #print(self.canvas.find_overlapping(x_1, y_1, x_2, y_2) )
            
        # les coordonnées de notre enemy
        coords = self.canvas.bbox(enemy.mechant)
            
        if (x_2 > coords[0]> x_1) and (y_1 < coords[1]< y_2):
            #print('collision  geuche !')
            enemy.perds_vie(self.degats)
            self.vie += -1
                
        elif (x_2 > coords[2]> x_1) and (y_1 < coords[3]< y_2):
            #print('collision  droite !')
            enemy.perds_vie(self.degats)
            self.vie += -1
                

        
              