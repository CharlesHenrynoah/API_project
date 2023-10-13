def get_fields(fields, class_to_select):
    if fields:
        return [getattr(class_to_select, field.strip()) for field in fields.split(',')]
    else:
        return [class_to_select]