# codotype-python-falcon-mongodb-generator
:snake: Codotype Generator for REST APIs in Python, Falcon, &amp; MongoDB

This [Codotype](https://codotype.io) Generator builds Python REST APIs with Falcon, MongoDB, and Gunicorn

## Setup

1. Install dependencies:

```
pip install -r requirements.txt
```

2. Start MongoDB Docker container:

```
docker-compose up -d
```

*Note:* this also starts a Mongo-Express Admin instance running at `localhost:8081`


## Run Development Server

```
./run_server.sh
```

Listening at [localhost:8000](http://localhost:8000). `Gunicorn` is used as WSGI HTTP Server.

## Further Reading
- [MongoEngine](http://docs.mongoengine.org/)
- [Falcon](https://falcon.readthedocs.io/en/stable/)
- [Gunicorn](http://docs.gunicorn.org/en/stable/)
- [Codotype](http://codotype.io/)