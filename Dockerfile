FROM alpine:3.12
RUN apk update && apk add py3-setuptools && \
    apk add py-pip && pip install flask-restful 
    
WORKDIR /opt/crud/
COPY . .

WORKDIR /opt/crud
EXPOSE 5000
CMD ["python3", "server.py"]

# other ways, other ports
#CMD python3 manage.py runserver 8787
#CMD ["python3", "manage.py", "runserver", "0.0.0.0:8787"]
