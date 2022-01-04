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
        self.window = tk.Toplevel()
        self.mechant= 0
        self.canvas = tk.Canvas(self.window, bg='black')
        self.player = pl.player( self.window, self.canvas)
        self.enemy = []        
        
        
        
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
        
        """move = tk.Button(self.window, text ='move')
        move.bind('<Right>', self.player.right)
        move.grid(column=20, row=10)
        move.focus()"""
        
        # resizeable playing area
        can_width =self.window.winfo_screenwidth()
        can_height = self.window.winfo_screenheight()
        self.canvas.config(width=can_width, height=can_height)
        self.canvas.grid(column=0, row=2, rowspan = 19, columnspan=19)
        
        # tout les truc interactifs  
        self.mechant = mechant.mechant(self.window, self.canvas, 400,200)
        
        self.enemy.append(self.mechant)
        
        
     
    
    def collisions(self):
        """ cette fonction détecte les collisions entre le joueur et les enmis"""
        for enemi in self.enemy:
            pass
        
    def main(self):
        
        """ the fonction running the whole project """
        self.window.geometry( "{}x{}".format(self.width, self.height) )
        self.principale()
        self.mechant.move()
        self.player.tout()  


        self.window.mainloop()
        
  
        

ecran= class_window(1000,800)
#ecran.structure_fenetre()

ecran.main()