# -*- coding: utf-8 -*-
"""
Created on Tue Dec 21 21:17:22 2021
@author: emma.begard & audrey.nicolle

Ce fichier contient les classes, la classe mère méchant et la classe fille M_bonus
qui permmettent de gérer les actions internes des mechants du jeu.

"""
#Import -----------------------------------------------------------------------
from PIL import Image, ImageTk
import projectile 

#Classe------------------------------------------------------------------------

class Mechant :
    
    def __init__(self, window,canvas,x,y):
        """ 
        Cette classe permet de générer des méchants et de gérer leurs actions 
        propres. 
        
        Parameters :
                window : la fenetre du jeu (tk)
                canvas : la zone de jeu où s'affiche le méchant
                self.x : position sur l'axe des abscices (int)
                self.y : position sur l'axe des ordonnées (int)
                self.image : image du méchant
                self.redi_image : image du méchant redimensionnée
                self.mechant : canvas image du mechant (objet canvas)
                self.dir : direction du méchant (int 1 ou -1)
                self.vel = vélocité du mechant (int)
                
        Returns : None                
        """
        self.window = window
        self.canvas = canvas
        self.x= x
        self.y = y
        self.image = Image.open("Image/sorcier.png")
        self.redi_image = ImageTk.PhotoImage(self.image.resize((70,70))) 
        self.mechant = self.canvas.create_image(self.x,self.y, image = self.redi_image )
        self.dir = 1
        self.vel = self.dir*0.1
        self.lst_projectile = []
        self.vie = 1
        
        
    def move(self,dy): 
        """
        Cette fonction permet de déplacaer horizontalement le méchant vers la 
        gauche ou la droite selon son indice de direction self.dir.
        
        Parameters : dy => deplcement verticale (int)

        Returns : None
        """
        
        # on bouge l'enemy
        #move(entité,x,y)
        self.canvas.move(self.mechant,self.vel*self.dir,dy)
        #récupère la position 
        self.x = self.canvas.bbox(self.mechant)[0]
        self.y = self.canvas.bbox(self.mechant)[1]

        
    def tir (self,on_tir) :
        """ 
        Cette fonction permet de tirer des boules de feu. 
        
        Parameters : on_tir => permet d'avoir une probalité de tir correcte par
                            rapport au nombre de fois que la fonction est appelé
                            (int)
        Returns : none
        """
        
        if on_tir == 2 :
            
            boule_de_feu = projectile.Projectile(self.x+2,self.y+2,self.canvas,\
                                             "Image/boule_de_feu.png", 1)
            self.lst_projectile.append(boule_de_feu)
            self.lst_projectile[-1].run(self.lst_projectile)
      
    def perd_vie(self, degats):
        self.vie += degats

        
        
        
        
        
