#!/bin/bash

set -e
MOVIELENS_DATASET=ml-100k

# Get Movielens data
if [ ! -f "$MOVIELENS_DATASET.zip" ]; then
  curl -SLO http://files.grouplens.org/datasets/movielens/$MOVIELENS_DATASET.zip
fi

if [ ! -d "$MOVIELENS_DATASET" ]; then
  unzip $MOVIELENS_DATASET.zip
fi

# Get generator
if [ ! -f "generate.rb" ]; then
  curl -SLO https://raw.githubusercontent.com/ankane/movielens.sql/master/generate.rb
fi

# Create SQL
if [ ! -f "movielens.sql" ]; then
  ruby generate.rb $MOVIELENS_DATASET > movielens.sql
fi

# Create database
createdb -U postgres -h $DB_PORT_5432_TCP_ADDR -p $DB_PORT_5432_TCP_PORT $MOVIELENS_DATASET

# Load data command

psql -U postgres -h $DB_PORT_5432_TCP_ADDR -p $DB_PORT_5432_TCP_PORT -d $MOVIELENS_DATASET -f movielens.sql
