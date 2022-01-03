# -*- coding: utf-8 -*-
"""
Created on Sat Jan  1 20:43:01 2022

@author: emma1
"""
import projectile as pj

class player :
    
    def __init__(self,window, canvas):
        
        self.__x = 400
        self.__y = 600
        self.vel = 10
        self.canvas = canvas
        self.window = window
        self.__image = canvas.create_rectangle( self.__x+20, self.__y+20, self.__x+40, self.__y+40, fill='blue')
        self.projectiles = []
        
        
    def move_right(self, evt):
        """ déplacement à droite """
        self.__x += self.vel
        self.canvas.coords(self.__image, self.__x+20, self.__y+20, self.__x+40, self.__y+40)
        
    def move_left(self, evt):
        """ déplacement à gauche """
        self.__x += -self.vel
        self.canvas.coords(self.__image, self.__x+20, self.__y+20, self.__x+40, self.__y+40)
        
    def crea_projectile (self, event):
        """ création d'un projectile, objet de classe projectile """
        print("création projectile")
        if len ( self.projectiles) > 0:
            self.canvas.delete(self.projectiles[0].image)
            del self.projectiles[0]
            
        else :
            self.projectiles.append( pj.projectile(self.__x, self.__y, self.canvas) )
        print('fin creation ')
        
    def key_event(self):
        """ gère les actions de clavier : déplacement à droite et gauche, tir """
        self.window.bind('<Right>', self.move_right)
        self.window.bind('<Left>', self.move_left)
        self.window.bind('<space>', self.crea_projectile)
        

    def tir(self):
        """ déplace les projectiles et vérifie qu'ils ne soient pas sortis de lécran, sinon on les supprimes"""
        print("on est dans le tir du joueur")
        print(len(self.projectiles) )
        
        for projectile in self.projectiles :
            print("dans la liste des projectiles", self.projectiles.index(projectile) )
            sortie = projectile.run()
            print("run projectile")
            
            # le projectile va sortir de l'écran, on le supprime
            if sortie :
                self.projectiles.remove(projectile)
                print("le projectile",self.projectiles.index(projectile)," est sortit")
                return 0
    
    def tout(self):
        
        self.key_event()
        self.tir()
        print("fin player.main()")
      