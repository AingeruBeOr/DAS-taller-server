# API and DB

## Descriptions

### API Rest

Using FastAPI (Python) for the API REST.

Using uvicorn for the production server.

### DB

Using mysql

## Running

Different environments for different purposes:

* DEV environment

### DEV environment

Start DEV environment using: `docker compose -f docker-compose-dev.yaml up`

Para conectarse a MySQL desde la máquina host desde le aplicación CLI de MySQL despúes de haber mapeado el puerto (hay que especificar IP y puerto):

`mysql -h 127.0.0.1 -P 3306 -u root -p`
