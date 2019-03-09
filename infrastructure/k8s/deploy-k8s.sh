#!/usr/bin/env bash
kubectl create -f flask-config-map.yml
kubectl create -f secret.yml
kubectl create -f googlecloud_ssd.yml
kubectl create -f mongodb-deployment.yml
kubectl create -f mongodb-service.yml
kubectl create -f redis-deployment.yml
kubectl create -f redis-service.yml
kubectl create -f flask-deployment.yml
kubectl create -f flask-service.yml
kubectl create -f worker-deployment.yml