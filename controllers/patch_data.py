# controllers/patch_data.py
# patch.py

from fastapi import HTTPException

from pydantic import BaseModel

# creez une classe UpdateDataModel qui herite de BaseModel
class UpdateDataModel(BaseModel):
    UN: str
    NOM_ENGRAIS: str

# creez une fonction patch_data qui prend en parametre:
# - table: str
# - condition: int
# - column: str
# - data: UpdateDataModel
# et qui retourne un dictionnaire avec le message "Mise à jour réussie" et les données mises à jour
# grace à la fonction updateData de la classe Config
def patch_data(table: str, condition: int, column: str, data: UpdateDataModel):
    print("patch")
    updated_data = {"message": "Mise à jour réussie", column: data.NOM_ENGRAIS}
    print(updated_data)
    return updated_data