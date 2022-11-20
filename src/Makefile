build-server:
	cd server && docker build -t light-control-system -f dockerfiles/server/Dockerfile . 

build-scheduler:
	cd server && docker build . -t django-q -f dockerfiles/scheduler/Dockerfile

run: build-server
	docker compose up

upload-image:
	cd server && gcloud builds submit --tag gcr.io/analog-sum-366019/light-control-system .
