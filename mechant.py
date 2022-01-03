# -*- coding: utf-8 -*-
"""
Created on Tue Dec 21 21:17:22 2021

@author: emma1
"""



class mechant :
    
    def __init__(self, window,canvas, x, y):
        """ parameters :
            
                canvas : la zone où doit être affiché le méchant
        
        """
        self.__canvas = canvas
        self.__x= x
        self.__y = y
        self.mechant = canvas.create_rectangle( self.__x+20, self.__y+20, self.__x+40, self.__y+40, fill='red')
        self.width = 20
        self.height = 20
        self.dir = 1
        self.vel = self.dir*0.05
        self.window = window
        self.__vie = 2


        
    def move(self): 
        
        #les conditions pour que l'éney ne sorte pas de l'écran
        if self.__x >= 900:
            self.dir = -1
            #print("gauche")
                
        elif self.__x <= 2:
            self.dir =1
            #print("droite")
        
        self.__x += self.vel*self.dir
        #print(self.__x)
        
        # on bouge l'enemy
        self.__canvas.coords(self.mechant, self.__x+20, self.__y+20, self.__x+40, self.__y+40)
        #print("déplacement")
        self.__canvas.after(1, self.move)
        
    def vie(self, degats):
        self.__vie += degats