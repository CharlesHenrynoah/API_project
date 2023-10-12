from fastapi import FastAPI
from pydantic import BaseModel

from config_alchemy import Config
from controllers.get_data import get_data
from controllers.post_data import post_data
from controllers.patch_data import patch_data
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


@app.patch('/update/{table}')
def read_data(table: str):
    return patch_data(table)


@app.delete('/delete/{table}')
def read_data(table: str):
    return delete_data(table)
