import csv

distances = []
# Données : Un fichier .csv
# Résultat : Une matrice M de taille N * N qui contient les distances entre chaque noeud.

with open('../data.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

    for i in csv_reader:
        distances.append(i)


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
                # Le noeud courant change de la valeur s'il existe un sommet intermédiaire qui donc possède un circuit de coût plus petit.
                np_matrices[i][j] = min(int(np_matrices[i][j]), int(np_matrices[i][k]) + int(np_matrices[k][j]))

    return np_matrices


print(Floyd_Warshall(distances))