# BDD
<div align="center" style="width: 70%;">
    <img src="https://github.com/user-attachments/assets/1c602641-af2e-40f1-b534-f7faa8f97a9e" width="70%" />
</div>


# Infrastructure
- L'infrastructure utilisée est celle du projet
<div align="center" style="width: 40%;">
    <img src="https://github.com/user-attachments/assets/acc2bf1b-b7a1-4b4d-8540-8bf9382f197c" />
</div>

# Routes 
## API 
- **GET** `garages/` : récupérer la liste de tous les garages.
- **GET** `garages/<int:pk>/` : récupérer un garage par son identifiant.
- **POST** `garages/add/` : ajouter un garage en fournissant son nom. Exemple de données : `-d {'nom': 'nom du garage'}`.
- **PUT/PATCH** `garages/<int:pk>/edit/` : modifier un garage en fournissant un nouveau nom. Exemple de données : `-d {'nom': 'nouveau nom'}`.
- **DELETE** `garages/<int:pk>/delete/` : supprimer un garage par son identifiant.

- **GET** `voitures/` : récupérer la liste de toutes les voitures.
- **GET** `voitures/<int:garageId>/` : récupérer une voiture par l'identifiant de son garage.
- **POST** `voitures/add/` : ajouter une voiture en fournissant toutes les informations nécessaires sous forme de JSON. Exemple de données : `-d {json contenant tous les champs de la voiture}`.


# public 
- **GET** `login/` : accéder à la page de connexion (Login).
- **GET** `signup/` : accéder à la page d'inscription (Signup).
- **GET** `profile/` : voir le profil de l'utilisateur connecté.
- **GET** `voiture/` : accéder à la page des voitures pour obtenir les formulaires de récupération de données.
- **GET** `garage/` : accéder à la page des garages pour obtenir les formulaires de récupération de données.


# Question 
## Django 

1. **Suite de requêtes et d'exécutions permettant l'affichage d'une page HTML** : 
   - On commence par recevoir la requête, puis vérifier si le endpoint existe dans la liste des URL de `urls.py` du projet. Le chemin `/` est ensuite redirigé vers l'application `public`, qui, à son tour, redirige vers la vue "home". Cette vue renvoie une page HTML `index.html`.

2. **Configurer la base de données** : 
   - La base de données est à configurer dans le fichier `settings.py` et l'ensemble des schémas de base dans le fichier `models.py`. 

3. **Configurer le fichier de paramètres du projet** : 
   - `settings.py` : Pour les configurations de base, comme les applications à installer, les hôtes autorisés, le chemin pour les fichiers statiques et médias, etc.
   - `apps.py` : Ce fichier permet de configurer chaque application du projet. Par exemple, pour l'API, on configure l'importation des signaux, qui sont déclenchés lors de la création d'un utilisateur pour générer un profil correspondant. Il est possible d'étendre la classe `User`, mais une bonne pratique consiste à créer un modèle `Profile` pour stocker les champs supplémentaires tels que la photo de profil, la localisation, etc.

4. **Makemigrations** : 
   - `makemigrations` : Django lit les fichiers `models.py` et les fichiers de migrations pour détecter les changements à apporter à la base de données. Si des modifications sont détectées, elles sont enregistrées dans des fichiers de migration, qui représentent des instructions à exécuter ultérieurement sur la base de données.
   - `migrate` : Cette commande applique les instructions générées lors de l'étape précédente sur la base de données et met à jour la table des migrations, qui stocke les métadonnées concernant les modifications appliquées.

## Docker 

1. **Commandes Docker** : 
   - `FROM` : Indique quelle image et quelle version récupérer pour commencer le build.
   - `RUN` : Exécute une commande lors du build.
   - `WORKDIR` : Définit le répertoire de travail du conteneur, équivalent à `~`.
   - `EXPOSE` : Ouvre des ports spécifiques.
   - `CMD` : Exécute une commande lors du lancement du conteneur, généralement une seule commande ou un script.

2. **Service** : 
   - `ports: "80:80"` : Connecte le port 80 de la machine locale au port 80 du conteneur. Si on appelle la machine sur le port 80, cette requête sera redirigée vers le port 80 du conteneur.
   - `context: .` : Indique dans quel dossier chercher le Dockerfile.
   - `dockerfile: Dockerfile.api` : Indique quel Dockerfile exécuter pour le build.
   - `depends_on` : Crée un réseau entre les conteneurs. Par exemple, pour requêter l'API depuis le service web, on peut exécuter `curl -X GET http://api:8001/api/...`.
   - `environment` : Définit les variables d'environnement depuis un fichier `.env`.

3. **ENV** : 
   - Définir une variable d'environnement dans un conteneur :
     - Les inclure lors du build dans le fichier Dockerfile ou via le fichier docker-compose dans `environment` depuis `.env` ou explicitement
     - Se connecter au conteneur et les définir manuellement via `docker-compose exec web sh`, utile pour déboguer.

4. **Réseau Docker** : 
   - Remplacer l'IP par le nom du service, par exemple `http://web:8000`.

