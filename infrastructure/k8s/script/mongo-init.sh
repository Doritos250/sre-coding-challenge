#!/usr/bin/env bash
kubectl cp mongo-db-init.js mongo-0:/tmp/.
kubectl exec -it mongo-0 -- bash -c "mongo --eval 'rs.initiate()'"
sleep 3
kubectl exec -it mongo-0 -- bash -c "mongo multivac /tmp/mongo-db-init.js"