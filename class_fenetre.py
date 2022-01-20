#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 13 14:42:01 2021
@author: emma.begard & audrey.nicolle

Ce fichier contient la classe qui s'occupe de la gestion de la fenêtre du jeu et des actions de celui-ci.

To-do : - régler problème vie 
        - faire le mechant bonus
        - pour le score (stringVar et set)
"""
#Import -----------------------------------------------------------------------

import tkinter as tk
import player as pl
import mechant as mechant
from random import randint
from PIL import Image, ImageTk


#Classe -----------------------------------------------------------------------

class class_window :
    
    def __init__(self, width, height):
        """ 
        Cette classe permet de générer le fenêtre de jeu, la zone de jeu canvas et
        de gérer les actions entres les différentes entités du jeu.
        
        Parameters : 
                    self.window : fenêtre du jeu (objet Tk)
                    self.canvas : zone de jeu (objet tk)
                    self.player : joueur (objet canvas) 
                    self.ennemy : contient les objets mechant (list)
        Returns : none
        """  
        self.width = width
        self.height = height
        self.window = tk.Toplevel()
        self.mechant= 0
        self.canvas = tk.Canvas(self.window, bg='black')
        self.player = pl.Player( self.window, self.canvas)
        self.enemy = []                   
        self.game = True
        
        
    def principale(self):
        
        """ 
        Cette fonction permet de créer la fenêtre et de gérer les 
        interractions du jeu.
        Paramaters : none 
        Returns : none 
        """
        # creaton d'une grille de 20 lignes et colonnes 
        for i in range(20):
            self.window.grid_rowconfigure(i, weight=2)
            self.window.grid_columnconfigure(i, weight=2)
        
        # on change le poids de score 
        score = tk.Label(self.window, width =3, height = 3 , text='score')  
        score.grid(row = 0, column = 0, sticky="nsew")
        
        # on crée un bouton de sortie
        button_quit = tk.Button(self.window, text='quit', command=self.window.destroy)
        button_quit.grid(row = 20, column = 20)
        
 
        
        # resizeable playing area
        can_width =self.window.winfo_screenwidth()
        can_height = self.window.winfo_screenheight()
        self.canvas.config(width=can_width, height=can_height)
        self.canvas.grid(column=0, row=2, rowspan = 19)
        
        # tout les truc interactifs 
        self.crea_mechant()
        self.move_groupe()
        self.player.crea_vie()
        self.player.tout()
        self.gestion_Pgentil_VS_Pmechant()
        #self.gestion_collisions()  
        
    def gestion_collisions(self):
        """cette fonction détecte les collisions entre le joueur et les enmis"""
   
        for lst_bad_guy in self.enemy :
            if lst_bad_guy == []:
                self.enemy.remove(lst_bad_guy)
            else :
                for bad_guy in lst_bad_guy :
                    
                    
                    
                    # on test si le méchant a encore de la vie
                    if bad_guy.vie == 1:
                        
                        # juste au cas ou ou on veiole pouvoir tirer plusieurs projectiles 
                        for projectile in self.player.projectiles :
                            projectile.collision(bad_guy.mechant)
                            
                        for projectile in bad_guy.lst_projectile :
                            projectile.collision(self.player.yeti)
                    
                    else :
                        # on enlève le méchant de la liste des enemys, car il est mort
                        lst_bad_guy.remove(bad_guy)
                        # on n'affiche plus le méchant
                        self.canvas.delete(bad_guy.mechant)
                
        self.canvas.after(1, self.gestion_collisions)    
    def gestion_Pgentil_VS_Pmechant (self):
        
        for lst_bad_guy in self.enemy :
            
            if lst_bad_guy == []:
                self.enemy.remove(lst_bad_guy)
            else :
                for bad_guy in lst_bad_guy :

                    # on test si le méchant a encore de la vie
                    if bad_guy.vie == 1:
                        
                        # juste au cas ou ou on veiole pouvoir tirer plusieurs projectiles 
                        for projectile in self.player.projectiles :
                            if self.collision(projectile.projectile,bad_guy.mechant) :
                                projectile.vie -= 1
                                bad_guy.perd_vie(-1)
                        
                        for projectile in bad_guy.lst_projectile :
                            if self.collision(projectile.projectile, self.player.yeti) :
                                projectile.vie -= 1
                                print('here')
                                self.player.gestion_vie(-1)
                        
                    
                    else :
                        # on enlève le méchant de la liste des enemys, car il est mort
                        lst_bad_guy.remove(bad_guy)
                        # on n'affiche plus le méchant
                        self.canvas.delete(bad_guy.mechant)
                
        self.canvas.after(1, self.gestion_Pgentil_VS_Pmechant)
        
        
    def collision(self,entite1, entite2):
        
        x_1 = self.canvas.bbox(entite1)[0] 
        x_2 = self.canvas.bbox(entite1)[2] 
        y_1 = self.canvas.bbox(entite1)[1] 
        y_2 = self.canvas.bbox(entite1)[3] 
        #print(self.canvas.find_overlapping(x_1, y_1, x_2, y_2) )
             
        # les coordonnées de notre enemy
        coords = self.canvas.bbox(entite2)
            
        if (x_2 > coords[0]> x_1) and (y_1 < coords[1]< y_2):
            #print('collision  geuche !')
            return True
                
        elif (x_2 > coords[2]> x_1) and (y_1 < coords[3]< y_2):
            #print('collision  droite !')
            return True   
        
    def move_groupe (self) :
        """ 
        Permet de faire bouger horizontalement le bloc de mechant et de 
        descendre ce bloc lorsque un des sorciers d'une ligne de bloc touche 
        le cadre.
        
        Parameters : none
        
        Returns : none 
        """
        
        for sous_lst in self.enemy :
            if sous_lst != [] :
                
            
                # vérifie que les sorciers des extrémités du bloc ne touche pas le bord
                if sous_lst[-1].x > 900 : 
                    for bad_guy in sous_lst :
                        bad_guy.dir = -1 #on change la direction
                        bad_guy.move(15) #on les faits bouger horizontalement en descendant
                    
            
                elif sous_lst[0].x < 2 : 
                    for bad_guy in sous_lst :
                        bad_guy.dir = 1
                        bad_guy.move(15)
                    
           
                #sinon on ne fait que de les bouger horizontalement        
                else : 
                    for bad_guy in sous_lst :
                        bad_guy.move(0)
                        bad_guy.tir(randint(1,10000)) #permet de les faire tirer avec une chance sur 10 000, cf fontion tir
                    
        #rappelle de la fonction pour un mouvement continu            
        self.canvas.after(1, self.move_groupe) 
                
                
    def crea_mechant (self) : 
        """ 
        Cette fonction permet de créer une matrice de méchant.
        Parameters : none
        Rteurns : none
        """
        
        #Initialisation 
        i = 0 
        y = 20
        while i < 3 :
            
            y += 100 #changement de la poition verticale pour chaque sous liste
            #Initialisation
            j = 0 
            sous_lst_enemy = [] #initialisation sous liste
            x = 50 
            
            while j < 11 : 
                    x += 70 #changement de la poition horizontale pour chaque mechant
                    bad_guy = mechant.Mechant(self.window,self.canvas,x,y) 
                    sous_lst_enemy.append(bad_guy)
                    j += 1
                    
            self.enemy.append(sous_lst_enemy)
            i += 1 
        
        
     
        
    def main (self):
        
        """ the fonction running the whole project """
        self.window.geometry( "{}x{}".format(self.width, self.height) )
        self.principale() 
        self.window.mainloop()


#Main -------------------------------------------------------------------------
#Note : à mettre dans un autre fichier --> fichier main       

ecran= class_window(1000,800)
#ecran.structure_fenetre()

ecran.main()
