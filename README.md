## IIC2173-T1

### Tarea 1 del curso Arquitectura de Sistemas de Software - IIC2173

Tutoriales utilizados:
* [The Flask Mega Tutorial](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world)
* [Nginx Flask Portgres Docker Compose](http://www.ameyalokare.com/docker/2017/09/20/nginx-flask-postgres-docker-compose.html) 

### Instalación

1. Clone repo
```
git clone git@github.com:dacasas/IIC2173-T1.git
```

2. Bootstrap the DB
```bash
$ docker-compose up -d db
$ docker-compose run --rm flaskapp /bin/bash -c "cd /opt/services/flaskapp/src && python -c  'import database; database.init_db()'"
```

3. Bring up the cluster
```bash
$ docker-compose up -d
```

4. Go to the page.