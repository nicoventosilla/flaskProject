# Proyecto Flask con SQLAlchemy y Flask-Migrate

Esta es una aplicación web desarrollada con Flask que utiliza SQLAlchemy para la gestión de la base de datos y
Flask-Migrate para las migraciones. Incluye la configuración de la base de datos, migraciones y estructura del proyecto.

## Características principales

- Framework: Flask
- ORM: SQLAlchemy
- Migraciones: Flask-Migrate

## Requisitos

Antes de empezar, asegúrate de tener lo siguiente instalado en tu máquina:

- Python 3.x
- pip (gestor de paquetes para Python)
- [Flask](https://flask.palletsprojects.com/en/2.0.x/)
- [SQLAlchemy](https://www.sqlalchemy.org/)

## Instalación

Sigue estos pasos para configurar el proyecto en tu máquina local:

1. Clona el repositorio:
    ```bash
    git clone <URL_DEL_REPOSITORIO>
    cd <NOMBRE_DEL_REPOSITORIO>
    ```

2. Crea un entorno virtual y actívalo:
    ```bash
    python -m venv venv
    source venv/bin/activate  # En Windows usa `venv\Scripts\activate`
    ```

3. Instala las dependencias del proyecto desde el archivo `requirements.txt`:
    ```bash
    pip install -r requirements.txt
    ```

Si hay algún error con las dependencias, asegúrate de que `pip` esté actualizado:

```bash
pip install --upgrade pip
```

## Configuración

Configura las variables de entorno en un archivo `.env` que será usado para conectar tu base de datos. Asegúrate de
reemplazar los valores de ejemplo con tus propios datos:

```env
USER_DB=<tu_usuario>         # Usuario de la base de datos
PASS_DB=<tu_contraseña>      # Contraseña de la base de datos
URL_DB=<url_de_tu_base_de_datos> # URL de la base de datos (por ejemplo, localhost para pruebas locales)
NAME_DB=<nombre_de_tu_base_de_datos> # Nombre de la base de datos que estás usando
```

## Migraciones con Flask-Migrate

Usa los siguientes comandos para manejar las migraciones de la base de datos:

1. Inicializa las migraciones (solo la primera vez):
    ```bash
    flask db init
    ```

2. Crea una nueva migración basada en los cambios en tus modelos:
    ```bash
    flask db migrate -m "Descripción de la migración"
    ```

3. Aplica la migración a la base de datos:
    ```bash
    flask db upgrade
    ```

Opcionalmente, puedes revertir una migración:

```bash
flask db downgrade
```

O marcar el estado actual de la base de datos como la "cabeza" (estado más reciente):

```bash
flask db stamp head
```

## Ejecución

Para ejecutar la aplicación localmente, usa el siguiente comando:

```bash
flask run
```

Esto iniciará un servidor en modo de desarrollo. La aplicación estará disponible en http://127.0.0.1:5000/.

Si la aplicación no arranca, asegúrate de que las dependencias están instaladas correctamente y que tienes el entorno
virtual activado.

## Contribución

Si quieres contribuir a este proyecto, solo tienes que hacer un fork y enviar un pull request con tus cambios.