import requests

base_url = "https://petstore.swagger.io/v2/"  # Reemplaza esto con la URL real que estás utilizando

# Realiza una solicitud HTTP a la URL con status=sold
response = requests.get(base_url + 'pet/findByStatus?status=available')

if response.status_code == 200:  # Verifica que la solicitud haya tenido éxito
    data = response.json()  # Convierte la respuesta JSON en un diccionario de Python

    # Itera a través de los elementos en la respuesta y imprime el id y el name de cada uno
    for item in data:
        pet_id = item.get('id', 'No se encontró ID')
        pet_name = item.get('name', 'No se encontró nombre')
        print(f'ID: {pet_id}, Name: {pet_name}')

else:
    print(f'Error al realizar la solicitud. Código de estado: {response.status_code}')