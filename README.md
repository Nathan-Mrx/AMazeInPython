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
4. Lancez le fichier main.py avec des privilèges d'administrateurs
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

Une fois le script lancé, il vous sera proposé de générer votre labyrinthe : pour cela, vous devrez sélectionner l'algorithme de génération de votre choix en entrant 1, 2, 3, 4 ou 5, puis la taille souhaitée pour le labyrinthe en entrant 1, 2, 3 ou 4.

Le labyrinthe est alors généré. Votre personnage est représenté par la lettre P. L'arrivée est représentée par la lettre A. Vous pouvez vous déplacer en utilisant les touches Z, Q, S, D. 

Pour quitter le jeu, appuyez sur X.

## Crédits

Nathan Merieux

Jaïmy Dumont

Remerciements : Etienne Coutant, Olivier Nocent, Frédéric Blanchard pour nous avoir proposé ce projet.

## License

AMazeInPython vous est distribué sous la license [Creative Commons](https://creativecommons.org/licenses/by/4.0/).