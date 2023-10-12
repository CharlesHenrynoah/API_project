from fastapi import FastAPI

from config_alchemy import Config
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
def read_data(table: str):
    return post_data(table)


@app.patch('/update/{table}/{condition}')
async def update_data(table: str, condition: int, data: dict):
    table_class = get_table_class(table)
    if table_class is None:
        return {"message": "Table non trouvée"}
    result = Config.updateData(table_class, data, condition)
    print(table_class)
    print(data)
    print(condition)
    print(result)
    return {"message": result}





@app.delete('/delete/{table}')
def read_data(table: str):
    return delete_data(table)
