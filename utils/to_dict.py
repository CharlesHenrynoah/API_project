import datetime
import decimal


def to_dict(row, fields_to_get):
    dict_result = {}
    for n in range(len(row)):
        value = row[n]
        if isinstance(value, datetime.date):
            value = value.strftime('%Y-%m-%d')
        elif isinstance(value, str):
            value = value.strip()
        elif isinstance(value, decimal.Decimal):
            value = float(value)
        dict_result[fields_to_get[n].name] = value
    return dict_result
