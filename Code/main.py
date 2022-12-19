import numpy as np

# Traitement de la matrice depuis le csv
with open("../data.csv") as file:
    lines = file.readlines()
    relations_matrice = {}
    liens = []
    relations_array = []
    matrice = []
    for i in range(len(lines)):
        if i == 0:
            for j in lines[i].strip("\n").split(", "):
                relations_matrice[j] = []
        else:
            relations = lines[i].strip("\n").split(", ")
            relations = np.array(relations)
            relations = relations.astype(int)
            liens.append(relations)
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

    for i in matrice:
        for j in i:
            if i[j][j] == 0:
                del i[j][j]
    for i in matrice:
        print(i)
