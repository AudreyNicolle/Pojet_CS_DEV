#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 13 14:42:01 2021
@author: emma.begard & audrey.nicolle
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
        im_coeur = Image.open("Image/coeur.png")
        redi_image = ImageTk.PhotoImage(im_coeur.resize((50,50))) 
        self.canvas.create_image(400,500, image = redi_image )
        self.canvas.image = im_coeur
        self.crea_mechant()
        self.move_groupe()
        self.player.crea_vie()
        self.affichage_vie()
        self.player.tout()
        self.collisions()  

    def collisions(self):
        #cette fonction détecte les collisions entre le joueur et les ennemis
        #print("test  ")
        #for enemy in self.enemy:
        # au cas ou on veut modifier les prinsipes du jeu et tirer plusieurs projectiles
        for projectile in self.player.projectiles :
            projectile.collision(self.enemy[0])
        self.canvas.after(1, self.collisions)
    
    def affichage_vie (self) : 
        for vie in self.player.nb_vie :
            vie
        self.canvas.after(10,self.affichage_vie)
        
    def move_groupe (self) :
        """ 
        Permet de faire bouger horizontalement le bloc de mechant et de 
        descendre ce bloc lorsque un des sorciers d'une ligne de bloc touche 
        le cadre.
        
        Parameters : none
        
        Returns : none 
        """
        
        for sous_lst in self.enemy : 
            
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
        while i < 4 :
            
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
    #def affichage_vie (self) : 
        
       
        
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
