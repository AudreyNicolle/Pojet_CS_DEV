#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 13 14:42:01 2021

@author: emma.begard
"""
import tkinter as tk
import player as pl
import mechant as mechant



class class_window :
    
    def __init__(self, width, height):
        
     
        self.width = width
        self.height = height
        self.window = tk.Tk()
        self.mechant= 0
        self.canvas = tk.Canvas(self.window, bg='black')
        self.player = pl.player( self.window, self.canvas)
        self.enemys = []  
        self.game = True
        
        
        
    def principale(self):
        
        """ creation de la grille de la fenêtre """
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
        self.mechant = mechant.mechant(self.window, self.canvas, 400,200)
        self.enemys.append(self.mechant)
        
        
     

    def collisions(self):
        """cette fonction détecte les collisions entre le joueur et les enmis"""
   
        for enemy in self.enemys :
            # on test si le méchant a encore de la vie
            if enemy.vie < 1:
                # on n'affiche plus le méchant
                self.canvas.delete(enemy.mechant)
                # on enlève le méchant de la liste des enemys, car il est mort
                self.enemys.remove(enemy)
            
            # juste au cas ou ou on veiole pouvoir tirer plusieurs projectiles 
            for projectile in self.player.projectiles :
                projectile.collision(enemy )
                
        self.canvas.after(1, self.collisions)
 
    def mechant_move(self):
        
        for  enemy in self.enemys :
            print("etat enemy ",enemy.move)
            # si le méchant n'as plu de points de vie
            if enemy.move == False :
                # on enlève le méchant de la liste des enemys, il n'existe plus 
                self.enemys.pop(enemy)
        
    def main (self):
        
        """ the fonction running the whole project """
        self.window.geometry( "{}x{}".format(self.width, self.height) )
        self.principale()
        self.mechant.move()
        self.player.tout(self.enemys)
        self.collisions()     
        self.window.mainloop()

        
""" partie test """
        

ecran= class_window(1000,800)
#ecran.structure_fenetre()

ecran.main()
