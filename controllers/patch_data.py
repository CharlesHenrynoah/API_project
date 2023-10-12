# controllers/patch_data.py
# patch.py

from fastapi import HTTPException

from pydantic import BaseModel


class UpdateDataModel(BaseModel):
    NOM_ENGRAIS: str

def patch_data(table: str, condition: int, column: str, data: UpdateDataModel):
    updated_data = {"message": "Mise à jour réussie", column: data.NOM_ENGRAIS}
    return updated_data