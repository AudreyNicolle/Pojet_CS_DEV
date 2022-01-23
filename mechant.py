# -*- coding: utf-8 -*-
"""
Created on Tue Dec 21 21:17:22 2021
@author: emma.begard & audrey.nicolle

Ce fichier contient les classes, la classe mère méchant et la classe fille NICOLLE
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
                self.arme_secrete : permet de savoir si l'arme secrete du mechant
                                    bonus est active.
                self.points : permet de savoir combien de point rapporte le 
                                mechant
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
        self.arme_secrete = 0
        self.points = 1
        
        
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
                                             "Image/boule_de_feu.png", 1, 0)
            self.lst_projectile.append(boule_de_feu)
            self.lst_projectile[-1].run(self.lst_projectile)
      
    def perd_vie(self, degats):
        self.vie += degats

#•-----------------------------------------------------------------------------

class NICOLLE (Mechant) :
    """
    Cette classe est celle qui permet de créer et de gérer le méchant bonus.Elle
    hérite de la classe mechant.
    """
    
    def modif_caracteristique (self) :
        """
        Cette fonction permet de modifier les caractéristiques du mechant bonus
        soit son image et sa vitesse de déplacement.
        
        Parameters : none.

        Returns : None.
        """
        
        self.image = Image.open("Image/papa_gentil.png")
        self.redi_image = ImageTk.PhotoImage(self.image.resize((80,80))) 
        self.mechant = self.canvas.create_image(self.x,self.y, image = self.redi_image )
        self.vel = self.dir*3
        self.vie = 2
        
    def into_mechant (self) :
        """ 
        Cette fonction modifié l'image du mechant bonus et d'activer le tir 
        secret.
        
        Parameters : none 
        
        Returns : none 
        """

        self.image = Image.open("Image/papa_mechant.jpg")
        self.redi_image = ImageTk.PhotoImage(self.image.resize((80,80))) 
        self.mechant = self.canvas.create_image(self.x,60, image = self.redi_image)
        
        self.arme_secrete = 1
        
    def tir_secret (self, on_tir) :
        """
        Cette fonction permet de tirer les tir secret du mechant bonus. 
        
        Parameters : 
            on_tir : permet de créer de l'aléatoire. (int)
            
        Retruns : none.
        """
    
        if on_tir == 2 :
            
            mauvaise_note = projectile.Projectile_secret(self.x+2,self.y+2,self.canvas,\
                                             "Image/mauvaise_note.jpg", 1,1)
            mauvaise_note.modif_caracteristiques()
            
            
            self.lst_projectile.append(mauvaise_note)
            self.lst_projectile[-1].run(self.lst_projectile)
         
    