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


def get_table_class(table_name):
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
    return table_mapping.get(table_name, None)



