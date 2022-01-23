# -*- coding: utf-8 -*-
"""
Created on Fri Jan 21 15:22:54 2022

@author: emma.begard & audrey.nicolle

Ce fichier contient 
"""

class Ilot () :
    
    def __init__(self,window,canvas,x,y) :
        
        """
        Cette classe permet de créer un îlot composé de plusieur petit bloc.
        
        self.lst_carre : contient les lignes des petits blocs
        self.x : position du coin gauche du bloc selon l'axe des abscices
        self.y : position du coin gauche du bloc selon l'axe des ordonnées
        self.canvas : zone du jeu (objet canvas)
        self.window : fenêtre du jeu (objet tkinter)
        """
        
        self.lst_carre = []
        self.x = x
        self.y = y
        self.canvas = canvas
        self.window = window
        
    def crea_ilot (self) : 
        
        """ 
        Cette fonction permet de créer une matrice de bloc de l'îlot.
        
        Parameters : none
        
        Returns : none
        """
        
        #Initialisation 
        i = 0 
        y = self.y
        while i < 3 :
            
            
            #Initialisation
            j = 0 
            sous_lst_ilot= [] 
            x = self.x
            
            while j < 5 : 
                    x += 10 #changement de la poition horizontale pour chaque mechant
                    bloc = self.canvas.create_rectangle(x,y,x+50,y+50,width=0,fill = "blue") 
                    sous_lst_ilot.append(bloc)
                    j += 1
                 
            self.lst_carre.append(sous_lst_ilot)
            i += 1 
            y += 10 #changement de la poition verticale pour la prochaine sous
            #liste
        