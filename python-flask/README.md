## Overview
This repo provides a basic example of how to containerzie a simple Python based web application.

## Dockerfile
Dockerfile is used to build the container image for this Python app.


## Build the container image
```
docker build . -t python-flask-simple-webapp
```

## Push the image to docker hub
* Tag the image with your user account

```
docker build . -t vineethac/python-flask-simple-webapp
```

* Check the image
```
❯ docker images | grep python-flask-simple-webapp
vineethac/python-flask-simple-webapp                                                     latest         a494930c7792   12 minutes ago   519MB
python-flask-simple-webapp                                                               latest         a494930c7792   12 minutes ago   519MB
❯
```

* Login to docker hub and push the image
```
❯ docker login
Login with your Docker ID to push and pull images from Docker Hub. If you don't have a Docker ID, head over to https://hub.docker.com to create one.
Username: vineethac
Password:
Login Succeeded

Logging in with your password grants your terminal complete access to your account.
For better security, log in with a limited-privilege personal access token. Learn more at https://docs.docker.com/go/access-tokens/

❯
❯ docker push vineethac/python-flask-simple-webapp
Using default tag: latest
The push refers to repository [docker.io/vineethac/python-flask-simple-webapp]
52593ae03020: Pushed
4126fb46affb: Pushed
63ac3fe112a0: Pushed
cf07ecc48e8b: Pushed
f54b14754230: Pushed
4b19ec59a03e: Pushed
a899174a51cd: Pushed
256d88da4185: Mounted from library/ubuntu
latest: digest: sha256:5ebd12de4c09de57d9bc13e7255d7151dd40823a9f37851c11b29afbe950c0e1 size: 2006
❯
```

## To run this web application as a pod on Kubernetes

`kubectl run webapp --image=vineethac/python-flask-simple-webapp -n default`

## To port forward the application from your localhost

`kubectl port-forward pod/webapp -n default 8080:5000`

## From the localhost machine you can open another terminal and verify
```
❯ curl http://127.0.0.1:8080      
Welcome to flask!  
❯   
❯ curl http://127.0.0.1:8080/hello  
Hello, this is a response from flask!  
❯
```
