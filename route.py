from typing import Optional

from fastapi import FastAPI

from pydantic import BaseModel
from sqlalchemy import null

from config_alchemy import Config
from controllers.get_data import get_data
from controllers.post_data import post_data
from controllers.patch_data import UpdateDataModel, patch_data
from controllers.delete_data import delete_data
from utils.get_table_class import get_table_class

app = FastAPI(
    title="Agricole API",
)


def main():
    return Config.database_connection()


print(main())


@app.get('/select/{table}')
def read_data(table: str, skip: int = 0, limit: int = 10, sort_by: Optional[str] = None,
              filters: Optional[str] = None,
              fields: Optional[str] = None):
    return get_data(table, skip, limit, sort_by,
                    filters,
                    fields)


@app.post('/insert/{table}',responses={
    200: {
            "description": "reponse de la requête",
            "content": {
                "application/json": {
                    "example": {"result": "Data has been added."}
                }
            },
        },
    400: {
            "description": "erreur de la requête",
            "content": {
                "application/json": {
                    "example": {"error": "random error"}
                }
            },
    }
})
async def read_data(table: str, data: list[dict] | dict):
    """
    ## Insérer des données dans une table:
    **Param table: string** = nom de la table.

    **Body data: list[dict] ou dict** = données à insérer.

    exemple paramètre table UNITE

    exemple de body data (pas besoin de mettre les colonnes qui auto increment, il est généré automatiquement):
    ```json
    [
        {
            "UN": "kg"
        }
    ]

    ou

    {
        "UN": "kg"
    }
    ```
    ## Résultat:
    **result: dict** = resultat de la requête
    ```json
    {
        "result": "Data has been added."
    }
    ```
    ## Erreur:
    **error: dict** = erreur de la requête
    ```json
    {
        "error": "random error"
    }
    ```
    """
    # traduit le paramètre "table" en une classe SQLAlchemy
    table_class = get_table_class(table)
    if table_class is None:
        return {"error": "Table not found"}
    return post_data(table_class, data)

@app.patch('/update/{table}/{column}={condition}',responses={
    200: {
            "description": "reponse de la requête",
            "content": {
                "application/json": {
                    "example": {
                        "resultat": {
                            "UN": "12345",
                            "ID_ENGRAIS": 3,
                            "NOM_ENGRAIS": "Update"
                        }
                    }
                }
            },
        },
    400: {
            "description": "erreur de la requête",
            "content": {
                "application/json": {
                    "example":
                        {
                            "resultat": [
                                "erreur",
                                [
                                    {}
                                ]
                            ]
                        }
                }
            },
    }
}) # EX => @app.patch('/update/Engrais/ID_ENGRAIS=1')
async def update_data(table: str, column: str, condition: int, data: dict):
    """
    ## Mettre à jour des données dans une table:
    **Param table: string** = nom de la table à modifier.

    **Param column: string** = nom de la colonne pour selecionner la ligne de comparaison.

    **Param condition: int** = valeur a comparer avec la colonne.

    **Body data: dict** = données à modifier.

    exemple paramètre table ENGRAIS

    exemple paramètre column ID_ENGRAIS

    exemple paramètre condition 1 (ID_ENGRAIS = 1)

    exemple de body data:
    ```json
    {
        "NOM_ENGRAIS": "engrais 1"
    }
    ```
    ## Résultat:
    **resultat: dict** = resultat de la requête
    ```json
    {
        "resultat": {
            "NOM_ENGRAIS": "Update",
            "UN": "lol",
            "ID_ENGRAIS": 1
        }
    }
    ```
    """
    table_class = get_table_class(table) # Traduit le paramètre "table" en une classe SQLAlchemy
    if table_class is None: # Si la classe n'est pas trouvée
        return {"message": f"Table non trouvée : {table} n'existe pas"}
    # Si la classe est trouvée on appelle la fonction updateData de config_alchemy.py
    # qui va mettre à jour les données
    result = Config.updateData(table_class, data, column, condition)
    str_variable = "resultat : "
    tuple_as_str = str(result)
    # On transforme le tuple en string pour pouvoir le comparer
    result_print = str_variable + tuple_as_str
    if result_print == "resultat : None":
        print("<<<<<== Échec de la modification, vérifiez si " + column + " a bien une ligne avec pour valeur : " + str(
            condition))
    else :
        print ("resultat : " + result_print)


    return {"resultat": result}




@app.delete('/delete/{table}/{condition_column}/{condition_value}',responses={
    200: {
            "description": "reponse de la requête",
            "content": {
                "application/json": {
                    "example": "Erreur : Donnée non trouvée"
                }
            },
        },
    400: {
            "description": "erreur de la requête",
            "content": {
                "application/json": {
                    "example":"Erreur : Donnée non trouvée"
                }
            },
    }
})
def delete_specific_data(table: str, condition_column: str, condition_value: str):
    """
    ## Supprimer des données dans une table:
    **Param table: string** = nom de la table à modifier.

    **Param condition_column: string** = nom de la colonne pour selectionner la ligne de comparaison.

    **Param condition_value: string** = valeur a comparer avec la colonne.

    exemple paramètre table ENGRAIS

    exemple paramètre condition_column ID_ENGRAIS

    exemple paramètre condition_value 1 (ID_ENGRAIS = 1)

    ## Résultat:
    **result: string** = resultat de la requête
    ```json
    "Donnée supprimée avec succès"
    ```

    ## Erreur:
    **error: string** = erreur de la requête
    ```json
    "Erreur : Donnée non trouvée"
    ```
    """
    return delete_data(table, condition_column, condition_value)
