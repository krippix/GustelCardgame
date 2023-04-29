# Generic Cardgame test

## Installation

run `pip install -r requirements.txt`

## run software

start backend: `uvicorn backend/cardgame/main:app --reload`

## Build and run frontend

`docker build frontend -t krippix/frontend`

`docker run -d -p 80:80 --name frontend krippix/frontend`
