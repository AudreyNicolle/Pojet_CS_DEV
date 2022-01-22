# -*- coding: utf-8 -*-
"""
Created on Sun Jan  2 21:05:15 2022
@author: emma.begard & audrey.nicolle

Ce fichier contient la classe Projectile qui permet de gérer les projeciles et 
sa classe fille Projectile_secret.
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
        
        self.x = x
        self.y = y
        self.vel = 10
        self.canvas = canvas
        self.image = Image.open(chemin_image)
        self.redi_image = ImageTk.PhotoImage(self.image.resize((50,50))) 
        self.projectile = self.canvas.create_image(self.x,self.y, \
                                                     image = self.redi_image)
        self.height = 10
        self.width = 10
        self.dir = direction
        self.degats = -1
        self.vie = 1
        self.type = 0

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
        if self.y >= 1 and self.vie >= 1: 
            self.y += self.dir*self.vel
            self.canvas.move(self.projectile, 0, self.dir*self.vel)
            self.canvas.after(50, self.run, lst_projectiles)
        
        #sinon on le supprime du canvas et de la liste de projectiles
        else :
            self.canvas.delete(self.projectile)
            lst_projectiles.remove(self)


#•-----------------------------------------------------------------------------

class Projectile_secret(Projectile) :
    """ 
    Cette classe permet de créer les projectile secret du mechant bonus. Elle
    hérite de la classe Projectile.
    """
     
    def modif_caracteristiques(self) :
        """        
        Cette fonction permet de modifer quelques caractérisqtiques du 
        projectile.
    
        Parameters : none 
    
        Returns : none 
        """
    
        self.height = 15
        self.width = 15 
        self.vel = 15 
        self.type = 1
        self.image = Image.open("Image/mauvaise_note.jpg")
        self.redi_image = ImageTk.PhotoImage(self.image.resize((40,40))) 
        self.projectile = self.canvas.create_image(self.x,self.y, \
                                                     image = self.redi_image)
 
#•-----------------------------------------------------------------------------

#class Projectile


