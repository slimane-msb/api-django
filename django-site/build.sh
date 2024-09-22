docker rm -vf $(docker ps -aq)
docker rmi -f $(docker images -aq)
docker system prune
docker build -t django . 
docker run -p 8000:8000 django 


docker rm -vf $(docker ps -aq)
docker rmi -f $(docker images -aq)
docker system prune -y
docker volume prune -y
docker volume rm -f $(docker volume ls)
cp env-exemple .env
sudo docker-compose up
docker-compose exec web python voiture/manage.py migrate
docker-compose exec web python voiture/manage.py createsuperuser
