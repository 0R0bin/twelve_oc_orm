# twelve_oc_orm
## Récapitulatif
Ce projet est une CRM sécurisée en interne pour la société Epic Events.  
Cette CRM permet de stocker des informations en rapport avec des utilisateurs, contrats, évènements et clients. 

Pour mener à bien ce projet, les technologies suivantes ont été utilisées :  
* Python
* SQLAlchemy
* Click
* Psycopg2 (POSTGRESQL)
* PyJWT

## Détails
La CRM est organisée en trois niveaux d'accès.

Le premier, le pôle Gestion s'occupe d'enregistrer les utilisateurs de la société Epic Events, de créer les contrats et d'associer des collaborateurs du pôle support aux évènements.

Le second, le département commercial s'occupe du relationnel client. Ils ont donc, sur la solution, la possibilité de créer des clients et de les maintenir. Et de modifier les contrats, liés à leurs clients.

En dernier nous retrouvons l'équipe support qui peut mettre à jour les évènements pour lesquels ils ont été nommés responsables.

Tous peuvent accéder à l'entièreté des objets Clients, Contrats, et évènements.
Pour facilier la recherche des filtres sont mis en place en fonction du niveau d'accès de l'utilisateur.
Par exemple pour les évènements, si l'utilisateur est du pôle support, alors il pourra filtrer tous les évènements auxquels il a été rattaché. En revanche si un utilisateur du département Gestion utilise le filtre, ce dernier verra tous les contrats sans collaborateur support associé.

## Configuration
Dans le dossier files, créer un fichier nommé env.json avec les informations suivantes
```
"DB_USER": "votre_user",
"DB_PASS": "votre_mdp",
"DB_NAME": "votre_nom_de_bdd",
"DB_HOST": "votre_host",
"DB_PORT": 5432,
"SECRET_KEY": "votre_cle",
"LIFETIME_TOKEN": 120
```
Merci de notrer que le LIFETIME_TOKEN est à renseigner en minutes  
```
NE PAS OUBLIER LA BASE DE DONNEES
```
Téléchargez ou clonez le repository à l'aide du lien suivant
```
https://github.com/0R0bin/twelve_oc_orm.git
```
Placez vous dans le dossier du repository, puis, exectuez les commandes suivantes :
Sous Unix/macOS
```
python3 -m venv env
```
```
source env/bin/activate
```
Sous Windows
```
py -m venv env
```
```
.\env\Scripts\activate
```
Ensuite, installez les packages nécessaires :
```
pip install -r requirements.txt
```
Positionnez vous ensuite dans le dossier epic_orm
Et initialisez votre base de données à l'aide de la commande ci-dessous
```
python app.py init-db
```
Un utilisateur vous sera créer par défaut, vous pouvez vous connecter grâce à cette commande
```
python app.py login admin@admin.fr
```
Vous êtes prêt !
## Exemples de commande
Vous pouvez naviguez et avoir toute l'aide nécessaire dans votre console à l'aide de Click
Pour avoir la liste des commandes :
```
python app.py
```
Exemple de commandes :
```
python app.py client list-all
```
```
python app.py user create
```
Attention aux droits d'accès !
## Sources & Aides
Informations sur SQLAlchemy
```
https://www.tutorialspoint.com/sqlalchemy/sqlalchemy_orm_updating_objects.htm
```
Markdown
```
https://github.com/Simplonline-foad/utiliser-markdown/blob/master/README.md
```
## Améliorations possibles
POETRY (Package manager)
setup.py -> Transformation en package
Voir console script en général