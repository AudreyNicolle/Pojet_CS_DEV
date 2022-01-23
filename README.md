    Ce dossier contient le projet du space invader revisité. Les règles du jeu 
sont affichées dans la commande options - à propos, de la fenêtre du jeu lorsque 
vous démarrez le programme.

L'adresse du répertoire git est la suivante : 
    https://github.com/AudreyNicolle/Pojet_CS_DEV.git
    
    Ce projet est composé d'un fichier principal, le ficher Fenetre.py. 
En effet, le programme principal qui permet de créer un objet de la classe 
Fenetre, qui, elle, permet de lancer le jeu en appuyant sur le bouton 
jouer. Ainsi, pour mettre en route le programme, il faut lire le fichier 
Fenetre.
    Les différentes entités de ce jeu soit les méchants (normaux ou méchant bonus), 
les projectiles (boule de feu, rocher, projectile secret ou les bonus), les 
îlots et le joueur sont chacun associé à une classe 'mère' avec potentiellement 
des classes 'fille'. 
    Ces classes 'mère' sont, chacune, associées à un fichier qui porte leur nom. 
Les objets de ces classes sont utilisés et liés entre eux dans la classe 
Fenêtre, par exemple les collisions qui sont l'interaction de deux 
entités différentes sont gérés dans la classe Fenetre.
    Les interactions qui sont propres aux entités elles-mêmes sont gérées par 
leur classe, par exemple le fait de bouger le joueur est géré par la classe 
Player.

Toutes les images utilisées sont libre de droit ou bien leur utilisation a été
validé par la personne concernée.
