# -*- coding: utf-8 -*-
"""
Created on Sat Jan  1 20:43:01 2022

@author: emma1
"""
import projectile as pj
from PIL import Image, ImageTk

class player :
    
    def __init__(self,window, canvas):
        
        self.__x = 400
        self.__y = 600
        self.vel = 10
        self.canvas = canvas
        self.window = window
        #self.__image = canvas.create_rectangle( self.__x+20, self.__y+20, self.__x+40, self.__y+40, fill='blue')
        self.image = Image.open("Image\yeti.png")
        self.redi_image = ImageTk.PhotoImage(self.image.resize((50,50)))
        self.yeti = self.canvas.create_image(self.__x,self.__y, image = self.redi_image )
        self.projectiles = [ ]
        
        
    def move_right(self, evt):
        """ déplacement à droite """
        self.__x += self.vel
        self.canvas.move(self.yeti, self.vel, 0)
        
    def move_left(self, evt):
        """ déplacement à gauche """
        
        self.__x += -self.vel
        self.canvas.move(self.yeti, -self.vel, 0)
        
    def crea_projectile (self, event):
        """ création d'un projectile, objet de classe projectile """
        # comme on ne peut avoir que 1 projectile à l'écran 
        if len(self.projectiles) <= 0:
            self.projectiles.append( pj.projectile(self.__x, self.__y, self.canvas) )
            self.projectiles[-1].run(self.projectiles)
           

    def key_event(self):
        """ gère les actions de clavier : déplacement à droite et gauche, tir """
        #print("début evenements de clavier ")
        self.window.bind('<Right>', self.move_right)
        self.window.bind('<Left>', self.move_left)
        self.window.bind('<space>', self.crea_projectile)
        self.canvas.focus_set()
        #print("fin evenements de clavier ")


    
    def tout(self):
        
        self.key_event()
        
      