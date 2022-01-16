# -*- coding: utf-8 -*-
"""
Created on Sat Jan  1 20:43:01 2022
@author: emma.begard & audery.nicolle
"""
#Import -----------------------------------------------------------------------

import projectile as pj
from PIL import Image, ImageTk

#Classe -----------------------------------------------------------------------

class Player :
    
    def __init__(self,window, canvas):
        """ 
        Cette claasse permet de gérer les actions propres du joueur.
        
        Parameters : 
            window : la fenetre du jeu (tk)
            canvas : la zone de jeu où s'affiche le méchant
            self.__x : position sur l'axe des abscices (int)
            self.__y : position sur l'axe des ordonnées (int)
            self.vel : vélocité du joueur (int)
            self.image : image du joueur (objet canvas)
            self.projectiles : contient tous les projectiles tirer par le joueur
                                (lst)
        """
        self.__x = 400
        self.__y = 600
        self.vel = 10
        self.__canvas = canvas
        self.window = window
        self.image = Image.open("Image/yeti.png")
        self.redi_image = ImageTk.PhotoImage(self.image.resize((70,70))) 
        self.yeti = self.__canvas.create_image(self.__x,self.__y, image = self.redi_image )
        self.projectiles = []
        self.nb_vie = []
   
    def move_right(self, evt):
        """ 
        Cette fonction permet de déplacer le joeur à droite.
        
        Parameters : 
            evt : variable utilisé dans la fonction key_event => window.bind (str)
            
        Returns : none
        """
        if self.__x < 950 :
            self.__x += self.vel
            self.__canvas.move(self.yeti, self.vel, 0)
        
    def move_left(self, evt):
        """ 
        Cette fonction permet de déplacer le joeur à gauche.
        
        Parameters : 
            evt : variable utilisé dans la fonction key_event => window.bind (str)
            
        Returns : none
        """
        if self.__x  > 50 :
            self.__x += -self.vel
            self.__canvas.move(self.yeti, -self.vel, 0)
        
    def crea_projectile (self, evt):
        """ 
        Cette fonction permet de créer un projectile que lorsque le projectile 
        précédent n'existe plus.
        
        Parameters : 
            evt : variable utilisé dans la fonction key_event => window.bind (str)
            
        Returns : none
        """
        # comme on ne peut avoir que 1 projectile à l'écran 
        if len(self.projectiles) <= 0:
            self.projectiles.append( pj.Projectile(self.__x, self.__y, self.__canvas,"Image/rocher.png", -1) )
            self.projectiles[-1].run(self.projectiles)
           

    def key_event(self):
        """
        Cette fonction permet de gérer les actions de clavier : déplacement à 
        droite et gauche, tir.
        
        Parameters : none
        
        Returns : none 
        """
        #self.window.bind('evenement', fonction à appliquer si l'évènement arrive)
        self.window.bind('<Right>', self.move_right)
        self.window.bind('<Left>', self.move_left)
        self.window.bind('<space>', self.crea_projectile)
        self.__canvas.focus_set()
    
    def crea_vie (self) : 
        i = 0
        x = 600
        y = 600
        print('here')
        while i < 3 : 
            print('here'+ str(i)) 
            
            im_coeur = Image.open("Image/coeur.png")
            redi_image = ImageTk.PhotoImage(im_coeur.resize((50,50))) 
            vie = self.__canvas.create_image(x,y, image = redi_image )
            self.__canvas.image = im_coeur
            self.nb_vie.append(vie)
            i += 1
            x += 70
        
            
    
    def tout(self):
        
        self.key_event()