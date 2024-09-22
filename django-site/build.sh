
docker rm -vf $(docker ps -aq)
docker rmi -f $(docker images -aq)
docker system prune -y
docker volume prune -y
docker volume rm -f $(docker volume ls)
cp env-exemple .env
sudo docker-compose up



# docker-compose exec web python voiture/manage.py migrate
# docker-compose exec web python voiture/manage.py createsuperuser 
# docker-compose exec web python voiture/manage.py createsuperuser \
#     --email 'admin@admin.com' --username 'admin2' \
#     --noinput

# docker-compose exec web  python voiture/manage.py shell < voiture/voiture/super.py