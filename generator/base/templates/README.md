# REST API with Falcon, MongoDB and PyPy

Project Template for a high-performance RESTful web service in Python, using [falcon-jsonify](https://github.com/AndreiRegiani/falcon-jsonify) middleware and [MongoEngine](https://github.com/MongoEngine/mongoengine) Object-Document-Mapper.


## Setup

1. Install dependencies:

```
pip install -r requirements.txt
```

2. Start MongoDB Docker container:

```
docker-compose up -d
```

*Note:* this also starta a Mongo-Express Admin instance running at `localhost:8080`


## Run Development Server

```
./run_server.sh
```
Listening at [localhost:8000](http://localhost:8000). `Gunicorn` is used as WSGI HTTP Server.

**Demo routes:**

* `POST /api/example  {"email": "value"}` create an item
* `GET  /api/example` return all items


## Further Reading

* [MongoEngine Docs](http://docs.mongoengine.org/)
* [Falcon Docs](https://falcon.readthedocs.io/en/stable/)
* [Gunicorn Docs](http://docs.gunicorn.org/en/stable/)
* [About PyPy](http://pypy.org/features.html)
