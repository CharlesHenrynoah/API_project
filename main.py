import json
from classes.Culture import Culture
from classes.Date_table import DateTable
from classes.Engrais import Engrais
from classes.Element_chimiques import ElementChimiques
from classes.Epandre import Epandre
from classes.Parcelle import Parcelle
from classes.Posseder import Posseder
from classes.Unite import Unite
from classes.Production import Production
from config_alchemy import Config


def main():
    return Config.database_connection()
def select_test():
    result = Config.selectData(Parcelle)
    return result

def insert_test():
   Config.insertData(Parcelle, [{"NO_PARCELLE": 1, "SURFACE":100, "NOM_PARCELLE": "lololo", "COORDONNEES": "edededed"}])

print(main())

print(select_test())
