# Application Météo avec Flask et OpenWeather API

## Description
Cette application permet aux utilisateurs de consulter la météo d'une ville, de sauvegarder l'historique des recherches et de télécharger cet historique en format CSV.

## Fonctionnalités
#Saisissez le nom d'une ville pour obtenir la météo actuelle.
- **Recherche de météo** : bafoussam
- **Gestion des erreurs** : Messages clairs si la ville n'est pas trouvée ou si un problème survient lors de l'appel API.
- **Historique des recherches** : Sauvegarde des recherches valides dans un fichier JSON et affichage sur une page distincte.
- **Téléchargement CSV** : Option pour télécharger l'historique des recherches au format CSV.

## Configurer le projet
1. Clonez le dépôt ou téléchargez les fichiers du projet :
    ```bash
    cd <CHEMIN/Vers/LE/DOSSIER>
    git clone https://github.com/GitDurrel/CC_python-meteo.git

2. Installez les dépendances requises :
    ```bash
    pip install -r requirements.txt

3. Créez un fichier .env à la racine du projet et ajoutez votre clé API OpenWeather :
    
    API_KEY=<VOTRE_CLE_API>

## Execution
1. Lancez l'application Flask avec la commande :
        ```bash
        flask run 

2. Accédez à l'application dans votre navigateur à l'adresse : http://127.0.0.1:5000

## Obtention d'une clé API OpenWeather
1. Rendez-vous sur OpenWeather.com et créez un compte.

2. Générez une clé API et ajoutez-la dans le fichier .env.

# Creation du depot git pour le projet
1. Installer le logiciel git sur votre pc , executez cette commande pour verifier l'installation:
    ```bash
    git --version

2. Initialisez un nouveau dépôt Git local dans le dossier courant:
    ```bash
    git init

3. Ajoutez tous les fichiers (suivis ou non suivis) dans la zone de staging:
    ```bash
    git add .

4. Enregistrez les fichiers dans l'historique Git avec un message:
    ```bash
    git commit -m "First commit"

5. Liez le dépôt local à un dépôt distant :
    . Créez un nouveau dépôt sur GitHub 
    .        ```bash
            git remote add origin https://github.com/GitDurrel/CC_python-meteo.git

6. Transfèrez les fichiers vers GitHub et établit une connexion par défaut entre les branches locale et distante:
    git push -u origin master

7. Creez des branches pour chaque nouvelles fonctionnlités 




