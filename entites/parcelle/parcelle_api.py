from config import Settings

#fetch all parcelles
def fetch_all_parcelles():
    return Settings.test_database_connection('SELECT * FROM "PARCELLE"')

#fetch one parcelle
def fetch_one_parcelle(id):
    return Settings.test_database_connection(f'SELECT * FROM "PARCELLE" WHERE "NO_PARCELLE" = {id}')

#add one parcelle
def add_one_parcelle(surface, nom_parcelle, coordonnees):
    return Settings.test_database_connection(f'INSERT INTO public."PARCELLE" ("SURFACE", "NOM_PARCELLE", "COORDONNEES") VALUES ({surface}, \'{nom_parcelle}\', \'{coordonnees}\')')

print(fetch_all_parcelles())