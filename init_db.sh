#Create docker-compose file first
docker-compose up --build

docker-compose exec web flask db init
docker-compose exec web flask db migrate
docker-compose exec web flask db upgrade