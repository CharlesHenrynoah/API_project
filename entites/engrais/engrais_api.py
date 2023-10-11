# engrais_api.py

from config import Settings

def engrais_select():
    requete_engrais_select = 'SELECT * FROM public."ENGRAIS";'
    resultat_select = Settings.requete_global(requete_engrais_select)
    return requete_engrais_select

def engrais_insert():
    UN = "test"
    NOM_ENGRAIS = "ezf"

    requete_engrais_insert = f'INSERT INTO public."ENGRAIS2"("UN", "NOM_ENGRAIS") VALUES (\'{UN}\', \'{NOM_ENGRAIS}\');'

    resultat_insert = Settings.requete_global(requete_engrais_insert)
    print(resultat_insert)
    return requete_engrais_insert


def engrais_update():
    ID_ENGRAIS_ANCIEN = 2
    UN_UPDATE = "UNupdate"

    requete_engrais_update = f'UPDATE public."ENGRAIS" SET "UN" = \'{UN_UPDATE}\' WHERE "ID_ENGRAIS" = \'{ID_ENGRAIS_ANCIEN}\';'

    resultat_update = Settings.requete_global(requete_engrais_update)
    print(resultat_update)
    return requete_engrais_update


def engrais_delete():
    ID_ENGRAIS_DELETE = 2

    requete_engrais_delete = f'DELETE from public."ENGRAIS" WHERE "ID_ENGRAIS" = \'{ID_ENGRAIS_DELETE}\';'

    resultat_delete = Settings.requete_global(requete_engrais_delete)
    print(resultat_delete)
    return requete_engrais_delete