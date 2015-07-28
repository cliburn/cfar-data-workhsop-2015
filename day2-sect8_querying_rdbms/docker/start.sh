#!/bin/bash

# Start database container
docker run -d -P --name movielens-db postgres:9.4.4

#Load data
docker build -t movielens-loader .
docker run --rm --link movielens-db:db movielens-loader

