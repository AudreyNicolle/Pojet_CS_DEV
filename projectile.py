# -*- coding: utf-8 -*-
"""
Created on Sun Jan  2 21:05:15 2022
@author: emma.begard & audrey.nicolle

Ce fichier contient la classe Projectile qui permet de gérer les projeciles et 
sa classe fille Projectile_secret.
"""

#Import -----------------------------------------------------------------------

from PIL import Image, ImageTk
import time

#Classe -----------------------------------------------------------------------

class Projectile:

    def __init__(self, x, y, canvas, chemin_image, direction, genre):
        """ 
        Cette classe s'occupe de gérer les actions propres aux projectiles du 
        jeu soit : 
                - de les faire avancer vers le bas.
                - de gérer leur vie.
                
        
        Parameters : 
            self.__x : position selon l'axe des abscisses (int)
            self.__y : position selon l'axe des ordonées (int)
            self.vel : vélocité des projectiles (int)
            self.canvas : zone de jeu ( objet canvas)
            self.image : image du projectile (objet canvas)
            self.projectile : image du projectile (objet canvas)
            self.dir : direction du projectile (int)
            self.degats : degats cuasés (int)
            self.vie : vie du projectile (int)
            self.temps : date de création du projectile (int)
        """
        
        self.x = x
        self.y = y
        self.vel = 10
        self.canvas = canvas
        self.image = Image.open(chemin_image)
        self.redi_image = ImageTk.PhotoImage(self.image.resize((40,40))) 
        self.projectile = self.canvas.create_image(self.x,self.y, \
                                                     image = self.redi_image)
        self.dir = direction
        self.degats = -1
        self.vie = 1
        self.type = genre
        self.temps = time.time_ns()

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
    hérite de la classe Projectile. Elle permet de modifier les caractéristiques 
    nécessaires.
    """
     
    def modif_caracteristiques(self) :
        """        
        Cette fonction permet de modifer quelques caractérisqtiques du 
        projectile.
    
        Parameters : none 
    
        Returns : none 
        """
        self.vel = 15 
        self.image = Image.open("Image/mauvaise_note.jpg")
        self.redi_image = ImageTk.PhotoImage(self.image.resize((40,40))) 
        self.projectile = self.canvas.create_image(self.x,self.y, \
                                                     image = self.redi_image)
 
#•-----------------------------------------------------------------------------

class Bonus(Projectile) :
    """
    Cette classe permet de créer des tartiflettes ou des thermos. Les 
    tartiflettes redonnent de la vie au joueur. Les thermos lui offre une 
    résistance au boule_de_feu jusqu'à ce qu'une boule le touche.
    """
    
    def modif_caractéritique(self) : 
        """        
        Cette fonction permet de modifer quelques caractérisqtiques du 
        projectile.
    
        Parameters : none.
    
        Returns : none.
        """
        self.vel = 8

    def run(self, lst_projectile) :  
        """
        Cette fonction permet de faire avancer les bonus sans passer en 
        dessous du yéti et selon une parabole.

        Parameters :
            lst_projectile : contient les bonus (lst)

        Returns : None.
        """
        
        #on regarde si c'est une tartiflette qui vient de la gauche ou de la 
        #droite
        if self.type[0] == '2' :
            x = 1
        else : 
            x = -1
            
        #on vérifie que le missile est tjs existant
        if self.vie >= 1 :
            
            #♥on vérifie qu'il ne va pas sous le yéti
            if self.y <= 600 :
        
                self.y += self.dir*self.vel
                self.canvas.move(self.projectile, x*self.vel, self.dir*self.vel)
        
        #sinon on le supprime du canvas et de la liste de projectiles
        else :
            self.canvas.delete(self.projectile)
            lst_projectile.remove(self)

    


