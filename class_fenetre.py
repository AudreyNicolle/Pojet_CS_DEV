#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 13 14:42:01 2021
@author: emma.begard & audrey.nicolle

Ce fichier contient la classe qui s'occupe de la gestion de la fenêtre du jeu 
et des actions de celui-ci.

To-do : - faire des niveaux de difficultés.
"""
#Import -----------------------------------------------------------------------

import tkinter as tk
import player as pl
import mechant 
from random import randint
import ilot as I
from PIL import Image, ImageTk
import projectile as P
import time


#Classe -----------------------------------------------------------------------

class Fenetre :
    
    def __init__(self) :
        """ 
        Cette classe permet de générer le fenêtre de jeu, la zone de jeu canvas, le
        lancement du jeu, l'affichage de la section ''À propos' et de gérer les
        actions entres les différentes entités du jeu.
        
        En effet, elle permet :
            - de gérer la collision entre deux entités. 
            - de gérer les actions liées aux collisions des différentes entités 
                du jeu.
            - de gérer les mouvements des différentes entités.
            - de gérer la fin du jeu, lorsque le joueur meurt.
            - de gérer l'appartion du mechant bonus version gentil et énervé.
            - de créer les matrices contenant les ilots ou les méchants.
            - des gérer les créations des projectiles des différentes entités
            - de gérer le score du joueur.
            - de gérer l'apport des bonus au joueur.
        
        Parameters : 
                    self.width : largeur de la fenetre (int)
                    self.height : hauteur de la fenetre (int)
                    self.window : fenêtre du jeu (objet Tk)
                    self.canvas : zone de jeu (objet tk)
                    self.player : joueur (objet canvas) 
                    self.ennemy : contient les objets mechant (list)
                    self.score  : le score du joueur
                    self.display_score : le texte dans le label 
                                        score de la fenêtre d'affichage
                    self.background : image du fond du jeu (objet tk)
                    self.papa : mechant bonus (int, partie sur pause ou objet 
                                               canvas, partie en cours)
                    self.game : s'il est égal à True le jeu est en cours (booléen)
                    self.lst_ilot : contient les 3 objets Ilot (list)
                    self.lst_bonus : contient les objets bonus (lst)
        """  
        self.width = 1000
        self.height = 800
        self.window = tk.Toplevel()
        self.canvas = tk.Canvas(self.window, bg='black')
        self.player = pl.Player( self.window, self.canvas)
        self.enemy = []                   
        self.game = True
        self.score = 0
        self.display_score = tk.StringVar()
        self.im_background = Image.open('Image/fond.png')
        self.background = ImageTk.PhotoImage(self.im_background.resize((1000,800))) 
        self.papa  = 0
        self.lst_ilot = [] 
        self.lst_bonus = []
      
    def about(self):
        """ 
        Cette fonction ouvre un fichier texte qui décrit le fonctionnement du 
        jeu.
        
        Parameters : none.
        
        Returns : none.
        """
        
        # la chaîne de caractères avec la description du jeu etc ...
        text =''
        # on lit notre fichier de description du jeu
        with open ('a_propos.txt','r', encoding="utf8") as des:
            
            for line in des :
                text += str(line)
                
        tk.messagebox.showinfo('A propos', text)


        
    def principale(self):
        
        """ 
        Cette fonction permet de créer la fenêtre et faire appaître les widgets.
        
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
        menufichier.add_command(label="À propos ", command=self.about)
    
        
        # on créer un bouton pour lancer une partie
        play = tk.Button(self.window, text='Jouer', command= self.launch_game )
        play.grid(row = 10, column =20)
        
        # on crée un bouton de sortie
        button_quit = tk.Button(self.window, text='Quitter', command=self.window.destroy)
        button_quit.grid(row = 20, column = 20)

        # resizeable playing area
        can_width =self.window.winfo_screenwidth()
        can_height = self.window.winfo_screenheight()
        self.canvas.config(width=can_width, height=can_height)
        self.canvas.grid(column=0, row=2, rowspan = 19)
        
        #Fond du Jeu
        self.canvas.create_image(0, 0, image=self.background,  anchor = "nw")
        
    def crea_ilots (self) : 
        """
        Cette fonction permet de créer 3 îlots composé de lignes de petits blocs.
        
        Parameters : none.
        
        Returns : none.
        """
        
        i = 0 
        x = 80
        y = 500
        
        while i < 3 : 
            
            ilot = I.Ilot(self.window,self.canvas,x,y)
            ilot.crea_ilot() #pour créer les blocs qui le composent
            self.lst_ilot.append(ilot)
            x += 350 
            i += 1
            
        
    def gestion_tir_M_bonus(self) : 
        """
        Cette fonction permet de faire tirer le méchant bonus, soit avec son 
        arme secrète s'il est activée où comme un méchant normal.
        
        Parameters : none
        
        Returns : none.
        """
        if self.game :
            
            if self.papa.arme_secrete == 0 :
                self.papa.tir(randint(1,100))
            
            else :
               self.papa.tir_secret(randint(1,100))
            
            self.canvas.after(50, self.gestion_tir_M_bonus)
        
      
    def bad_daddy_is_comming(self) :
        """
        Cette fonction permet de mofifier la tête du mechant bonus quand il y a
        moins de mechant.
        
        Parameters : none.
        
        Returns : none
        """
        if self.game :
            
            cpt = 0
            for sous_lst in self.enemy :
                for bad_guy in sous_lst :
                    cpt +=1
        
            #on change l'image si if validé
            if cpt <= 29 : 
                self.papa.into_mechant()
            
        
            else :
                self.canvas.after(50, self.bad_daddy_is_comming) 
        
    def gestion_fin_de_vie_EHPHAD (self) :
        
        """
        Cette fonction permet de supprimer les éléments canvas nécessaires 
        quand le joueur a perdu. On met le jeu sur pause grâce à self.game 
        jusqu'à la prochaine partie.
        
        Parameters : none
        
        Returns : none
        """
        
        if self.player.nb_vie == [] :
            
            #on supprime les canvas des mechants et leurs projectiles
            for sous_lst in self.enemy :
                for bad_guy in sous_lst : 
                    for projectile in bad_guy.lst_projectile :
                        self.canvas.delete(projectile.projectile)
                   
                    bad_guy.lst_projectile = []
                    self.canvas.delete(bad_guy.mechant)
                    
            self.enemy = []
            
            #on supprime les ilots
            for ilot in self.lst_ilot :
                for lst_bloc in ilot.lst_carre : 
                    for bloc in lst_bloc :
                        self.canvas.delete(bloc)
                ilot.lst_carre = []
                
            #on supprime les tartiflettes 
            for bonus in self.lst_bonus : 
                self.canvas.delete(bonus)
            
            self.lst_bonus = []
            
            #on supprime les projectiles du mechant bonus
            for projectile in self.papa.lst_projectile : 
                self.canvas.delete(projectile.projectile)
            
            self.papa.lst_projectile = []
            
            #on supprime le mechant bonus et on le reset
            self.canvas.delete(self.papa.mechant)
            self.papa = 0
            
            #on supprime les projectiles du joueur
            for projectil in self.player.projectile :
                self.canvas.delete(projectile.projectile)
            
            self.player.projectile = []
            
            #on supprime les bonus s'il y en a
            for bonus in self.lst_bonus : 
                self.canvas.delete(bonus.projectile)
                
            for resistance in self.player.thermos_bu : 
                self.canvas.delete(resistance)
            
            self.player.lst_bonus = []   
            
            #on supprime le canvas du joueur
            self.canvas.delete(self.player.yeti)
            
            #on met le jeu en pause
            self.game = False
                    
        else:
             
            self.canvas.after(50, self.gestion_fin_de_vie_EHPHAD)    
        
    
    def thermos_bu (self) : 
        """ 
        Cette fonction permet de faire appraître un carré rouge symbolisant 
        que la résistance à un tir est activée.
        
        Parameters : none.
        
        Returns : none.
        """
        
        if self.player.thermos_bu == [] : 
            
            resistance = self.canvas.create_rectangle(self.player.x +20,\
                         self.player.y + 10,self.player.x + 30 ,self.player.y + 20,\
                             width = 0, fill = 'red')
                
            self.player.thermos_bu.append(resistance)
            self.player.resistance = 1
            
    def fin_thermos (self) : 
        """ 
        Cette fonction permet d'enlever la fonction du thermos.
        
        Parameters : none.
        
        Returns : none.
        """

        if self.player.thermos_bu != []:

            
            self.canvas.delete(self.player.thermos_bu[0])
            self.player.resistance = 0
            self.player.thermos_bu = []
            
    def on_prepare_un_bonus (self) : 
        """
        Cette fonction permet de créer une bonne tartiflette à donner à Mr.Yeti
        ou un thermos contenant la superbe potion.
        Les bonus sont crées au bout d'un temps aléatoire.
        
        Paramters : none.
        
        Returns : none.
        """
        if self.game :

            chance = randint(1,150)
            x = randint(0,1)

            # on crée une tartiflette
            if  chance == 1 :
                
                if x == 0 :
                    #on crée la tartiflette sur la coté gauche, 
                    #tartiflette.type = 21
                    bonus = P.Bonus(0, randint(100, 400), \
                                    self.canvas, "Image/tartiflette.jpg", 1,'21')
                
                else : 
                    #on crée la tartiflette sur le coté gauche, 
                    #tartiflette.type = 31
                    bonus = P.Bonus(900, randint(100, 400), \
                                    self.canvas, "Image/tartiflette.jpg", 1,'31')
        
                self.lst_bonus.append(bonus) 
            
            #on crée un thermos
            elif chance == 2 :

                if x == 0 :
                    
                    #on crée le thermos sur le coté gauche, 
                    #thermos.type = 22
                    bonus = P.Bonus(0, randint(100, 400), \
                                    self.canvas, "Image/thermos.png", 1,'22')
                else : 
                    #on crée la thermos sur le coté gauche, 
                    #thermos.type = 32
                    bonus = P.Bonus(900, randint(100, 400), \
                                    self.canvas, "Image/thermos.png", 1,'32')
                    
                
                
                self.lst_bonus.append(bonus) 
            
            self.canvas.after(100,self.on_prepare_un_bonus)
            
        
    
    def action_bonus (self) : 
        """
        Cette fonction permet de faire bouger les bonus, 
        de les faire disparaître si ça fait trop longtemps qu'ils sont là.
        
        Parameters : none.
     
        Returns : none.
        """
        if self.game : 
            
            for bonus in self.lst_bonus : 
                
                #on regarde combien de temps ils sont là et on supprime si sup
                # à 5s
                temps_de_vie = time.time_ns() - bonus.temps

                if temps_de_vie > 5000000000 : #5s

                    self.canvas.delete(bonus.projectile)
                    self.lst_bonus.remove(bonus)
                    
                # sinon on les fait avancer
                else :

                    bonus.run(self.lst_bonus)
                
            self.canvas.after(50, self.action_bonus) 

        
    def gestion_collisions(self):
        """
        Cette fonction permet de vérifier différents types de collisions
        entre différents types d'entités. Elles enlèvent la vie des entités si 
        besoin, elle set le score si besoin et vérifie que le mechant bonus soit 
        en vie.
        
        Parameters : none.
        
        Returns : none.
        """
        if self.game :
            #Si le mechant bonus n'a plus de vie, on le supprime.
            if self.papa.vie == 0 :
                self.canvas.delete(self.papa)
                self.score += 10
            
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
                            for projectile_P in self.player.projectile :

                                # s'il y a collision 
                                if self.collision(projectile_P.projectile,\
                                                  bad_guy.mechant,0) :
                                    
                                    projectile_P.vie -= 1
                                    bad_guy.perd_vie(-1)
                                    self.score += bad_guy.points

                                self.collision_ilot_projectile(projectile_P) 
                            
                                                                
                            #on gère les collisions projectile méchant vs joueur
                            #et projectile gentil
                            for projectile_M in bad_guy.lst_projectile :
                               
                                if self.collision(projectile_M.projectile, \
                                                  self.player.yeti,0) :
                                    
                                    projectile_M.vie -= 1

                                    if self.player.resistance == 0 :
                                        
                                        self.player.gestion_vie(-1)
                                        # on perds des points sur notre score, 
                                        #autant que le monstre rapporterais
                                        self.score -= bad_guy.points
                                     
                                    #on enlève la résistance du joueur si besoin 
                                    self.fin_thermos()
                                    
                                    
                                for projectile_P in self.player.projectile :
                                       
                                    if self.collision(projectile_M.projectile,\
                                                      projectile_P.projectile,0) :
                                            
                                        projectile_M.vie -= 1
                                        projectile_P.vie -= 1
                                
                                self.collision_ilot_projectile(projectile_M)
                        
                        
                            #on gère les collisions joueur vs méchant
                            if self.collision(bad_guy.mechant, self.player.yeti,0) :

                                bad_guy.perd_vie(-1)
                                
                                while len(self.player.nb_vie) >= 1 :
                                   
                                    self.player.gestion_vie(-1)
                                    # on perd du score, 2 fois plus que le monstre rapporte
                                    self.score -= 2*bad_guy.points
                    
                    
                        else :
                            # on enlève le méchant de la liste des enemys, car il est mort
                            lst_bad_guy.remove(bad_guy)
                            # on n'affiche plus le méchant
                            self.canvas.delete(bad_guy.mechant)
        
        
            for projectile in self.papa.lst_projectile :
                
                if self.collision(projectile.projectile,self.player.yeti,0):
                   
                    projectile.vie -= 1
                    
                
                    if self.player.resistance == 0 :
                        
                        self.player.gestion_vie(-1)                    
                        # on perds des points sur notre score, autant que le monstre rapporterais
                        self.score -= bad_guy.points
                    
                        #si c'est un tir_secret on enlève une vie en plus
                        if projectile.type == 1 :
                            self.player.gestion_vie(-1) 
                            
                    #on enlève la résistance du joueur si besoin 
                    self.fin_thermos()
                    
                self.collision_ilot_projectile(projectile)
               
             #on regarde si le bonus sont mangés/bus par le joueur  
            for bonus in self.lst_bonus : 

                if self.collision(bonus.projectile, self.player.yeti,100) :                    
                    
                    #on regarde si c'est une tartiflette
                    if bonus.type[1] == '1' :
                                       
                        self.player.gestion_vie(1)
                    
                    #sinon thermos
                    else :
                        self.thermos_bu()
                    
                    bonus.vie -= 1
                
            #on regarde si les projectiles du gentils rentrent en collision 
            #avec le mechant bonus
            for projectile in self.player.projectile : 
                
                if self.collision(projectile.projectile, self.papa.mechant, 0) :
                    self.papa.vie -= 1
                    projectile.vie -= 1
                    
            
            #on et un temps de rappel de la fonction de 50ms car en-dessous lorsqu'on
            #rappelle la fonction la collision n'est pas fini et cela fausse le reste
            #du programme
            self.canvas.after(50, self.gestion_collisions)
        
    def collision_ilot_projectile(self,projectile) :
        """
        Cette fonction permet de faire les actions nécessaires lorsqu'un projectile
        rentre en collision avec un ilot.
        
        Parameters :
            projectile : objet de la classe projectile
            
        Returns : none.
        """
        #les boucles for permettent de rentrer dans la liste et d'obtenir un
        #élément bloc
        for ilot in self.lst_ilot :
            for lst_bloc in ilot.lst_carre :
                for i,bloc in enumerate(lst_bloc) :

                    if self.collision(projectile.projectile, bloc,0) :

                        projectile.vie -= 1
                        self.canvas.delete(bloc)
                        del lst_bloc[i]

        
    def collision(self,entite1, entite2,y):
        """ 
        Cette fonction permet de voir si deux objets rentrent en collisions.
        
        Parameters : 
            - entite1 : premier objet concerné par la collision (objet canvas) 
            - entite1 : deuxième objet concerné par la collision (objet canvas)
            - y : permet d'ajouter de la sensibilité au niveau de l'axe des ordonnées
                    (int)
            
        Returns : on retourne un booléen. Vrai s'il y a eu collision.
        """
       
        #On récupère les coordonées de l'objet 1
        x_1 = self.canvas.bbox(entite1)[0] 
        x_2 = self.canvas.bbox(entite1)[2] 
        y_1 = self.canvas.bbox(entite1)[1] 
        y_2 = self.canvas.bbox(entite1)[3] 
        
        
        # les coordonnées de la deuxième entité
        coords2 = self.canvas.bbox(entite2)
        
        
        #On vérifie s'i y a une collison par la gauche de l'entité 1 sur l'entité 2
        # l'ajout de 10 à x_2 et la soustraction de 10 à x_1 est pour améliorer 
        #la sensibilité
        if (x_2 + 10 > coords2[0]> x_1 - 10) and (y_1 - y < coords2[1] <  y_2 ):

            return True
       
        #On vérifie s'i y a une collison par la droite de l'entité 1 sur l'entité 2       
        elif (x_2 + 10 > coords2[2]> x_1 - 10) and (y_1 - y < coords2[3] < y_2 ):

            return True   
      
    def move_papa(self) :
        
        """ 
        Cette fonction permet de se faire déplacer le méchant bonus de gauche à
        droite.
        
        Parameters : none
        
        Returns : none
        """
        if self.game :
            #On vérifie qu'il ne déplca pas le cadre et on le fait bouger. S'il le
            #dépasse on chnage sa direction.
            if self.papa.x > 900 : 

                self.papa.dir = -1 
                self.papa.move(0)
        
            elif self.papa.x < 2 :
                self.papa.dir = 1
                self.papa.move(0)
            
            else : 
                self.papa.move(0)
        
            self.canvas.after(50, self.move_papa) 
  
        
    def move_groupe (self) :
        """ 
        Permet de faire bouger horizontalement le bloc de mechant et de 
        descendre ce bloc lorsque un des sorciers d'une ligne de bloc touche 
        le cadre. Il permet aussi au mechant de tirer aléatoirement.
        
        Parameters : none
        
        Returns : none 
        """
        if self.game :
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
                            bad_guy.tir(randint(1,4000)) #permet de les faire tirer
                            #avec une chance sur 10 000, cf fontion tir
                    
                    #rappelle de la fonction pour un mouvement continu            
            self.canvas.after(1, self.move_groupe) 
                
                
    def crea_mechant (self) : 
        """ 
        Cette fonction permet de créer une matrice de méchant.
        
        Parameters : none
        
        Returns : none
        """
        
        #Initialisation 
        i = 0 
        y = 80
        while i < 4 :
            
            y += 60 #changement de la poition verticale pour chaque sous liste
            #Initialisation
            j = 0 
            sous_lst_enemy = [] 
            x = 50 
            
            while j < 11 : 
                
                    x += 70 #changement de la poition horizontale pour chaque mechant
                    bad_guy = mechant.Mechant(self.window,self.canvas,x,y) 
                    sous_lst_enemy.append(bad_guy)
                    j += 1
                    
            self.enemy.append(sous_lst_enemy)
            i += 1 
   
    def update_score(self):
        """ 
        Cette fonction sert à actualiser le score du joueur. 
        
        Parametres:
            score : le label tkinter qui affiche le score (objet tk)
            
        Returns : none.
        """
        if self.game :
            # on met à jour l'affichage du score
            self.display_score.set(' Votre score est de : ' + str(self.score))
            self.canvas.after(10, self.update_score)
       
            
    def launch_game(self):
        """ 
        Cette fonction permet de lancer une partie. Elle contient tous les appels
        de fonction qui permettent la bonne mise en route du jeu.
        
        Parameters : none.
        
        Returns : none.        
        """
        self.game = True
        self.ennemy = []
        self.score = 0
        self.display_score.set(' Votre score est de : 0')
        self.papa = mechant.M_bonus(self.window,self.canvas,450,60)  
        self.crea_mechant()        
        self.player.crea_vie()
        self.player.tout()
        self.papa.modif_caracteristique()
        self.crea_ilots()
        self.move_groupe()
        self.move_papa()
        self.bad_daddy_is_comming()
        self.gestion_collisions()  
        self.gestion_fin_de_vie_EHPHAD()                   
        self.gestion_tir_M_bonus()
        self.on_prepare_un_bonus()
        self.action_bonus()
        self.update_score()



    def main (self):
        
        """ 
        Cette fonction permet de mettre en route la fenêtre du jeu.
        
        Parameters : none.
        
        Returns : none.
        """
        
        self.window.geometry( "{}x{}".format(self.width, self.height) )
        self.principale() 
        self.window.mainloop()


#Main -------------------------------------------------------------------------
  
ecran= Fenetre()

ecran.main()


