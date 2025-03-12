import os
import numpy as np
import tensorflow as tf
from PIL import Image
import cv2
from flask import Flask, request, render_template
from werkzeug.utils import secure_filename

# Charger le modèle
model_01 = tf.keras.models.load_model("model_weights/vgg19_model_01.keras")
app = Flask(__name__)

print('Model loaded. Check http://127.0.0.1:5000/')

# Vérifier le dossier des fichiers uploadés
UPLOAD_FOLDER = 'uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def get_className(classNo):
    """Retourne la classe en fonction du numéro."""
    return "Healthy" if classNo == 0 else "Tumor" if classNo == 1 else "Unknown"

def getResult(img_path):
    """Prépare l'image et renvoie la prédiction de la classe."""
    image = cv2.imread(img_path)
    if image is None:
        raise ValueError(f"L'image n'a pas pu être chargée depuis le chemin : {img_path}")
    
    # Convertir en RGB et redimensionner
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    image = Image.fromarray(image).resize((224, 224))
    input_img = np.expand_dims(np.array(image) / 255.0, axis=0)
    
    # Prédiction
    result = model_01.predict(input_img)
    class_index = np.argmax(result, axis=1)[0]
    return class_index

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return "No file part in the request", 400
    
    file = request.files['file']
    if file.filename == '':
        return "No selected file", 400

    # Enregistrer le fichier
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(file.filename))
    file.save(file_path)

    # Prédire et retourner le résultat
    try:
        value = getResult(file_path)
        result = get_className(value)
        return result
    except Exception as e:
        return str(e), 500

if __name__ == '__main__':
    app.run(debug=True)
