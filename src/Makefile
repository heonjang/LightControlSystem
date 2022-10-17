build-server:
	cd server && docker build . -t light-control-system -f Dockerfile

run: build-server
	docker-compose up
