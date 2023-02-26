# uav-rental-project


###  Development Setup

- install Docker and Docker-compose 

Follow the instructions from the link below;
	-https://docs.docker.com/engine/install/
	-https://docs.docker.com/compose/



First run docker-compose in detach mode by executing this command then;
```
docker-compose up -d
```

- run this command to create migrations
```
docker-compose exec web python manage.py makemigrations
```

- migrate the database
```
docker-compose exec web python manage.py migrate
```

Go to http://0.0.0.0:8000/

To stop all services:

```
docker-compose down
```
