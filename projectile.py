# -*- coding: utf-8 -*-
"""
Created on Sun Jan  2 21:05:15 2022
@author: utilisateur
"""
import tkinter as tk
from PIL import Image, ImageTk

class projectile:
    
    def __init__(self, x, y, canvas):
        
        self.__x = x
        self.__y = y
        self.vel = 0.01
        self.canvas = canvas
        self.image = Image.open("Image\boule_de_feu.png")
        self.redi_image = ImageTk.PhotoImage(self.image.resize((50,50))) 
        self.mechant = self.__canvas.create_image(self.__x,self.__y, image = self.redi_image)
        
    def run(self):
        """ déplacement du projectile jusqu'en haut de l'écran """
        print('on est dans run projectile')
        #if self.__y >= 1:
            #print("le projectile doit être visible")
        self.__y += -self.vel
        print(self.__y)
        self.canvas.move(self.image, 0, self.vel)
        #self.__canvas.after(1, self.run)
            
          
        """else :
            print("le projectile est effacé")
            self.canvas.delete(self.image)
            return True"""
