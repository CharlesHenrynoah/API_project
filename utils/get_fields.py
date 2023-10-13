def get_fields(fields, class_to_select):
    # Gestion des champs
    # Si fields est vide, on retourne la classe
    # Sinon, on retourne les champs demandés
    if fields:
        return [getattr(class_to_select, field.strip()) for field in fields.split(',')]
    else:
        return [class_to_select]