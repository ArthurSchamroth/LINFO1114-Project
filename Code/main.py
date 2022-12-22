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


def Dijkstra(C):
    # Initialisation de la matrice des distances de sortie.
    # Ces distances sont initialisées à l'infini.
    D = np.full((C.shape[0], C.shape[1]), float('inf'))

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

    # Gestion des "." indésirables dans la matrice de sortie.
    D = np.around(D)
    D = D.astype(int)
    return D


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
                    np_matrices[i][j] = 1000000000

                # Le noeud courant change de la valeur s'il existe un sommet intermédiaire qui donc possède un
                # circuit de coût plus petit.
                np_matrices[i][j] = min(int(np_matrices[i][j]), int(np_matrices[i][k]) + int(np_matrices[k][j]))

    return np_matrices

print(Dijkstra(matrice_np))
print(Floyd_Warshall(matrice_np))