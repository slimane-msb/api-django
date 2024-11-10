# étape 1: Création et Publication d'une Image Docker pour l’Application Django

- test 
```
docker compose up --build

docker run yzriga/todo_list_project:v1

monkube delete deployments/voiture-dep

monkube delete deployments/ma-db

monkube delete services/db

monkube delete services/todo-list-service

monkube delete services/mon-dep-service

monkube get deployments
monkube get services


monkube apply -f dep-db.yml
monkube apply -f deployment.yaml
monkube apply -f service-db.yml
monkube apply -f service.yaml
```


```
docker build -t yzriga/todo_list_project:v1 .

docker login

docker push yzriga/todo_list_project:v1


docker build -t yzriga/voiture:v1 .

docker login

docker push yzriga/voiture:v1


docker build -t ssdev1254/voiture:v1 .

docker login

docker push ssdev1254/voiture:v1

```
# étape 2: Déployer le site Django dans un Pod

```
monkube apply -f deployment.yaml

monkube apply -f service.yaml

monkube get pods

monkube logs deployments/voiture-dep > log.log

```
# Questions

# Quelle est la différence entre un service ClusterIP et NodePort ?
Les deux sont une solution pour la non stabilité des IP des pods, et donc pour permettre d'accéder au pods. La différence entre les deux se base sur : 
L'ouverture : NodePort peut permettre à la fois d'exposer le port dans le cluster et à l'exterieur du cluster. ClusterIP crée une IP virtuelle et permet uniquement un accés interne. 

# Quelle critique pouvez-vous donner vis-à-vis de l'utilisation d'un Pod pour la base de données ?



# Sur quel type de ressource KubeDNS crée des entrées ? Quelle information propre a la ressource est utilisée ?


# Le schéma !
