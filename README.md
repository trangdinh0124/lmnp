# lmnp
## Run project
docker compose up
## Create user
docker exec -it lmnp_web_1 python manage.py makemigrations apps
docker exec -it lmnp_web_1 python manage.py migrate
docker exec -it lmnp_web_1 python manage.py createsuperuser