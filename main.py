import fastapi
import uvicorn
import pydantic

# Créez un tableau (liste) d'exemple
my_array = [1, 2, 3, 4, 5]

# Concaténez les éléments en une chaîne de caractères et imprimez
array_as_string = " ".join(map(str, my_array))
print(array_as_string)
