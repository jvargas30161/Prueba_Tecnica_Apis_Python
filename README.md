# Proyecto Python con Métodos POST y GET

Este proyecto en Python se centra en interactuar con la API de Petstore usando 
métodos HTTP POST y GET. También incluye una clase `MascotasVendidas` que permite 
contar las mascotas vendidas por nombre. Para la ejecución de las pruebas automáticas será 
necesario tener inslado Pyhon.

## Contenido
* [Librerías](#librerías)
* [Documentación de API](#Documentación de API)
* [IDE](#ide)
* [Scripts](#Scripts)
* [Contribuciones](#Contribuciones)

## Librerías
- Requests
- JSON
- 
## Documentación de API
- https://petstore.swagger.io/#/pet/findPetsByStatus

## IDE
Para este proyecto se ha usado [IntelliJ](https://www.jetbrains.com/idea/)

### Plugins recomendados para intelliJ

- [SonarLint](https://plugins.jetbrains.com/plugin/7973-sonarlint) - Valida código python.

### Ejecución desde IDE de un test en concreto

Colocar el ratón sobre el scenario a ejecutar y click derecho "Run"

### Scripts

 La carpeta scripts contiene los ficheros:

- user_creation.py
  - 
  - Contiene código python para ejecución de creación de usaurio método POST.
   
- new_user.json
  - 
- Contiene archivo json, con la data para la creación del usuario método POST.

- user_created.py
  - 
- Contiene código python para ejecución de la búsqueda del usuario creado método GET.

- find_by_status.py
  - 
- Contiene código python para ejecución de la búsqueda por ID y NAME de mascotas por estado SOLD.
- 
- find_by_status.py
  -
- Contiene clase python con constructor donde se obtendrá el total de mascotas con mismo nombre.

- Contribuciones
  - 
- Las contribuciones son bienvenidas. Si deseas mejorar este proyecto, no dudes en crear un pull request.