#!/bin/bash

echo "Waiting for RDF4J to be available on database:8080..."

until curl --output /dev/null --silent --fail http://database:8080/rdf4j-server/repositories; do
  echo "RDF4J not ready yet, retrying in 5 seconds..."
  sleep 5
done

echo "RDF4J is up, starting Flask app..."
exec "$@"
