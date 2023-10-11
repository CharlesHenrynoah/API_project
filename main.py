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

#    "UN": "UPDATE4",
#    "NOM_ENGRAIS": "4UPDATE"

data = {
    "UN": "UPDATE4",
}
def main():
    return Config.database_connection()

#table = input("Selectionner table")
task = input("select / insert / update / delete")

#if table == "Engrais":

table = Engrais #test

if task == "select":
    def select_test():
        result = Config.selectData(table)
        return result
elif task == "insert":
    def insert_test():
        result = Config.insertData(table, data)
        return result
elif task == "update":
    def update_test():
        condition = int(input("Donner l'ID lié au row à delete"))
        result = Config.updateData(table, data, condition)
        return result
elif task == "delete":
    def delete_test():
        condition = int(input("Donner l'ID lié au row à delete"))
        result = Config.deleteData(table, condition)
        return result



print(main())

if task == "select":
    print(select_test())
elif task == "insert":
    print(insert_test())
elif task == "update":
    print(update_test())
elif task == "delete":
    print(delete_test())