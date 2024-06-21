# LMNP
## Run project
docker compose up
## Create User
docker exec -it lmnp_web_1  python manage.py createsuperuser
docker exec -it lmnp_web_1  python manage.py makemigrations apps
docker exec -it lmnp_web_1  python manage.py migrate
