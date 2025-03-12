Pour exécuter app.py , il faut exécuter ces commandes :
1. Créer un environnement python 
>> python -m venv venv

2. Activer l'environnement
>> venv\Scripts\activate

Après erreurs :
... Autoriser les Scripts PowerShell
>> Set-ExecutionPolicy RemoteSigned
et choisir Yes(Y)


3. Installer les dépendances existantes dans un fichier par exemple ici requirements.txt
>> pip install -r requirements.txt
Sinon exécuter les dépendances une à une, par exemples :
>> pip install Pillow
>> pip install flask
>> pip install tensorflow

4. Exécuter l'application
>> flask --app app.py run
