from sqlalchemy import func
# toutes les opérations de comparaison possibles
COMPARATORS = {
    '==': '__eq__',
    '>=': '__ge__',
    '<=': '__le__',
    '>': '__gt__',
    '<': '__lt__'
}

# permet de récupérer le nom de la colonne, l'opérateur et la valeur d'un filtre
def parse_filter(filter_str: str):
    for comp, comp_func in COMPARATORS.items():
        if comp in filter_str:
            field, value = filter_str.split(comp)
            return field.strip().upper(), comp_func, value.strip()
    return None, None, None

# permet de récupérer les clauses de filtres
# exemple : apply_filters("ID_CULTURE==1,DATE_DEBUT>=2021-01-01", Culture)
# renvoie [Culture.ID_CULTURE == 1, Culture.DATE_DEBUT >= '2021-01-01']
def apply_filters(filters, class_to_select):
    if filters:
        filter_clauses = []
        for filter_str in filters.split(','):
            column_name, op_method, value = parse_filter(filter_str)
            if column_name:
                column = getattr(class_to_select, column_name)
                if column:
                    filter_method = getattr(column, op_method)
                    filter_clauses.append(filter_method(value if isinstance(value, str) else func.trim(value)))
            else:
                raise Exception("Il manque le nom de la colonne.")

        return filter_clauses

    return None
