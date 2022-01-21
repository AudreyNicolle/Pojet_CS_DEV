#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 13 14:42:01 2021
@author: emma.begard & audrey.nicolle
Ce fichier contient la classe qui s'occupe de la gestion de la fenêtre du jeu et des actions de celui-ci.
To-do : - faire collions projectileG projectile mechant, aussi chnager la sensibilité de la collion
            et regarder cette erreur qui arrive une fois sur 4 : 
                x_1 = self.canvas.bbox(entite1)[0]
            TypeError: 'NoneType' object is not subscriptable
        - faire le mechant bonus
        - pour le score (stringVar et set)
"""
#Import -----------------------------------------------------------------------

import tkinter as tk
import player as pl
import mechant as mechant
from random import randint


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
                    self.score  : le score du joueur
                    self.display_score : lme texte dans le label score de la fenêtre d'affichage
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
        self.score = 0
        self.display_score = tk.StringVar()
        self.background = tk.PhotoImage(file='Image/fond.png')
      
    def about(self):
        """ cette fonction ouvre un fichier texte qui décrit le fonctionnement du jeu """
        print("on veut ouvrir le menu d'explications" )
        # la chaîne de caractères avec la description du jeu et tt
        text =''
        # on lit notre petit fichier de description du jeu
        with open ('a_propos.txt','r', encoding="utf8") as des:
            for line in des :
                print(line)
                text += str(line)
        tk.messagebox.showinfo('A propos', text)
        #self.window.showinfo(title='A propos', massage= text)
        
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
        
        self.update_score()
        # la zone d'affichage du score
        score = tk.Label(self.window, width =3, height = 3 , textvariable = self.display_score )  
        score.grid(row = 0, column = 0, sticky="nsew")
        
        # création du menu
        menubar = tk.Menu(self.window)
        self.window.config(menu=menubar)
        menufichier = tk.Menu(menubar,tearoff=0)
        menubar.add_cascade(label="Options", menu=menufichier)
        menufichier.add_command(label="à propos ", command=self.about)
    
        
        # on créer un bouton pour lancer une partie
        play = tk.Button(self.window, text='partie', command= self.launch_game )
        play.grid(row = 10, column =20)
        
        # on crée un bouton de sortie
        button_quit = tk.Button(self.window, text='quit', command=self.window.destroy)
        button_quit.grid(row = 20, column = 20)

        # resizeable playing area
        can_width =self.window.winfo_screenwidth()
        can_height = self.window.winfo_screenheight()
        self.canvas.config(width=can_width, height=can_height)
        self.canvas.grid(column=0, row=2, rowspan = 19)
        
        self.canvas.create_image(10, 0, image=self.background,  anchor = "nw")
        
        
    def gestion_fin_de_vie_EHPHAD (self) :
        
        """
        Cette fonction permet de supprimer tous les éléments canvas quand le 
        joeur a perdu.
        
        Parameters : none
        
        Returns : none
        """
        
        if self.player.nb_vie == [] :
            self.canvas.delete("all")   
            self.ennemy = []
            
        self.canvas.after(50, self.gestion_fin_de_vie_EHPHAD)    
        
            
        
    def gestion_collsions(self):
        """
        Cette fonction permet de vérifier si les ennemis entre en collision avec 
        un projectile du joueur. Si c'est le cas les deux disparaissent. 
        Elle permet aussi de vérifier si les ennemis rentrent en collision avec
        le joueur. Si c'est le cas le cas le joueur perd toutes ses vies.
        Ensuite elle permet de vérifier si'il y a une collision entre un projectile
        d'un méchant et le joueur. Si c'est le cas, le joeur perd une vie et le 
        tir disparaît.
        Enfin elle permet de savoir si deux projectiles se collisionnent. Si 
        c'est le cas les deux disparaissent.
        
        Parameters : none.
        
        Returns : none.
        """
        #On va regarder toutes les collisions qui mettent en jeu les ennemis. 
        for lst_bad_guy in self.enemy :
            
            #On vérifie que la rangée de méchant en contient toujours au moins 
            #un
            if lst_bad_guy == []:
                self.enemy.remove(lst_bad_guy)
           
            else :
                
                for bad_guy in lst_bad_guy :

                    # on test si le méchant a encore de la vie
                    if bad_guy.vie == 1:
                        
                        #on gère les collisions projectile gentil vs méchant 
                        for projectile in self.player.projectiles :
                            # si il y a collision 
                            if self.collision(projectile.projectile,bad_guy.mechant) :
                                projectile.vie -= 1
                                bad_guy.perd_vie(-1)
                                # on ajopute les points que rapporte l emontre
                                self.score += bad_guy.points
                                print(self.score)
                                
                        #on gère les collisions projectile méchant vs joueur
                        for projectile in bad_guy.lst_projectile :
                            if self.collision(projectile.projectile, self.player.yeti) :
                                projectile.vie -= 1
                                self.player.gestion_vie(-1)
                                # on perds des points sur notre score, autant que le monstre rapporterais
                                self.score -= bad_guy.points
                                print(self.score)
                        
                        #on gère les collisions joeur vs méchant
                        if self.collision(bad_guy.mechant, self.player.yeti) :
                           # print('here')
                            bad_guy.perd_vie(-1)
                            while self.player.nb_vie >= 1 :
                                self.player.gestion_vie(-1)
                                # on perds du score, 2 fois plus que le monstre rapporte
                                self.score -= 2*bad_guy.points
                                print(self.score)
                    
                    else :
                        # on enlève le méchant de la liste des enemys, car il est mort
                        lst_bad_guy.remove(bad_guy)
                        # on n'affiche plus le méchant
                        self.canvas.delete(bad_guy.mechant)
                        print(self.score)
                
        #on et un temps de rappel de la fonction de 50ms car en-dessous lorsqu'on
        #rappelle la fonction la collision n'est pas fini et cela fausse le reste
        #du programme
        self.canvas.after(50, self.gestion_collsions)
        
        
    def collision(self,entite1, entite2):
        """ 
        Cette fonction permet de voir si deux objets rentrent en collisions.
        
        Parameters : 
            - entite1 : premier objet concerné par la collision (objet canvas) 
            - entite1 : deuxième objet ci=oncerné par la collision (objet canvas) 
            
        Returns : on retourne un booléen. Vrai s'il y a eu collision.
        """
       
        #On récupère les coordonées de l'objet 1
        x_1 = self.canvas.bbox(entite1)[0] 
        x_2 = self.canvas.bbox(entite1)[2] 
        y_1 = self.canvas.bbox(entite1)[1] 
        y_2 = self.canvas.bbox(entite1)[3] 
        
        
        # les coordonnées de la deuxième entité
        coords = self.canvas.bbox(entite2)
         
        #On vérifie s'i y a une collison par la gauche de l'entité 1 sur l'entité 2
        if (x_2 > coords[0]> x_1) and (y_1 < coords[1]< y_2):
            return True
        
        #On vérifie s'i y a une collison par la droite de l'entité 1 sur l'entité 2       
        elif (x_2 > coords[2]> x_1) and (y_1 < coords[3]< y_2):
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
        y = 50
        while i < 3 :
            
            y += 60 #changement de la poition verticale pour chaque sous liste
            #Initialisation
            j = 0 
            sous_lst_enemy = [] #initialisation sous liste
            x = 50 
            
            while j < 11 : 
                print('premier ligne monstre')
                x += 70 #changement de la poition horizontale pour chaque mechant
                bad_guy = mechant.Mechant(self.window,self.canvas,x,y) 
                sous_lst_enemy.append(bad_guy)
                j += 1
            i += 1 
                    
            self.enemy.append(sous_lst_enemy)

    
    def update_score(self):
        """ Cette fonction sert à actualiser le score du joueur 
        Parametres:
            score : le label tkinter qui affiche le score
        """
        # on let à jour l'affichaffichage du score
        self.display_score.set(' Votre score est de : '+str(self.score))
        self.canvas.after(10, self.update_score)
        
    def launch_game(self):
        """ cette fonction permet de lancer une partie """
        self.update_score()
        # tout les truc interactifs 
        self.crea_mechant()
        self.move_groupe()
        self.player.crea_vie()
        self.player.tout()
        self.gestion_collsions()  
        self.gestion_fin_de_vie_EHPHAD()

    def main (self):
        
        """ the fonction running the whole project """
        self.window.geometry( "{}x{}".format(self.width, self.height) )
        self.principale() 
        #self.launch_game()
        self.window.mainloop()


#Main -------------------------------------------------------------------------
#Note : à mettre dans un autre fichier --> fichier main       

ecran= class_window(1000,800)
#ecran.structure_fenetre()

ecran.main()