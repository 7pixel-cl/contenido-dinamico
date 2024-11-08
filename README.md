# Employee List Project

Este proyecto es una aplicación web simple que muestra una lista de empleados en un formato de tarjetas utilizando Bootstrap.



![image](https://github.com/user-attachments/assets/24c70c1f-e96b-4d71-96c2-1989818ae4fa)



## Tecnologías Utilizadas

- Python
- Django
- Bootstrap 4.5.2

## Instalación

1. Clona el repositorio:

   ```bash
   git https://github.com/7pixel-cl/contenido-dinamico.git
   cd tu-repositorio
   ```

2. Crea y activa un entorno virtual:

   ```bash
   python -m venv env
   source env/bin/activate  # En Windows usa `env\Scripts\activate`
   ```

3. Instala las dependencias:

   ```bash
   pip install -r requirements.txt
   ```

4. Ejecuta las migraciones de la base de datos:

   ```bash
   python manage.py migrate
   ```

5. Inicia el servidor de desarrollo:

   ```bash
   python manage.py runserver
   ```

6. Abre tu navegador y ve a `http://127.0.0.1:8000/` para ver la aplicación en funcionamiento.

## Estructura del Proyecto

- `views.py`: Contiene la vista para mostrar la lista de empleados.
- `templates/empleados.html`: Plantilla HTML que utiliza Bootstrap para mostrar la lista de empleados en formato de tarjetas.

## Contribuciones

Las contribuciones son bienvenidas. Por favor, abre un issue o envía un pull request para discutir cualquier cambio que te gustaría hacer.

## Licencia

Este proyecto está bajo la Licencia MIT. Consulta el archivo `LICENSE` para más detalles.
