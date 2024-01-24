# Weather API

API that provides weather historical data for specific location.

[![Built with Cookiecutter Django](https://img.shields.io/badge/built%20with-Cookiecutter%20Django-ff69b4.svg?logo=cookiecutter)](https://github.com/cookiecutter/cookiecutter-django/)
[![Black code style](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)

License: MIT

## Basic Commands

You can build the Docker images by executing the following command:

```
docker compose build --no-cache
```

Containers can be launched by executing the following command:

```
docker compose build up -d
```

### Swagger documentation
Please, follow: http://127.0.0.1:8000/api/docs/


### Setting Up Your Users

- To create a **superuser account**, use this command:

      docker compose run --rm django python manage.py createsuperuser

For convenience, you can keep your normal user logged in on Chrome and your superuser logged in on Firefox (or similar), so that you can see how the site behaves for both kinds of users.

## Deployment

The following details how to deploy this application.

### Docker

See detailed [cookiecutter-django Docker documentation](http://cookiecutter-django.readthedocs.io/en/latest/deployment-with-docker.html).

### Settings

Moved to [settings](http://cookiecutter-django.readthedocs.io/en/latest/settings.html).
