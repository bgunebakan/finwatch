# Finwatch

Django based REST api service for financial news

## Getting Started

### Docker 
This project uses Docker CE and Docker Compose to run all services. [Installing Docker](https://docs.docker.com/engine/installation/#supported-platforms)
depends on the platform and is hence not included here. Docker Compose has to be [installed separately](https://docs.docker.com/compose/install/).
 
### Source Code
To obtain the source code, please clone this repository.

    git clone https://github.com/bgunebakan/finwatch

### Running
Runnig finwatch requires a fully configured `.env` file. A template for `.env` can be found in `.env.example`. Below, all values are documented.

 - `DB_NAME`: Postgres database name
 - `DB_USER`: Database User
 - `DB_PASSWORD`: Database password
 - `DB_HOST`: Postgres database host
 - `DB_PORT`: Postgres database port
 - `DEV`: Set Debug mode on/off
 - `REDIS_URL`: Redis server URL

After populating `.env` with all appropriate values, the service can be started with

    docker-compose up

### Django Management Console

Many development tasks require the django management console, which can be reached though the `exec` command of docker-compose. A typical example includes creating the django superuser to first login to Django.

    docker-compose exec finwatch_web python manage.py createsuperuser
    
To see a list of available management commands, call

    docker-compose exec finwatch_web python manage.py 


## License

All work in this repository is licensed under the MIT license. For details, see the LICENSE file.
