#!/bin/bash

# Variables
DOCKER_IMAGE_1="flask-app-1:latest"
DOCKER_IMAGE_2="flask-app-2:latest"

K8S_NAMESPACE="default"

# Build & Push Docker Image
docker build -t $DOCKER_IMAGE_1 -f app-1/Dockerfile app-1/ 
docker push $DOCKER_IMAGE_1

# Build & Push Docker Image
docker build -t $DOCKER_IMAGE_2 -f app-2/Dockerfile app-2/ 
docker push $DOCKER_IMAGE_2

cat app-1/dep-app1.yml | sed "s/{{IMAGE_NAME}}/$DOCKER_IMAGE_1/g" | kubectl apply -n $K8S_NAMESPACE -f -
cat app-2/dep-app2.yml | sed "s/{{IMAGE_NAME}}/$DOCKER_IMAGE_2/g" | kubectl apply -n $K8S_NAMESPACE -f -

kubectl port-forward service/flask-app-1 8000:8000 &
kubectl port-forward service/flask-app-2 9000:9000 &


curl -s 127.0.0.1:8000
curl -s 127.0.0.1:9000

