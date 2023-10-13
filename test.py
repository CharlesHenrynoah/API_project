# Remplacez 'votre_chemin_vers_config' par le chemin d'accès réel à votre fichier de configuration
from config_alchemy import Config  # Assurez-vous que le chemin est correct

# Test de la connexion à la base de données
print(Config.database_connection())
