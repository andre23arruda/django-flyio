bash:
	docker exec -it app bash

deploy:
	flyctl deploy

fly_console:
	flyctl ssh console

run:
	docker-compose up

superuser:
	docker exec -it app python manage.py createsuperuser