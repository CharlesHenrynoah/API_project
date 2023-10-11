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

condition = 7

data = {
    "UN": "UPDATE3",
    "NOM_ENGRAIS": "3UPDATE"
}
def main():
    return Config.database_connection()

task = input("select / insert / update")

if task == "select":
    def select_test():
        result = Config.selectData(Engrais)
        return result
elif task == "insert":
    def insert_test():
        result = Config.insertData(Engrais, data)
        return result
elif task == "update":
    def update_test():
        result = Config.updateData(Engrais, data, condition)
        return result





print(main())
#print(select_test())
#print(insert_test())
print(update_test())