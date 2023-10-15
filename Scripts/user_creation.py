import requests
import json

# Definir la URL base de la API de Petstore
base_url = 'https://petstore.swagger.io/v2/'

# Función para crear un usuario a partir de un archivo JSON
def crear_usuario_desde_json(json_file):
    url = base_url + 'user'

    # Leer los datos del archivo JSON
    with open(json_file, 'r') as file:
        usuario = json.load(file)

    headers = {'Content-Type': 'application/json'}

    response = requests.post(url, data=json.dumps(usuario), headers=headers)

    if response.status_code == 200:
        print(f'Usuario creado con éxito. ID: {usuario["id"]}')
    else:
        print(f'Error al crear el usuario. Código de estado: {response.status_code}')

if __name__ == "__main__":
    # Ruta al archivo JSON con los datos del usuario
    json_file = 'new_user.json'  # Reemplaza con la ruta correcta a tu archivo JSON.

    # Crear un nuevo usuario desde el archivo JSON
    crear_usuario_desde_json(json_file)