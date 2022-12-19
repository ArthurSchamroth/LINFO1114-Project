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
            relations = relations.astype(int)
            liens.append(relations)
    matrice_np = np.array(liens)


def Dijkstra(np_matrice):
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

    depart = "A"
    noeuds_visites = [{depart: 0}]
    noeud_actuel = depart
    noeud_final = "F"

    if noeud_actuel != noeud_final:
        print(noeud_actuel)
        cle_noeud_visite = []
        noeuds_non_visites = []
        for i in noeuds_visites:
            cle_noeud_visite.append(list(i.keys())[0])
        print("Noeuds visités début du tour : ", )
        for i in matrice:
            if list(i.keys())[0] != depart:
                noeuds_non_visites.append(list(i.keys())[0])
        print("Noeuds non visités au début de ce tour : ", noeuds_non_visites)
        for i in matrice:
            if list(i.keys())[0] == noeud_actuel:
                min_key = None
                min_value = float('inf')
                for key, value in i.items():
                    print("Noeuds proches du noeud : ", noeud_actuel, ", ", value)
                    for key_i, value_i in value.items():
                        print("test", key_i)
                        if value_i < min_value and key_i not in cle_noeud_visite:
                            min_key = key_i
                            min_value = value_i
                somme_actuel = list(noeuds_visites[-1].values())[0]
                nouvelle_somme = somme_actuel + min_value
                noeud_actuel = min_key
                print(noeud_actuel)
                noeuds_visites.append({noeud_actuel: nouvelle_somme})
                cle_noeud_visite.append(noeud_actuel)
                print("Distance parcourue : ", noeuds_visites)
                print("Noeud actuel : ", noeud_actuel)
                noeuds_non_visites.remove(noeud_actuel)
                print("Noeuds non visités a la fin du tour : ", noeuds_non_visites)
                print("teeeeeeest", noeud_actuel)
    else:
        print("ok")

Dijkstra(matrice_np)