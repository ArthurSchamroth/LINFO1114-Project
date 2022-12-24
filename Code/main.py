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


def Dijkstra(C: np.matrix):
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
def Floyd_Warshall(C: np.matrix):
    # L'algorithme est constitué de N itération principales;
    # pour chaque itération k, on calcule les plus courts chemins entre toute paire de sommets
    # avec des sommets intermédiaires appartenant uniquement à l'ensemble {1,2,3,...k}
    for k in range(len(C)):
        for i in range(len(C)):
            for j in range(len(C)):
                # ici si le cout est égale à 0,ceci signifie que le cout est 10 exposant 12
                # bien évidemment, à l'exception des elements appartenant à la diagonale.
                if i != j and C[i][j] == 0:
                    C[i][j] = 1000000000

                # Le noeud courant change de la valeur s'il existe un sommet intermédiaire qui donc possède un
                # circuit de coût plus petit.
                C[i][j] = min(int(C[i][j]), int(C[i][k]) + int(C[k][j]))
    D = C
    return D


def Bellman_Ford(C: np.matrix):
    # N = Nombre de noeuds du graphe
    N = C.shape[0]
    nv_matrice = []
    # Mise à jour de la matrice pour qu'elle transforme les 0 en valeur infinie sauf pour les noeuds envers eux-même
    for i in range(len(C)):
        ligne = []
        for j in range(len(C[i])):
            if i != j:
                if C[i][j] == 0:
                    ligne.append(float("inf"))
                else:
                    ligne.append(C[i][j])
            else:
                ligne.append(0)
        nv_matrice.append(ligne)

    # Création de la matrice des distances minimales.
    # Les distances initiales sont celles de la matrice d'entrée.
    D = np.array(nv_matrice)

    # Répéter l'algorithme N-1 fois
    for i in range(N - 1):
        # Mettre à jour les distances minimales en prenant en compte tous les chemins possibles
        for j in range(N):
            for k in range(N):
                if D[j, i] != np.inf and D[i, k] != np.inf:
                    D[j, k] = min(D[j, k], D[j, i] + D[i, k])

    return D


if __name__ == '__main__':
    matrice_lecture = []
    lecture = "  | A, B, C, D, E, F, G, H, I, J \n"
    with open("../data.csv") as file:
        lines = file.readlines()
        for i in range(len(lines)):
            ligne = []
            if i == 0:
                continue
            else:
                for j in lines[i].split(", "):
                    ligne.append(int(j))
            matrice_lecture.append(ligne)
    for i in range(len(matrice_lecture)):
        for j in range(len(matrice_lecture[i])):
            if i == 0 and j == 0 and matrice_lecture[i][j] == 1000000000000:
                lecture += "A | ∞, "
            elif i == 0 and j == 0 and matrice_lecture[i][j] != 1000000000000:
                lecture = lecture + "A | " + str(matrice_lecture[i][j]) + ", "
            elif i == 1 and j == 0 and matrice_lecture[i][j] == 1000000000000:
                lecture += "B | ∞, "
            elif i == 1 and j == 0 and matrice_lecture[i][j] != 1000000000000:
                lecture = lecture + "B | " + str(matrice_lecture[i][j]) + ", "
            elif i == 2 and j == 0 and matrice_lecture[i][j] == 1000000000000:
                lecture += "C | ∞, "
            elif i == 2 and j == 0 and matrice_lecture[i][j] != 1000000000000:
                lecture = lecture + "C | " + str(matrice_lecture[i][j]) + ", "
            elif i == 3 and j == 0 and matrice_lecture[i][j] == 1000000000000:
                lecture += "D | ∞, "
            elif i == 3 and j == 0 and matrice_lecture[i][j] != 1000000000000:
                lecture = lecture + "D | " + str(matrice_lecture[i][j]) + ", "
            elif i == 4 and j == 0 and matrice_lecture[i][j] == 1000000000000:
                lecture += "E | ∞, "
            elif i == 4 and j == 0 and matrice_lecture[i][j] != 1000000000000:
                lecture = lecture + "E | " + str(matrice_lecture[i][j]) + ", "
            elif i == 5 and j == 0 and matrice_lecture[i][j] == 1000000000000:
                lecture += "F | ∞, "
            elif i == 5 and j == 0 and matrice_lecture[i][j] != 1000000000000:
                lecture = lecture + "F | " + str(matrice_lecture[i][j]) + ", "
            elif i == 6 and j == 0 and matrice_lecture[i][j] == 1000000000000:
                lecture += "G | ∞, "
            elif i == 6 and j == 0 and matrice_lecture[i][j] != 1000000000000:
                lecture = lecture + "G | " + str(matrice_lecture[i][j]) + ", "
            elif i == 7 and j == 0 and matrice_lecture[i][j] == 1000000000000:
                lecture += "H | ∞, "
            elif i == 7 and j == 0 and matrice_lecture[i][j] != 1000000000000:
                lecture = lecture + "H | " + str(matrice_lecture[i][j]) + ", "
            elif i == 8 and j == 0 and matrice_lecture[i][j] == 1000000000000:
                lecture += "I | ∞, "
            elif i == 8 and j == 0 and matrice_lecture[i][j] != 1000000000000:
                lecture = lecture + "I | " + str(matrice_lecture[i][j]) + ", "
            elif i == 9 and j == 0 and matrice_lecture[i][j] == 1000000000000:
                lecture += "J | ∞, "
            elif i == 9 and j == 0 and matrice_lecture[i][j] != 1000000000000:
                lecture = lecture + "J | " + str(matrice_lecture[i][j]) + ", "
            elif j == len(matrice_lecture[i]) - 1 and matrice_lecture[i][j] == 1000000000000:
                lecture += "∞ \n"
            elif j == len(matrice_lecture[i]) - 1 and matrice_lecture[i][j] != 1000000000000:
                lecture = lecture + str(matrice_lecture[i][j]) + " \n"
            elif j != len(matrice_lecture[i]) - 1 and matrice_lecture[i][j] == 1000000000000:
                lecture += "∞, "
            elif j != len(matrice_lecture[i]) - 1 and matrice_lecture[i][j] != 1000000000000:
                lecture = lecture + str(matrice_lecture[i][j]) + ", "

    print("Voici la lecture de la matrice issue du CSV : ")
    print(lecture)
    print("Voici la matrice issue de Dijkstra : ")
    print(Dijkstra(matrice_np))
    print("Voici la matrice issue de Floyd-Warshall : ")
    print(Floyd_Warshall(matrice_np))
    print("Voici la matrice issue de Bellman-Ford : ")
    print(Bellman_Ford(matrice_np))
