# -*- coding: utf-8 -*-
"""
Created on Tue Dec 21 21:17:22 2021
@author: emma1
"""
import tkinter as tk
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
        self.image = Image.open("Image\sorcier.png")
        self.redi_image = ImageTk.PhotoImage(self.image.resize((50,50))) 
        self.mechant = self.__canvas.create_image(self.__x,self.__y, image = self.redi_image )
        self.largeure = 20
        self.height = 20
        self.dir = 1
        self.vel = self.dir*0.05
        self.window = window
        


        
    def move(self): 
        
        #les conditions pour que l'énemy ne sorte pas de l'écran
        if self.__x >= 800:
            self.dir = -1
            #print("gauche")
                
                
        elif self.__x <= 2:
            self.dir =1
            #print("droite")
        
        #print(self.__x)
        
        
        # on bouge l'enemy
        self.__canvas.move(self.mechant,self.vel*self.dir,0)
        self.__x = self.__canvas.bbox(self.mechant)[0]
        print(self.__x)
        #print("déplacement")
        self.__canvas.after(1, self.move)

    def image_perso (self) : 
        
        image_me = tk.PhotoImage(file = "yeti.png" )
        self.__canvas.create_image(0,0,image = image_me )
        
        
        
        