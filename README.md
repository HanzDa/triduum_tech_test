# Prueba Técnica Triduum
Prueba Técnica FullStack para el proceso de selección
## Pasos para compilar el programa:
1. Instalar docker, docker compose y construir la imagen del proyecto
2. ``docker compose build``
3. Usar el comando custom **run.sh** para levantar los servicios, o en su defecto ejecutar sus propios pasos manuales para ejecutar el servicio
4. `. run.sh` - Este comando levanta un contenedor con la base de datos en postgres y el servicio web de Django corriendo en el puerto 8000
5. `. run.sh bash` - Este comando ejecuta el bash de Django **web**. Usarlo para crear un superusuario y cargar los fixtures.json y poblar así la base de datos `python manage.py loaddata fixtures/*.json`
6. Revisar `<localhost:8000>/redoc/` y `<localhost:8000>/swagger/` para visualizar la documentación de la API

### Creado:
-  2023-07-03
