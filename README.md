# py-ws-crud

a simple python crud web service

## requirements

This only needs flask-restful and its dependencies.

```cmd
pip install flask-restful
```

## this is based on this example

<https://codeburst.io/this-is-how-easy-it-is-to-create-a-rest-api-8a25122ab1f3>

<https://auth0.com/blog/developing-restful-apis-with-python-and-flask/>

<https://flask-restful.readthedocs.io/en/0.3.5/quickstart.html>

## testing the web service

There are nicer visual tools like postman or insomnia, but I am going with curl for this, so it can be scripted.

Get the full list, and try one user that is present and one that isn't

```bash
curl -s --request GET --url http://127.0.0.1:5000/users
curl -s --request GET --url http://127.0.0.1:5000/user/Matt
curl -s --request GET --url http://127.0.0.1:5000/user/Kirby
```

Now let test adding one, trying to add it again, changing it, and deleting it.

```bash
curl -s --request POST --url http://127.0.0.1:5000/user/Kirby --data 'age=42&occupation=slacker'
curl -s --request POST --url http://127.0.0.1:5000/user/Kirby --data 'age=42&occupation=awesome dude'
curl -s --request PUT --url http://127.0.0.1:5000/user/Kirby --data 'age=42&occupation=awesome dude'
curl -s --request DELETE --url http://127.0.0.1:5000/user/Kirby
```

## Docker

I was originally doing this is a pipenv/venv setup, but 
decided to move to docker.  It is just way less hassle and 
setup, plus it is easier for an end user to setup and run 
the sample code, without needing any extra tools or 
permissions.

### Docker commands

if a build is out of space use 
docker system prune
tags can have versions ie polls:1.0

docker run polls [command]
docker run polls ls -lR /opt/mysite/

docker build --tag polls .
docker run --publish 8787:8787 --detach --name ptest polls

docker ps
docker stop ptest
docker rm ptest