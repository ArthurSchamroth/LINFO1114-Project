import numpy as np

liens = []
relations_matrice = {}
relations_array = []
matrice = []
# Traitement de la matrice depuis le csv vers matrice numpy
with open("../data.csv") as file:
    lines = file.readlines()
    for i in range(len(lines)):
        if i == 0:
            for j in lines[i].strip("\n").split(", "):
                relations_matrice[j] = []
        else:
            relations = lines[i].strip("\n").split(", ")
            relations = np.array(relations)
            for j in range(len(relations)):
                if int(relations[j]) == 1000000000000:
                    relations[j] = 0
            relations = relations.astype(int)
            liens.append(relations)
    matrice_np = np.array(liens)


def Dijkstra(np_matrice):
    """
    # Traitement de la matrice numpy pour la mettre sous forme de dictionnaire,
    # Facilitant ainsi l'utilisation des différentes données fournies par la matrice.
    for i in range(len(relations_matrice.keys())):
        relations_matrice[list(relations_matrice.keys())[i]] = liens[i]
    for i in relations_matrice:
        test = {"A": 0, "B": 0, "C": 0, "D": 0, "E": 0, "F": 0, "G": 0, "H": 0, "I": 0, "J": 0}
        for j in range(len(relations_matrice[i])):
            test[list(test.keys())[j]] = relations_matrice[i][j]
        relations_array.append(test)
    for i in range(len(relations_array)):
        objet = {}
        if relations_array[i] != 0:
            objet[list(relations_matrice.keys())[i]] = relations_array[i]
        matrice.append(objet)

    for ligne in matrice:
        for colonne in ligne:
            for key, value in list(ligne[colonne].items()):
                if value == 0:
                    ligne[colonne].pop(key, None)

    for i in matrice:
        print(i)"""


def Dijkstra(C):
    # Initialisation de la matrice des distances de sortie.
    # Ces distances sont initiées à l'infini.
    D = np.full((C.shape[0], C.shape[1]), np.inf)

    # Passage dans chaque ligne de la matrice
    for source in range(C.shape[0]):
        # Initialisation des distances à zéro pour les noeuds envers eux-mêmes
        D[source, source] = 0
        # Initialisation des noeuds précédents chaque noeud du graphe.
        # Initialement à -1 car cela indique que ce noeud n'a pas encore de prédécesseur.
        noeuds_precedents = np.full(C.shape[0], -1)

        # Création de l'ensemble des noeuds non visités.
        # Liste des indices des noeuds non-visités.
        nodes_index = []
        for i in range(C.shape[0]):
            nodes_index.append(i)
        # Passage en set pour être sûr de l'immuabilité de la liste des index
        noeuds_non_visites = set(nodes_index)

        while noeuds_non_visites:
            # Recherche du noeud le plus proche.
            noeud_courant = min(noeuds_non_visites, key=lambda x: D[source, x])
            # Suppression du noeud courant des noeuds non visités.
            noeuds_non_visites.remove(noeud_courant)

            # Mise à jour des distances des voisins
            # Passage dans chaque élément de chaque ligne de la matrice.
            for indice_voisin, poids_voisin in enumerate(C[noeud_courant]):
                # Si noeud pas connecté à voisin, ca passe
                if poids_voisin == 0:
                    continue
                # Calcul du nouveau poids du voisin
                nouveau_poids = D[source, noeud_courant] + poids_voisin
                # Si nouveau poids inférieur au poids enregistré pour ce voisin :
                # Le noeud courant change de valeur et le noeud courant est mis à jour.
                if nouveau_poids < D[source, indice_voisin]:
                    D[source, indice_voisin] = nouveau_poids
                    noeuds_precedents[indice_voisin] = noeud_courant

    return D


def bellman_ford(np_matrix):
    # Obtient le nombre de noeuds dans le graphe
    num_nodes = np_matrix.shape[0]

    # Initialise la matrice de sortie avec les valeurs de la matrice d'entrée
    distances = np_matrix.copy()

    # Répète l'algorithme V-1 fois
    for i in range(num_nodes - 1):
        # Pour chaque noeud de départ i
        for i in range(num_nodes):
            # Pour chaque noeud de destination j
            for j in range(num_nodes):
                # Pour chaque noeud intermédiaire k
                for k in range(num_nodes):
                    # Si le noeud de départ i et le noeud de destination j sont connectés par une arête
                    if np_matrix[i][j] != float('inf'):
                        # Met à jour la distance depuis la source en utilisant la formule de Bellman-Ford
                        distances[i][j] = min(distances[i][j], distances[i][k] + np_matrix[k][j])

    return distances


# Traitement de la matrice qui contient des distances entre chaque noeuds.
#
# Données : Un graphe orienté pondéré.
# Résultat : Le plus court chemin entre toute paire de sommets.
def Floyd_Warshall(np_matrices):
    # L'algorithme est constitué de N itération principales;
    # pour chaque itération k, on calcule les plus courts chemins entre toute paire de sommets
    # avec des sommets intermédiaires appartenant uniquement à l'ensemble {1,2,3,...k}
    for k in range(len(np_matrices)):
        for i in range(len(np_matrices)):
            for j in range(len(np_matrices)):
                # ici si le cout est égale à 0,ceci signifie que le cout est 10 exposant 12
                # bien évidemment, à l'exception des elements appartenant à la diagonale.
                if i != j and np_matrices[i][j] == 0:
                    np_matrices[i][j] = 10 ** 12

                # Le noeud courant change de la valeur s'il existe un sommet intermédiaire qui donc possède un
                # circuit de coût plus petit.
                np_matrices[i][j] = min(int(np_matrices[i][j]), int(np_matrices[i][k]) + int(np_matrices[k][j]))

    return np_matrices

distances = Dijkstra(matrice_np)
print(distances)