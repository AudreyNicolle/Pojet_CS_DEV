# -*- coding: utf-8 -*-
"""
Created on Tue Dec 21 21:17:22 2021

@author: emma1
"""
from PIL import Image, ImageTk


class mechant :
    
    def __init__(self, window,canvas, x, y):
        """ parameters :
            
                canvas : la zone où doit être affiché le méchant
        
        """
        self.__canvas = canvas
        self.__x= x
        self.__y = y
        #self.mechant = canvas.create_rectangle( self.__x+20, self.__y+20, self.__x+40, self.__y+40, fill='red')
        self.image = Image.open("Image/sorcier.png")
        self.redi_image = ImageTk.PhotoImage(self.image.resize((50,50))) 
        self.mechant = self.__canvas.create_image(self.__x,self.__y, image = self.redi_image, anchor='center' )
        self.width = 20
        self.height = 20
        self.dir = 1
        self.vel = self.dir*0.05
        self.window = window
        self.vie = 2
        
    def get_x_y(self):
        return (self.__x, self.__y, self.__x+self.width, self.__y+self.height)
        
    def move(self): 
        if self.vie >= 1:
            #les conditions pour que l'éney ne sorte pas de l'écran
            if self.__x >= 800:
                self.dir = -1
                #print("gauche")
                    
            elif self.__x <= 2:
                self.dir =1
                #print("droite")
            
            #self.__x += self.vel*self.dir
            #print(self.__x)
            
            """
            # on bouge l'enemy
            self.__canvas.coords(self.mechant, self.__x+20, self.__y+20, self.__x+40, self.__y+40)
            #print("déplacement")
            self.__canvas.after(1, self.move)
            """
            # on bouge l'enemy
            self.__canvas.move(self.mechant,self.vel*self.dir,0)
            # we get the position of our image
            self.__x = self.__canvas.coords(self.mechant)[0]
            self.__y = self.__canvas.coords(self.mechant)[1]
            self.__canvas.after(1, self.move)

        
    def perds_vie(self, degats):
        self.vie += degats