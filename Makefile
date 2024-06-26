run:
	python app/main.py

up-build:
	sudo docker-compose build
	sudo docker-compose up

build:
	sudo docker-compose build


down:
	sudo docker-compose down


up-d:
	sudo docker-compose up -d

up:
	sudo docker-compose up

bash:
	sudo docker exec -it auto-backend bash

clean:
	sudo docker-compose down -v

format:
	isort app/
	black app/
	flake8 app/ 

create:
	python3 -m venv venv


req-d:
	pip install -r requirements/dev.txt


req-b:
	pip install -r requirements/base.txt

test:
	pytest app/tests

test-and-run:
	pytest app/tests/ && make run

test-and-up:
	pytest app/tests/ && make up

test-and-build:
	pytest app/tests/ && make up-build