from utils.get_table_class import get_table_class
def get_data(table:str):
    class_table = get_table_class(table)
    print(class_table)
    return {"lala":1}
