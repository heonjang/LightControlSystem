Containerization means making a codebase runnable in a certain environment ([VM vs container](https://www.atlassian.com/microservices/cloud-computing/containers-vs-vms#:~:text=The%20key%20differentiator%20between%20containers,above%20the%20operating%20system%20level.) for more reference)

**We need to dockerize(containerize) the sever for two reasons**.


# Why dockerize

### 1. Consistent working environments for team members.
In the team, we have people using Mac and Windows. Also, one Mac user uses the Intel chip while the other one uses a M1 chip.

Due to this difference, the development setting should be handled separately, and this tends to cause many problems.

Therefore, if we dockerize(containerize) the codebase, we are going to be running the application in an identical environment.




### 2. Prepare for the k8s integegration in the future
In order to strengthen the stability of the server, the system will use the Kubernetes(k8s) which is a container orchestration tool.

Thus, we need to containerize the codebase to use it.




# Design

<img width="1042" alt="Screen Shot 2022-10-09 at 4 54 48 PM" src="https://user-images.githubusercontent.com/103418311/194781234-d8aef5ec-eee2-4a6f-a01b-c665624fc96a.png">


This is a rough diagram of how components are going to be dockerized

There are going to be 3 dockerized components

### 1. Backend Server
This server will be implemented with Django(python) in a linux environment.
Until the frontend server is ready to be developed, it will also serve the frontend as well for a easy development purpose.

The docker file for the backend
```yaml
FROM python:3.9.11

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip install -r requirements.txt
COPY . .

EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000", "--noreload"]
```

Its service configuration in the docker-compose file.

```yaml
backend:
  container_name: lcs-server
  image: light-control-system-server
  ports:
    - "8000:8000"
```


### 2. PSQL
This container will be running the official image of the PSQL

So the service configuration in the docker-compose file is 
```yaml
db:
    container_name: lcs-postgres
    image: postgres:14.1-alpine
    environment:
      - POSTGRES_USER=postgres
      - POSTGRES_PASSWORD=postgres
    ports:
      - '5432:5432'
```


The current main page:

<img width="1690" alt="Screen Shot 2022-10-09 at 5 09 00 PM" src="https://user-images.githubusercontent.com/103418311/194781785-19688712-0540-4f3b-9cd1-4aadd2b025e3.png">


