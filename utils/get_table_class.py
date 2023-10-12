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

# permet de récupérer la classe d'une table en fonction de son nom
# exemple : get_table_class("Culture") renvoie la classe Culture
def get_table_class(table_name):
    name_table = f"{table_name[0].upper()}{table_name[1:].lower()}"
    table_mapping = {
        "Culture": Culture,
        "Date_table": DateTable,
        "Engrais": Engrais,
        "Element_chimiques": ElementChimiques,
        "Epandre": Epandre,
        "Parcelle": Parcelle,
        "Posseder": Posseder,
        "Unite": Unite,
        "Production": Production
    }
    return table_mapping.get(name_table, None)



