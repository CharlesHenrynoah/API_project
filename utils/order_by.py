from sqlalchemy import desc, asc

# permet de récupérer les clauses de tri
# exemple : order_by("ID_CULTURE,-DATE_DEBUT", Culture)
# renvoie [Culture.ID_CULTURE, Culture.DATE_DEBUT.desc()]
def order_by(sort_by, class_to_select):
    order_by_clauses = []
    if sort_by:
        list_sort = sort_by.split(',')
        for field in list_sort:
            if field.startswith('-'):
                column = getattr(class_to_select, field[1:])
                if column:
                    order_by_clauses.append(desc(column))
            else:
                column = getattr(class_to_select, field)
                if column:
                    order_by_clauses.append(asc(column))
    return order_by_clauses
