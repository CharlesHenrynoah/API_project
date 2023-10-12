from sqlalchemy.orm import Session
from config_alchemy import Config
from utils.get_table_class import get_table_class


def delete_data(table: str, condition_column: str, condition_value: str):
    # Utilisez la fonction pour obtenir la classe
    table_class = get_table_class(table)

    if table_class is None:  # Vérifiez si la classe existe
        return "Table non reconnue"

    with Session(Config.engine) as session:
        # Utilisation de filter_by pour appliquer des conditions de filtrage
        item_to_delete = session.query(table_class).filter_by(
            **{condition_column: condition_value}).first()

        if item_to_delete is not None:
            session.delete(item_to_delete)
            session.commit()
            return "Donnée supprimée avec succès"
        else:
            return "Erreur : Donnée non trouvée"
