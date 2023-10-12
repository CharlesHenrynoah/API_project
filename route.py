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


from fastapi import FastAPI

app = FastAPI()

@app.patch('/update/{table}/{column}={condition}')
async def update_data(table: str, column: str, condition: int, data: dict):
    table_class = get_table_class(table) # Traduit le paramètre "table" en une classe SQLAlchemy
    if table_class is None: # Si la classe n'est pas trouvée
        return {"message": f"Table non trouvée : {table} n'existe pas"}
    result = Config.updateData(table_class, data, column, condition)
    return {"message": result}




@app.delete('/delete/{table}')
def read_data(table: str):
    return delete_data(table)
