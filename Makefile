bash:
	docker exec -it django-flyio_setup_1 bash

deploy:
	flyctl deploy

fly_console:
	flyctl ssh console

run:
	docker-compose up