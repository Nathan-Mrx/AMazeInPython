# AMazeInPython

AMazeinPython est un projet universitaire développé en python. C'est un jeu vidéo dans lequel le joueur se déplace dans un labyrinthe généré aléatoirement selon des algorithmes.

## Installation

La procédure d'installation est différente selon le système d'exploitation

### Windows 

1. Vous devez installer [python](https://www.python.org/downloads/) depuis leur site officiel.

2. Vous devrez ensuite installer un module à python :
   1. Appuyez sur la touche Windows et R en même temps
   2. Une fenêtre s'ouvre alors, tapez 'cmd' et appuyez sur entrée
   3. Une autre fenêtre s'ouvre, entrez-y la commande suivante

            pip install keyboard

3. Télécharger l'archive de ce dépôt et décompressez-la
4. Lancez le fichier main.py

         python sae-s2-labyrinthes-merieux-nathan-jaimy-dumont/main.py

5. Profitez

### Linux

1. Installer python

        sudo apt-get install python3

2. Installer le module keyboard

        pip install keyboard

3. Clonez le dépôt

        sudo apt-get install git
        git clone https://iut-info.univ-reims.fr/gitlab/dumo0057/sae-2-s2-labyrinthes-merieux-nathan-dumont-jaimy.git

4. lancez le fichier main.py

        cd sae-2-s2-labyrinthes-merieux-nathan-dumont-jaimy
        sudo python main.py

### Macintosh

1. Vous devez installer [python](https://www.python.org/downloads/) depuis leur site officiel.

2. Ouvrez un terminal (Cmd + Espace et tapez terminal, appuyez sur entrée)

3. Installer le module keyboard

        pip install keyboard

4. Installez Brew

         /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

5. Installez Git

         brew install git

6. Clonez le dépôt

         git clone https://iut-info.univ-reims.fr/gitlab/dumo0057/sae-2-s2-labyrinthes-merieux-nathan-dumont-jaimy.git

7. Lancez le fichier main.py

        cd sae-2-s2-labyrinthes-merieux-nathan-dumont-jaimy
        sudo python main.py

## Utilisation

Une fois le script lancé, il vous sera proposé choisir un mode de jeu, puis une difficulté

### Mode de jeu

#### Mode arcade
Dans le mode arcade, vous jouez 5 parties à la suite. Vous commencez en haut à gauche du labythithe et devez aller en bas à gauche.

#### Mode Endless
Dans le mode Endless, vous jouez autant de parties que vous le souhaitez. Vous commencez en haut à gauche du labythithe et devez aller en bas à gauche.

#### Mode Random Arcade
Dans le mode Random Arcade, vous jouez 5 parties à la suite. Vous commencez et devez aller à un point aléatoire du labyrinthe.

#### Mode Random Endless
Dans le mode Random Endless, vous jouez autant de parties que vous le souhaitez. Vous commencez et devez aller à un point aléatoire du labyrinthe.

### Difficulté

#### Facile
La difficulté facile génère un labyrinthe de 10x10 cases.

#### Moyen
La difficulté moyenne génère un labyrinthe de 20x20 cases.

#### Difficile
La difficulté difficile génère un labyrinthe de 30x30 cases.

#### Expert
La difficulté expert génère un labyrinthe de 40x40 cases.

### Commandes
Vous pouvez vous déplacer avec Z, Q, S, D. Vous pouvez quitter le jeu en appuyant sur X.


## Crédits

Nathan Merieux

Jaïmy Dumont

Remerciements : Etienne Coutant, Olivier Nocent, Frédéric Blanchard pour nous avoir proposé ce projet.

## License

AMazeInPython vous est distribué sous la license [Creative Commons](https://creativecommons.org/licenses/by/4.0/).