from fastapi import FastAPI

from pydantic import BaseModel
from sqlalchemy import null

from config_alchemy import Config, increment_and_log_api_counter
from controllers.get_data import get_data
from controllers.post_data import post_data
from controllers.patch_data import UpdateDataModel, patch_data
from controllers.delete_data import delete_data
from utils.get_table_class import get_table_class

app = FastAPI()


def main():
    print(Config.database_connection())


@app.get('/select/{table}')
def read_data(table: str):
    return get_data(table)


@app.post('/insert/{table}')
async def read_data(table: str, data: list[dict] | dict):
    '''
    :param table: string


    :body data: list[dict] ou dict


    :return: dict
    '''
    table_class = get_table_class(table)
    if table_class is None:
        return {"error": "Table not found"}
    return post_data(table_class, data)


from fastapi import FastAPI

app = FastAPI()

@app.patch('/update/{table}/{column}={condition}') # EX => @app.patch('/update/Engrais/ID_ENGRAIS=1')
async def update_data(table: str, column: str, condition: int, data: dict):
    '''

    :param table: 
    :param column:
    :param condition:
    :param data:
    :return:
    '''
    table_class = get_table_class(table) # Traduit le paramètre "table" en une classe SQLAlchemy
    if table_class is None: # Si la classe n'est pas trouvée
        return {"message": f"Table non trouvée : {table} n'existe pas"}
    result = Config.updateData(table_class, data, column, condition)
    str_variable = "resultat : "
    tuple_as_str = str(result)
    result_print = str_variable + tuple_as_str
    if result_print == "resultat : None":
        print("<<<<<== Échec de la modification, vérifiez si " + column + " a bien une ligne avec pour valeur : " + str(
            condition))
    else :
        increment_and_log_api_counter('PATCH')
        print ("resultat : " + result_print)


    return {"resultat": result}




@app.delete('/delete/{table}')
def read_data(table: str):
    return delete_data(table)
