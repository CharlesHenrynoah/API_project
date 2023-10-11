# controllers/patch_data.py
# patch.py

from fastapi import HTTPException

from pydantic import BaseModel


class UpdateDataModel(BaseModel):
    NOM_ENGRAIS: str

def patch_data(table: str, condition: int, data: UpdateDataModel):
    updated_data = {"message": "Mise à jour réussie", "NOM_ENGRAIS": data.NOM_ENGRAIS}
    return updated_data