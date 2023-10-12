COMPARATORS = {
    '==': '__eq__',
    '>=': '__ge__',
    '<=': '__le__',
    '>': '__gt__',
    '<': '__lt__'
}

def parse_filter(filter_str: str):
    for comp, comp_func in COMPARATORS.items():
        if comp in filter_str:
            field, value = filter_str.split(comp)
            return field.strip(), comp_func, value.strip()
    return None, None, None

def apply_filters(filters, class_to_select):
    if filters:
        filter_clauses = []
        for filter_str in filters.split(','):
            column_name, op_method, value = parse_filter(filter_str)
            if column_name:
                column = getattr(class_to_select, column_name, None)
                if column:
                    filter_method = getattr(column, op_method)
                    filter_clauses.append(filter_method(value))

        return filter_clauses
    return None