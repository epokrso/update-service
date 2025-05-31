import os

# Chemin vers le bureau de l'utilisateur
bureau = os.path.join(os.path.expanduser("~"), "Desktop")

# Nom du fichier
nom_fichier = "ordre_executer.txt"

# Chemin complet du fichier
chemin_fichier = os.path.join(bureau, nom_fichier)

# Contenu du fichier
contenu = "Ceci est un fichier ordre à exécuter."

# Création et écriture dans le fichier
with open(chemin_fichier, "w", encoding="utf-8") as f:
    f.write(contenu)
