build-server:
	cd server && docker build . -t light-control-system -f dockerfiles/server/Dockerfile

build-scheduler:
	cd server && docker build . -t django-q -f dockerfiles/scheduler/Dockerfile

run: build-server
	docker-compose up

build-and-run: build-server build-scheduler run
