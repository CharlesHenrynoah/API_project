# controllers/patch_data.py
# patch.py

from fastapi import HTTPException

from pydantic import BaseModel


class UpdateDataModel(BaseModel):
    UN: str
    NOM_ENGRAIS: str

def patch_data(table: str, condition: int, column: str, data: UpdateDataModel):
    print("patch")
    updated_data = {"message": "Mise à jour réussie", column: data.NOM_ENGRAIS}
    print(updated_data)
    return updated_data