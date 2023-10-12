from utils.get_table_class import get_table_class
from config_alchemy import Config


def post_data(table, data: list[dict] | dict):
    result = Config.insertData(table, data)
    return result