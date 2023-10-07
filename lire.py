# Ouvrir un fichier en mode lecture
with open('index.txt', 'r') as fichier:
    contenu = fichier.read()
    # Vous pouvez maintenant manipuler le contenu du fichier

# Le fichier se ferme automatiquement après la sortie du bloc "with"
