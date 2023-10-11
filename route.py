from fastapi import FastAPI

from config_alchemy import Config
from controllers.get_data import get_data
from controllers.post_data import post_data
from controllers.patch_data import patch_data
from controllers.delete_data import delete_data

app = FastAPI()


def main():
    print(Config.database_connection())


@app.get('/select/{table}')
def read_data(table: str):
    return get_data(table)


@app.post('/insert/{table}')
def read_data(table: str):
    return post_data(table)


@app.patch('/update/{table}')
def read_data(table: str):
    return patch_data(table)


@app.delete('/delete/{table}')
def read_data(table: str):
    return delete_data(table)
