docker rm -vf $(docker ps -aq)
docker rmi -f $(docker images -aq)
docker build -t django . 
docker run -p 8000:8000 django 