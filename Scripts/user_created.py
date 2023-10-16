import requests
import json

# Definir la URL base de la API de Petstore
base_url = 'https://petstore.swagger.io/v2/'

# Función para consultar usuario nombre de usuario (username)
def consultar_usuario(username):
    url = base_url + f'user/{username}'

    response = requests.get(url)

    if response.status_code == 200:
        usuario = response.json()
        print(f'Información del usuario creado:')
        print(f'Id del usuario: {usuario["id"]}')
        print(f'Nombre de usuario: {usuario["username"]}')
        print(f'Nombre completo: {usuario["firstName"]} {usuario["lastName"]}')
        print(f'Correo electrónico: {usuario["email"]}')
    else:
        print(f'Error al consultar el usuario. Código de estado: {response.status_code}')

if __name__ == "__main__":
    # Leer los datos del usuario desde el archivo JSON
    with open('new_user.json', 'r') as file:
        usuario = json.load(file)

    # Obtener el nombre de usuario del archivo JSON
    username = usuario['username']

    # Consultar el usuario por su nombre de usuario
    consultar_usuario(username)