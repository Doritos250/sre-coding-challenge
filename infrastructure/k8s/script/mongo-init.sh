#!/usr/bin/env bash
kubectl exec -it mongo-0 -- mongo --eval 'rs.initiate()'
sleep 3s
kubectl exec -it mongo-0 -- mongo multivac --eval 'db.createUser( { user: "multivac", pwd: "g84C7F3ZtMtfNgqD", roles: [ { role: "readWrite", db: "multivac" } ] } )'