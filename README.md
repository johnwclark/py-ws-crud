# py-ws-crud

a simple python crud web service

## requirements

## virtual environment

I am assuming that you are using a pipenv/virtualenv  setup, instead of a global one.

Set this up once.

```bash
virtualenv venv
```

Now use the activate and deactivate scripts as needed.

```bash
venv\Scripts\activate.bat
venv\Scripts\deactivate.bat
```

Source links

<https://docs.python.org/3/tutorial/venv.html>

<https://docs.python-guide.org/dev/virtualenvs/>

## this is based on this example

<https://codeburst.io/this-is-how-easy-it-is-to-create-a-rest-api-8a25122ab1f3>

<https://auth0.com/blog/developing-restful-apis-with-python-and-flask/>

## testing the web service

There are nicer visual tools like postman or insomnia, but I am going with 
curl for this, so it can be scripted.

### For PUT request

```bash
curl --request PUT --url http://localhost:8080/put --header 'content-type: application/x-www-form-urlencoded' --data 'bar=baz&foo=foo1'
```

### For POST request

```bash
curl --request POST --url http://localhost:8080/post --header 'content-type: application/x-www-form-urlencoded' --data 'bar=baz&foo=foo1'
```

### For GET request

```bash
curl --request GET --url 'http://localhost:8080/get?foo=bar&foz=baz'
```
