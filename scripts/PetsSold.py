class MascotasVendidas:
    def __init__(self, data):
        self.data = data

    def contar_mascotas_por_nombre(self):
        nombres_mascotas = {}
        for item in self.data:
            pet_name = item.get('name')
            if pet_name:
                if pet_name in nombres_mascotas:
                    nombres_mascotas[pet_name] += 1
                else:
                    nombres_mascotas[pet_name] = 1
        return nombres_mascotas


if __name__ == "__main__":
    import requests

    base_url = "https://petstore.swagger.io/v2/"
    response = requests.get(base_url + 'pet/findByStatus?status=sold')

    if response.status_code == 200:
        data = response.json()
        mascotas = MascotasVendidas(data)
        resultado = mascotas.contar_mascotas_por_nombre()
        for nombre, cantidad in resultado.items():
            print(f'{nombre}: {cantidad}')
    else:
        print(f'Error al realizar la solicitud. Código de estado: {response.status_code}')
