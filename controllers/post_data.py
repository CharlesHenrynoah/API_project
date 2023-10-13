from utils.get_table_class import get_table_class
from config_alchemy import Config

# creez une fonction post_data qui prend en parametre:
# - table: str
# - data: list[dict] | dict
# et qui retourne le résultat de l'insertion grace à la fonction insertData de la classe Config
def post_data(table, data: list[dict] | dict):
    result = Config.insertData(table, data)
    return result