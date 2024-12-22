import json  # Importation de la bibliothèque JSON pour manipuler les fichiers JSON
import os  # Importation de la bibliothèque OS pour interagir avec le système d'exploitation
import requests  # Importation de la bibliothèque Requests pour effectuer des requêtes HTTP
from flask import Flask, render_template, request, send_file  # Importation des modules Flask
from datetime import datetime  # Importation de datetime pour gérer les dates et heures
import csv  # Importation de la bibliothèque CSV pour travailler avec des fichiers CSV

app = Flask(__name__)  # Création d'une instance de l'application Flask
API_KEY = '5a681c967c9ac734cbb7aa88fc2b26d7'  # Remplacez par votre clé API OpenWeather

# Fonction pour charger l'historique des recherches depuis un fichier JSON
def load_history():
    if os.path.isfile('search_history.json'):  # Vérifie si le fichier existe
        with open('search_history.json') as f:  # Ouvre le fichier en mode lecture
            return json.load(f)  # Charge et retourne les données JSON du fichier
    return []  # Retourne une liste vide si le fichier n'existe pas

# Fonction pour sauvegarder une nouvelle recherche dans l'historique
def save_history(data):
    history = load_history()  # Charge l'historique actuel
    history.append(data)  # Ajoute les nouvelles données à l'historique
    with open('search_history.json', 'w') as f:  # Ouvre le fichier en mode écriture
        json.dump(history, f)  # Sauvegarde l'historique mis à jour dans le fichier JSON

# Route principale pour afficher la météo
@app.route('/', methods=['GET', 'POST'])  # Définit la route pour l'URL racine
def index():
    weather, error = None, None  # Initialise les variables pour la météo et les erreurs
    if request.method == 'POST':  # Vérifie si la méthode de la requête est POST
        city = request.form['city']  # Récupère le nom de la ville à partir du formulaire
        # Effectue une requête GET à l'API OpenWeather
        response = requests.get(f'https://api.openweathermap.org/data/2.5/weather', params={
            'q': city,  # Paramètre pour spécifier la ville
            'appid': API_KEY,  # Paramètre pour inclure la clé API
            'units': 'metric',  # Paramètre pour la température en degrés Celsius
            'lang': 'fr'  # Paramètre pour la langue française
        })
        if response.ok:  # Vérifie si la réponse de l'API est réussie (code 200)
            data = response.json()  # Convertit la réponse en JSON
            # Prépare les données météo à afficher
            weather = {
                'city': data['name'],  # Nom de la ville
                'temperature': data['main']['temp'],  # Température actuelle
                "humidite": data["main"]["humidity"], # L'humidité 
                'description': data['weather'][0]['description'],  # Description de la météo
                'icon': data['weather'][0]['icon']  # Icône représentant les conditions météorologiques
            }
            # Sauvegarde l'historique de la recherche
            save_history({
                'city': weather['city'],  # Ville recherchée
                'temperature': weather['temperature'],  # Température récupérée
                'humidite': weather['humidite'], #Humidité recuperée
                'description': weather['description'],  # Description de la météo
                'datetime': datetime.now().isoformat()  # Date et heure de la recherche
            })
        else:
            error = "Ville non trouvée. Veuillez réessayer."  # Message d'erreur si la ville n'est pas trouvée
    return render_template('index.html', weather=weather, error=error)  # Affiche la page avec les données météo

# Route pour afficher l'historique des recherches
@app.route('/history')  # Définit la route pour l'historique
def history():
    # Affiche la page d'historique avec les recherches triées par date (les plus récentes en premier)
    return render_template('history.html', history=sorted(load_history(), key=lambda x: x['datetime'], reverse=True))

# Route pour télécharger l'historique au format CSV
@app.route('/download')  # Définit la route pour le téléchargement
def download():
    history = load_history()  # Charge l'historique des recherches
    # Ouvre un fichier CSV pour écrire l'historique
    with open('search_history.csv', 'w', newline='', encoding='utf-8-sig') as f:
        writer = csv.writer(f)  # Crée un objet writer pour écrire dans le fichier CSV
        writer.writerow(['Ville', 'Température', 'Description', 'Datetime'])  # Écrit l'en-tête des colonnes
        # Écrit chaque entrée de l'historique dans le fichier CSV
        writer.writerows([[entry['city'], entry['temperature'], entry['description'], entry['datetime']] for entry in history])
    return send_file('search_history.csv', as_attachment=True)  # Envoie le fichier CSV en téléchargement

if __name__ == '__main__':
    app.run(debug=True)  # Lance l'application Flask en mode debug