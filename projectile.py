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
        self.vel = -30
        self.canvas = canvas
        #self.image = canvas.create_rectangle( self.__x+10, self.__y+10, self.__x+20, self.__y+20, fill='yellow')
        self.image = Image.open("Image\sorcier.png")
        self.redi_image = ImageTk.PhotoImage(self.image.resize((50,50)))
        self.rocher = self.canvas.create_image(self.__x,self.__y, image = self.redi_image )
        self.height = 10
        self.width = 10
        self.degats = -1
        self.vie = 1
        #print("projectile CREE")
        
    def run(self, lst_projectiles):
        """ déplacement du projectile jusqu'en haut de l'écran et l'éfface(visuel et liste projectile dans player) une fois sortit de l'écran
            lst_projectile : la liste de player conenant tt les projectiles lancés"""
        #print('on est dans run projectile')
        
        if self.__y >= 1 and self.vie >= 1:
            #print("le projectile doit être visible")
            self.__y += self.vel
            #print("déplacement du projectile", self.__y)
            self.canvas.move(self.rocher, 0, self.vel)
            self.canvas.after(50, self.run, lst_projectiles)
 
        else :
            
            # on n'affiche plus le projectile
            self.canvas.delete(self.rocher)
            del lst_projectiles[0]
            #print(lst_projectiles)
            #print("le projectile est effacé")

    def collision(self, objet):
         #gère les dégats donnés et reçus ( le missile enlève autant de points de vie qu'il fait de dégats et en perds autant) 
        
        print("on est dans collision")
        #les x, y min et max de l'objet encollision(?) sur l'écran
        print(self.canvas.bbox(self.rocher))
        x_1, y_1, x_2, y_2 = self.canvas.bbox(self.rocher)
        print(self.__x)
        
        # le coin gauche de l'objet est dans la zone des x du projectile 
        if  self.__x >= x_1  and x_1<= (self.__x+self.width):
            print("angle guauche enemy")
            

                
                
                
                
                
                
                
                
                