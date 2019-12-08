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

## virtual environment

I am experimenting with a pipenv/virtualenv  setup, instead of a global one.  I am currently working on a windows 10
 environment, which requires fixing the paths for all the tools like pip and virtualenv.

Set this up once.

```cmd
virtualenv venv
```

Now use the activate and deactivate scripts as needed.

```cmd
venv\Scripts\activate.bat
venv\Scripts\deactivate.bat
```

On a unix box just source

Source links

<https://docs.python.org/3/tutorial/venv.html>

<https://docs.python-guide.org/dev/virtualenvs/>
