# py-ws-crud

a simple python crud web service

<https://codeburst.io/this-is-how-easy-it-is-to-create-a-rest-api-8a25122ab1f3>

<https://auth0.com/blog/developing-restful-apis-with-python-and-flask/>

## virtual environment

<https://docs.python.org/3/tutorial/venv.html>

<https://docs.python-guide.org/dev/virtualenvs/>

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
