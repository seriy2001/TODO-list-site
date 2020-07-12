# TODO-list-site

### Setup

first, run migrations using the command:

``docker-compose run web python manage.py migrate``

then create super user in order to access admin page

 ``docker-compose run web python manage.py createsuperuser``
 
 finally, run docker-compose with command:
 
 ``docker-compose up``
