
docker rm -vf $(docker ps -aq)
docker rmi -f $(docker images -aq)
docker system prune -y
docker volume prune -y
docker volume rm -f $(docker volume ls)
cp env-exemple .env
sudo docker-compose up
