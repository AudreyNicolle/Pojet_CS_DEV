# -*- coding: utf-8 -*-
"""
Created on Sun Jan  2 21:05:15 2022
@author: emma.begard & audrey.nicolle

Ce fichier contient la classe Projectile qui permet de gérer les projeciles.
"""

#Import -----------------------------------------------------------------------

from PIL import Image, ImageTk

#Classe -----------------------------------------------------------------------

class Projectile:

    def __init__(self, x, y, canvas, chemin_image, direction):
        """ 
        Cette classe s'occupe de gérer les projectiles du jeu.
        
        Parameters : 
            self.__x : position selon l'axe des abscisses (int)
            self.__y : position selon l'axe des ordonées (int)
            self.vel : vélocité des projectiles (int)
            self.__canvas : zone de jeu ( objet canvas)
            self.image : image du projectile (objet canvas)
            self.height : 
            self.width : 
            self.dir : direction du projectile (int)
            self.degats : 
            self.vie :
        """
        
        self.__x = x
        self.__y = y
        self.vel = 10
        self.__canvas = canvas
        self.image = Image.open(chemin_image)
        self.redi_image = ImageTk.PhotoImage(self.image.resize((50,50))) 
        self.projectile = self.__canvas.create_image(self.__x,self.__y, image = self.redi_image)
        self.height = 10
        self.width = 10
        self.dir = direction
        self.degats = -1
        self.vie = 1

    def run(self, lst_projectiles):
        """ 
        Déplacement du projectile jusqu'en haut de l'écran et l'éfface
        (visuel et liste projectile dans player) une fois sortit de l'écran
        
        Parameters :
            lst_projectile : la liste de player conenant tt les projectiles 
                            lancés(lst)
        Returns : none
            """
        
        #on vérifie que le missile est tjs dans l'écran et tjs existant
        if self.__y >= 1 and self.vie >= 1: 
            self.__y += self.dir*self.vel
            self.__canvas.move(self.projectile, 0, self.dir*self.vel)
            self.__canvas.after(50, self.run, lst_projectiles)
        
        #sinon on le supprime du canvas et de la liste de projectiles
        else :
            
            self.__canvas.delete(self.projectile)
            del lst_projectiles[0]

    def collision(self, objet):
         #gère les dégats donnés et reçus ( le missile enlève autant de points de vie qu'il fait de dégats et en perds autant) 
        

        #les x, y min et max de l'objet encollision(?) sur l'écran

        x_1, y_1, x_2, y_2 = self.__canvas.bbox(self.projectile)

        
        # le coin gauche de l'objet est dans la zone des x du projectile 
        #if  self.__x >= x_1  and x_1<= (self.__x+self.width):
