from typing import Optional
from re import findall

from starlette import status
from starlette.responses import JSONResponse

from utils.get_table_class import get_table_class
from config_alchemy import Config, logCompteur
from classes.Culture import Culture
from utils.sanitize import sanitize



# fonction pour récupérer les données d'une table
def get_data(table: str, skip: int = 0, limit: int = 1, sort_by: Optional[str] = None,
             filters: Optional[str] = None,
             fields: Optional[str] = None):
    sanitized_sort = None
    sanitized_fields = None
    sanitized_filters = None
    # récupère la classe de la table
    class_table = get_table_class(sanitize(table))

    # si la table n'existe pas, retourne un message d'erreur
    if filters:
        sanitized_filters = sanitize(filters)
    if fields:
        sanitized_fields = sanitize(fields.upper())
    if sort_by:
        sanitized_sort = sanitize(sort_by.upper())
    if class_table is None:
        return JSONResponse(status_code=status.HTTP_404_NOT_FOUND,
                            content={"message": f"Table non trouvée : {table} n'existe pas"})

    # récupère les données de la table
    result = Config.selectData(class_table,  skip, limit, sanitized_filters, sanitized_sort, sanitized_fields)
    return result
