from config import Settings
from entites.engrais.engrais_api import engrais_select, engrais_insert, engrais_update, engrais_delete


class tkt:
    @staticmethod
    def ttkt():
        requete_execute = engrais_select() #MODIFIER "engrais_delete" PAR LA FONCTIONS VOULUS (ex: engrais_select, engrais_insert, engrais_update, engrais_delete)
        result = Settings.requete_global(requete_execute)
        return result


result = tkt.ttkt()
