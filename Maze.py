import random as r
from icecream import ic
class Maze:
    """
    Classe Labyrinthe
    Représentation sous forme de graphe non-orienté
    dont chaque sommet est une cellule (un tuple (l,c))
    et dont la structure est représentée par un dictionnaire
      - clés : sommets
      - valeurs : ensemble des sommets voisins accessibles
    """
    def __init__(self, height, width, empty=False):
        """
        Constructeur d'un labyrinthe de height cellules de haut
        et de width cellules de large
        Les voisinages sont initialisés à des ensembles vides
        Remarque : dans le labyrinthe créé, chaque cellule est complètement emmurée
        """
        self.height    = height
        self.width     = width
        self.neighbors = {(i,j): set() for i in range(height) for j in range (width)}

        if empty:
            self.empty()


    def info(self):
        """
        **NE PAS MODIFIER CETTE MÉTHODE**
        Affichage des attributs d'un objet 'Maze' (fonction utile pour deboguer)
        Retour:
            chaîne (string): description textuelle des attributs de l'objet
        """
        txt = "**Informations sur le labyrinthe**\n"
        txt += f"- Dimensions de la grille : {self.height} x {self.width}\n"
        txt += "- Voisinages :\n"
        txt += str(self.neighbors)+"\n"
        valid = True
        for c1 in {(i, j) for i in range(self.height) for j in range(self.width)}:
            for c2 in self.neighbors[c1]:
                if c1 not in self.neighbors[c2]:
                    valid = False
                    break
            else:
                continue
            break
        txt += "- Structure cohérente\n" if valid else f"- Structure incohérente : {c1} X {c2}\n"
        return txt

    def __str__(self):
        """
        **NE PAS MODIFIER CETTE MÉTHODE**
        Représentation textuelle d'un objet Maze (en utilisant des caractères ascii)
        Retour:
             chaîne (str) : chaîne de caractères représentant le labyrinthe
        """
        txt = ""
        # Première ligne
        txt += "┏"
        for j in range(self.width-1):
            txt += "━━━┳"
        txt += "━━━┓\n"
        txt += "┃"
        for j in range(self.width-1):
            txt += "   ┃" if (0,j+1) not in self.neighbors[(0,j)] else "    "
        txt += "   ┃\n"
        # Lignes normales
        for i in range(self.height-1):
            txt += "┣"
            for j in range(self.width-1):
                txt += "━━━╋" if (i+1,j) not in self.neighbors[(i,j)] else "   ╋"
            txt += "━━━┫\n" if (i+1,self.width-1) not in self.neighbors[(i,self.width-1)] else "   ┫\n"
            txt += "┃"
            for j in range(self.width):
                txt += "   ┃" if (i+1,j+1) not in self.neighbors[(i+1,j)] else "    "
            txt += "\n"
        # Bas du tableau
        txt += "┗"
        for i in range(self.width-1):
            txt += "━━━┻"
        txt += "━━━┛\n"

        return txt

    def add_wall(self, c1, c2):
        '''
        Ajoute un mur entre c1 et c2.

        :param c1: première cellule
        :param c2: seconde cellule
        '''
        # Facultatif : on teste si les sommets sont bien dans le labyrinthe
        assert 0 <= c1[0] < self.height and \
               0 <= c1[1] < self.width and \
               0 <= c2[0] < self.height and \
               0 <= c2[1] < self.width, \
            f"Erreur lors de l'ajout d'un mur entre {c1} et {c2} : les coordonnées de sont pas compatibles avec les dimensions du labyrinthe"
        # Ajout du mur
        if c2 in self.neighbors[c1]:  # Si c2 est dans les voisines de c1
            self.neighbors[c1].remove(c2)  # on le retire
        if c1 in self.neighbors[c2]:  # Si c3 est dans les voisines de c2
            self.neighbors[c2].remove(c1)  # on le retire


    def remove_wall(self, c1:tuple , c2:tuple):
        if not ((0 <= c1[0] <= self.height) and
                (0 <= c2[0] <= self.height) and
                (0 <= c1[1] <= self.width) and
                (0 <= c2[1] <= self.width)):
            raise ValueError("remove_wall : au moins une cellule est hors du labyrinthe")

        if not ((abs(c1[0]-c2[0]) <= 1 and abs(c1[1]-c2[1]) <= 0) or
                (abs(c1[0]-c2[0]) <= 0 and abs(c1[1]-c2[1]) <= 1)):
            raise ValueError("remove_wall : Les cellules ne sont pas adjacentes")

        if c2 not in self.neighbors[c1]:
            self.neighbors[c1].add(c2)
        if c1 not in self.neighbors[c2]:
            self.neighbors[c2].add(c1)


    def get_walls(self):
        '''
        Retourne la liste de tous les murs sous la forme d’une liste de tuple de cellules

        :return: liste des murs
        '''
        walls = []

        for key in self.neighbors.keys():
            # generate all links
            possibles_links = {(key[0], key[1]-1),  # right
                               (key[0]+1, key[1])} # bottom

            # remove existing links
            destinations = possibles_links - self.neighbors[key]

            # remove out of range walls
            for destination in destinations:
                if self.is_in_maze(destination):
                    walls.append( (key, destination) )

        return walls


    def fill(self):
        '''
        Ajoute tous les murs possibles dans le labyrinthe.
        '''
        for key in self.neighbors.keys():
            self.neighbors[key] = []


    def empty(self):
        for x in range(self.height):
            for y in range(self.width):
                self.neighbors[(x,y)] = set()
                possibles_links = self.get_contiguous_cells((x, y))

                for destination in possibles_links:
                    self.neighbors[(x,y)].add(destination)

    def get_contiguous_cells(self, c: tuple)-> list:
        '''
        Retourne la liste des cellules contigües à c dans la grille (sans s’occuper des éventuels murs)

        :param c: tuple (x, y) contenant les coordonnées de la cellule à traiter
        :return: liste des cellules contigües à c
        '''
        x = c[0]
        y = c[1]
        contiguous_cells = [(x, y + 1),  # left
                            (x, y - 1),  # right
                            (x - 1, y),  # top
                            (x + 1, y)]  # bottom
        for cell in contiguous_cells:
            if not (self.is_in_maze(cell)):
                contiguous_cells.remove(cell)
        return contiguous_cells



    def get_reachable_cells(self, c: tuple)-> list:
        '''
        Retourne la liste des cellules accessibles depuis c (c’est-à-dire les cellules contiguës à c qui sont dans le voisinage de c)

        :param c: tuple (x, y) contenant les coordonnées de la cellule à traiter
        :return: liste des cellules accessibles via c
        '''
        return [cell for cell in self.neighbors[c]]

    def get_cells(self)-> list:
        return [key for key in self.neighbors.keys()]

    def is_in_maze(self, c: tuple):
        '''
        Retourne True si les coordonnées sont cohérentes avec le labyrinthe, False sinon

        :param c: tuple (x, y) de coordonnées
        :return:
        '''
        return 0 <= c[0] < self.height and 0 <= c[1] < self.width

    @classmethod
    def exploration(cls, w, h):
        #Initialise le labyrinthe avec une cellule recupérée aléatoirement dans les cellules disponnible.
        laby = cls(h, w)
        cellule_recup = laby.get_cells()
        cellule = r.choice(cellule_recup)
        visiter = [cellule]
        pile = [cellule]
        #créer un tanque qui dit que si pile n'est pas vide alors ca continue
        while pile:
            pile_haut = pile.pop(0)
            non_visited = []
            #Vérifie si la cellule a des voisin non visiter
            for cell in laby.get_contiguous_cells(pile_haut):
                if cell not in visiter:
                    if laby.is_in_maze(cell):
                        non_visited.append(cell)
            '''
            Vérifie si la cellule est non visiter si c'est non visiter il remet sur la pile la cellule
            et choisie une cellule aléatoirement parmis les non visiter et retire le mur entre les deux
            '''
            if non_visited:
                pile.insert(0,pile_haut)
                ma_cellule = r.choice(non_visited)
                ic(pile_haut,ma_cellule)
                laby.remove_wall(pile_haut, ma_cellule)
                visiter.append(ma_cellule)
                pile.insert(0,ma_cellule)
        return laby