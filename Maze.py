import random as r


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
        self.height = height
        self.width = width
        self.neighbors = {(i, j): set() for i in range(height) for j in range(width)}

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
        txt += str(self.neighbors) + "\n"
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
        for j in range(self.width - 1):
            txt += "━━━┳"
        txt += "━━━┓\n"
        txt += "┃"
        for j in range(self.width - 1):
            txt += "   ┃" if (0, j + 1) not in self.neighbors[(0, j)] else "    "
        txt += "   ┃\n"
        # Lignes normales
        for i in range(self.height - 1):
            txt += "┣"
            for j in range(self.width - 1):
                txt += "━━━╋" if (i + 1, j) not in self.neighbors[(i, j)] else "   ╋"
            txt += "━━━┫\n" if (i + 1, self.width - 1) not in self.neighbors[(i, self.width - 1)] else "   ┫\n"
            txt += "┃"
            for j in range(self.width):
                txt += "   ┃" if (i + 1, j + 1) not in self.neighbors[(i + 1, j)] else "    "
            txt += "\n"
        # Bas du tableau
        txt += "┗"
        for i in range(self.width - 1):
            txt += "━━━┻"
        txt += "━━━┛\n"

        return txt

    def add_wall(self, c1, c2):
        """
        Ajoute un mur entre c1 et c2.

        :param c1: Première cellule
        :param c2: seconde cellule
        """
        # Facultatif : on teste si les sommets sont bien dans le labyrinthe
        assert 0 <= c1[0] < self.height and \
               0 <= c1[1] < self.width and \
               0 <= c2[0] < self.height and \
               0 <= c2[1] < self.width, \
            f"Erreur lors de l'ajout d'un mur entre {c1} et {c2} : les coordonnées de sont pas compatibles avec les " \
            f"dimensions du labyrinthe"
        # Ajout du mur
        if c2 in self.neighbors[c1]:  # Si c2 est dans les voisines de c1
            self.neighbors[c1].remove(c2)  # on le retire
        if c1 in self.neighbors[c2]:  # Si c1 est dans les voisines de c2
            self.neighbors[c2].remove(c1)  # on le retire

    def remove_wall(self, c1, c2):
        """
        Retire le mur entre c1 et c2.

        :param c1: Première cellule
        :param c2: seconde cellule
        """
        # On teste si les sommets sont bien dans le labyrinthe
        if not ((0 <= c1[0] <= self.height) and
                (0 <= c2[0] <= self.height) and
                (0 <= c1[1] <= self.width) and
                (0 <= c2[1] <= self.width)):
            raise ValueError("remove_wall : au moins une cellule est hors du labyrinthe")

        # On teste si les cellules sont adjacentes
        if not ((abs(c1[0] - c2[0]) <= 1 and abs(c1[1] - c2[1]) <= 0) or
                (abs(c1[0] - c2[0]) <= 0 and abs(c1[1] - c2[1]) <= 1)):
            raise ValueError("remove_wall : Les cellules ne sont pas adjacentes")

        if c2 not in self.neighbors[c1]:  # Si c2 est dans les voisines de c1
            self.neighbors[c1].add(c2)  # Alors, on ajoute c2 aux voisins de c1
        if c1 not in self.neighbors[c2]:  # Si c1 est dans les voisines de c2
            self.neighbors[c2].add(c1)  # Alors, on ajoute c1 aux voisins de c2

    def get_walls(self):
        """
        Retourne la liste de tous les murs sous la forme d’une liste de tuple de cellules

        :return: liste des murs
        """
        walls = []

        for key in self.neighbors.keys():
            # generate all links
            possibles_links = {(key[0], key[1] - 1),  # right
                               (key[0] + 1, key[1])}  # bottom

            # remove existing links
            destinations = possibles_links - self.neighbors[key]

            # remove out of range walls
            for destination in destinations:
                if self.is_in_maze(destination):
                    walls.append((key, destination))

        return walls

    def fill(self):
        """
        Ajoute tous les murs possibles dans le labyrinthe.
        """
        for key in self.neighbors.keys():
            self.neighbors[key] = []

    def empty(self):
        """
        Supprime tous les murs du labyrinthe.
        """
        for x in range(self.height):
            for y in range(self.width):
                self.neighbors[(x, y)] = set()
                possibles_links = self.get_contiguous_cells((x, y))

                for destination in possibles_links:
                    self.neighbors[(x, y)].add(destination)

    def get_contiguous_cells(self, c: tuple) -> list:
        """
        Retourne la liste des cellules contigües à c dans la grille (sans s’occuper des éventuels murs)

        :param c: Tuple (x, y) contenant les coordonnées de la cellule à traiter
        :return: liste des cellules contigües à c.
        """
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

    def get_reachable_cells(self, c: tuple) -> list:
        """
        Retourne la liste des cellules accessibles depuis c (c’est-à-dire les cellules contiguës à c qui sont dans le
        voisinage de c)

        :param c: Tuple (x, y) contenant les coordonnées de la cellule à traiter
        :return: liste des cellules accessibles via c.
        """
        return [cell for cell in self.neighbors[c]]

    def get_cells(self) -> list:
        """
        Retourne la liste de toutes les cellules de la grille du labyrinthe.

        :return: Liste de cellules (x, y)
        """
        return [key for key in self.neighbors.keys()]

    def is_in_maze(self, c: tuple):
        """
        Retourne True si les coordonnées sont cohérentes avec le labyrinthe, False sinon

        :param c: tuple (x, y) de coordonnées
        :return:
        """
        return 0 <= c[0] < self.height and 0 <= c[1] < self.width

    @classmethod
    def gen_btree(cls, h, w):
        """
        Génère un labyrinthe à h lignes et w colonnes, en utilisant l’algorithme de construction par arbre binaire.

        :param h: Hauteur du labyrinthe
        :param w: largeur du labyrinthe
        :return: le labyrinthe généré
        """
        laby = Maze(h, w)
        cells = laby.get_cells()
        for cell in cells:
            contiguous_cells = []
            if cell[1] != laby.width - 1:
                contiguous_cells.append((cell[0], cell[1] + 1))  # right
            if cell[0] != laby.height - 1:
                contiguous_cells.append((cell[0] + 1, cell[1]))  # bottom
            # get already opened ways
            reachable_cells = laby.get_reachable_cells(cell)

            if len(contiguous_cells) == 2:
                contiguous_cell = r.choice(contiguous_cells)
                if contiguous_cell not in reachable_cells:
                    laby.remove_wall(cell, contiguous_cell)
                else:
                    contiguous_cells.remove(contiguous_cell)

            if len(contiguous_cells) == 1:
                if contiguous_cells[0] not in reachable_cells:
                    laby.remove_wall(cell, contiguous_cells[0])
        return laby

    @classmethod
    def gen_sidewinder(cls, h, w):
        """
        Génère un labyrinthe à h lignes et w colonnes, en utilisant l’algorithme sidewinder.

        :param h: Hauteur du labyrinthe
        :param w: largeur du labyrinthe
        :return: le labyrinthe généré
        """
        laby = Maze(h, w)  # création d’un labyrinthe plein

        for i in range(laby.height - 1):
            seq = []  # Initialiser une variable séquence comme liste vide
            for j in range(laby.width - 1):
                seq.append((i, j))  # Ajouter la cellule (i, j) à la séquence
                is_pile = bool(r.getrandbits(1))  # Tirer à pile ou face
                if is_pile and j < laby.width - 2:  # Si c’est pile et qu'on n'est pas sur la dernière colonne
                    contiguous_cell = (i, j + 1)
                    laby.remove_wall((i, j), contiguous_cell)  # Casser le mur EST de la cellule (i, j)
                else:  # Si c'est face ou si on est sur la dernière colonne
                    if seq:  # Si la séquence n'est pas vide
                        cell = r.choice(seq)  # Choisir une cellule de la séquence au hasard
                        south_cell = (cell[0] + 1, cell[1])
                        laby.remove_wall(cell, south_cell)  # Casser le mur SUD de la cellule choisie
                    seq = []  # Réinitialiser la séquence à une liste vide

            # Ajouter la dernière cellule à la séquence et casser son mur SUD
            seq.append((i, laby.width - 1))
            south_cell = (i + 1, laby.width - 1)
            laby.remove_wall(seq[-1], south_cell)

        # Casser tous les murs EST de la dernière ligne
        for j in range(laby.width - 1):
            cell = (laby.height - 1, j)
            east_cell = (cell[0], cell[1] + 1)
            if laby.is_in_maze(east_cell):
                laby.remove_wall(cell, east_cell)

        return laby

    @classmethod
    def gen_fusion(cls, h, w):
        """
        Génère un labyrinthe à h lignes et w colonnes, en utilisant l’algorithme de fusion de chemins.

        :param h: Hauteur du labyrinthe
        :param w: largeur du labyrinthe
        :return: le labyrinthe généré
        """
        # Création du labyrinthe initial avec tous les murs
        laby = cls(h, w)

        # Initialisation des labels pour chaque cellule
        labels = {}
        for i, j in laby.get_cells():
            labels[(i, j)] = (i, j)

        # Obtention de la liste de tous les murs et mélange aléatoire
        walls = laby.get_walls()
        r.shuffle(walls)

        # Parcours des murs
        for c1, c2 in walls:
            if laby.is_in_maze(c1) and laby.is_in_maze(c2):
                # Récupération des labels des deux cellules séparées par le mur
                label1 = labels[c1]
                label2 = labels[c2]
                if label1 != label2:
                    # Cassage du mur
                    laby.remove_wall(c1, c2)

                    # Fusion des chemins en affectant le label de label1 à toutes les cellules ayant le label de label2
                    new_label = label2
                    old_label = label1
                    for cell in labels:
                        if labels[cell] == old_label:
                            labels[cell] = new_label

        # Retour du labyrinthe finalisé
        return laby

    @classmethod
    def gen_exploration(cls, w, h):
        # Initialise le labyrinthe avec une cellule recupérée aléatoirement dans les cellules disponibles.
        laby = cls(h, w)
        cellule_recup = laby.get_cells()
        cellule = r.choice(cellule_recup)
        visiter = [cellule]
        pile = [cellule]
        # tant que la pile n'est pas vide
        while pile:
            pile_haut = pile.pop(0)
            non_visited = []
            # Vérifie si la cellule a des voisins non visités
            for cell in laby.get_contiguous_cells(pile_haut):
                if cell not in visiter:
                    if laby.is_in_maze(cell):
                        non_visited.append(cell)
            '''
            Vérifie si la cellule est non visiter si c'est non visiter il remet sur la pile la cellule
            et choisie une cellule aléatoirement parmis les non visiter et retire le mur entre les deux
            '''
            if non_visited:
                pile.insert(0, pile_haut)
                ma_cellule = r.choice(non_visited)
                laby.remove_wall(pile_haut, ma_cellule)
                visiter.append(ma_cellule)
                pile.insert(0, ma_cellule)
        return laby

    def overlay(self, content=None):
        """
        Rendu en mode texte, sur la sortie standard, \
        d'un labyrinthe avec du contenu dans les cellules
        Argument :
            content (dict) : dictionnaire tq content[cell] contient le caractère à afficher au milieu de la cellule
        Retour :
            string
        """
        if content is None:
            content = {(i, j): ' ' for i in range(self.height) for j in range(self.width)}
        else:
            # Python >=3.9
            # content = content | {(i, j): ' ' for i in range(
            #    self.height) for j in range(self.width) if (i,j) not in content}
            # Python <3.9
            new_content = {(i, j): ' ' for i in range(self.height) for j in range(self.width) if (i, j) not in content}
            content = {**content, **new_content}
        txt = r""
        # Première ligne
        txt += "┏"
        for j in range(self.width - 1):
            txt += "━━━┳"
        txt += "━━━┓\n"
        txt += "┃"
        for j in range(self.width - 1):
            txt += " " + content[(0, j)] + " ┃" if (0, j + 1) not in self.neighbors[(0, j)] else " " + content[
                (0, j)] + "  "
        txt += " " + content[(0, self.width - 1)] + " ┃\n"
        # Lignes normales
        for i in range(self.height - 1):
            txt += "┣"
            for j in range(self.width - 1):
                txt += "━━━╋" if (i + 1, j) not in self.neighbors[(i, j)] else "   ╋"
            txt += "━━━┫\n" if (i + 1, self.width - 1) not in self.neighbors[(i, self.width - 1)] else "   ┫\n"
            txt += "┃"
            for j in range(self.width):
                txt += " " + content[(i + 1, j)] + " ┃" if (i + 1, j + 1) not in self.neighbors[(i + 1, j)] else " " + \
                                                                                                                 content[
                                                                                                                     (
                                                                                                                     i + 1,
                                                                                                                     j)] + "  "
            txt += "\n"
        # Bas du tableau
        txt += "┗"
        for i in range(self.width - 1):
            txt += "━━━┻"
        txt += "━━━┛\n"
        return txt

    def solve_dfs(self, start, stop):
        """
        Résout le labyrinthe en utilisant le parcours en largeur.

        :param start: Cellule servant de point de départ
        :param stop: Cellule servant de point d'arrivée
        :return: la liste des cellules à explorer dans l'ordre pour aller du point start à stop.
        """
        visited = []
        pile = [start]  # Placer start dans la struture d’attente (pile) et marquer start
        found = False
        predecesseurs = {start: start}  # Mémoriser l’élément prédécesseur de start comme étant start
        while len(visited) < self.width * self.height and not found:  # Tant qu’il reste des cellules non-marquées
            cell = pile.pop()  # Prendre la « première » cellule et la retirer de la structure
            if cell == stop:
                found = True  # on a trouvé un chemin vers la cellule de destination
            else:
                for neighbor in self.get_reachable_cells(cell):  # Pour chaque voisine de cell
                    if neighbor not in visited:  # Si elle n’est pas marquée
                        visited.append(neighbor)  # La marquer
                        pile.append(neighbor)  # La mettre dans la structure d’attente
                        predecesseurs[neighbor] = cell  # Mémoriser son prédécesseur comme étant c

        cell = stop
        way = []
        while cell != start:
            way.append(cell)
            cell = predecesseurs[cell]  # mettre le prédécesseur de cell dans cell
        way.append(start)

        return way

    def solve_rhr(self, start, stop):
        """
        Résout le labyrinthe en utilisant la technique de la main droite, à partir de la cellule de départ donnée.

        :return: La liste ordonnée des cellules visitées pour atteindre la sortie.
        """
        # On initialise la cellule courante avec la cellule de départ et la direction avec 'droite'.
        current_cell = start
        current_direction = 'droite'
        visited_cells = [current_cell]

        while current_cell != stop:
            # On détermine la cellule suivante en fonction de la direction courante.
            if current_direction == 'droite':
                next_cell = (current_cell[0], current_cell[1] + 1)
            elif current_direction == 'bas':
                next_cell = (current_cell[0] + 1, current_cell[1])
            elif current_direction == 'gauche':
                next_cell = (current_cell[0], current_cell[1] - 1)
            else:
                next_cell = (current_cell[0] - 1, current_cell[1])

            # Si la cellule suivante n'a pas de mur dans la direction courante, on avance dans cette direction.
            if next_cell in self.neighbors[current_cell]:
                visited_cells.append(next_cell)
                current_cell = next_cell
                # On tourne à droite en changeant la direction courante de 90° dans le sens horaire.
                if current_direction == 'droite':
                    current_direction = 'bas'
                elif current_direction == 'bas':
                    current_direction = 'gauche'
                elif current_direction == 'gauche':
                    current_direction = 'haut'
                elif current_direction == 'haut':
                    current_direction = 'droite'
            # Sinon, on tourne à gauche en changeant la direction courante de 90° dans le sens anti-horaire.
            else:
                # On tourne à gauche en changeant la direction courante de 90° dans le sens anti-horaire.
                if current_direction == 'droite':
                    current_direction = 'haut'
                elif current_direction == 'haut':
                    current_direction = 'gauche'
                elif current_direction == 'gauche':
                    current_direction = 'bas'
                elif current_direction == 'bas':
                    current_direction = 'droite'
        return visited_cells


    def distance_geo(self, cell1, cell2):
        """
        Calcule la distance géodésique entre deux cellules.

        :param cell1: La première cellule.
        :param cell2: La deuxième cellule.
        :return: La distance géodésique entre les deux cellules.
        """
        return len(self.solve_dfs(cell1, cell2)) - 1


    def distance_man(self, cell1, cell2):
        """
        Calcule la distance de Manhattan entre deux cellules.

        :param cell1: La première cellule.
        :param cell2: La deuxième cellule.
        :return: La distance de Manhattan entre les deux cellules.
        """
        return abs(cell1[0] - cell2[0]) + abs(cell1[1] - cell2[1])