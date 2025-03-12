
import os
import numpy as np
import tensorflow as tf
from PIL import Image
import cv2

# Charger le modèle
model_01 = tf.keras.models.load_model("model_weights/vgg19_model_01_with_generated_data.keras")

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

real_tumor_image_paths = []
real_pathTumor = "C:\\Users\\asus\\Downloads\\Brain tumor classification\\Dataset\\tumor".replace("\\", "/")
# Charger les images de "Tumor" avec le label 1
for filename in os.listdir(real_pathTumor):
    real_tumor_image_paths.append(os.path.join(real_pathTumor, filename))

Nb_real_Tumor = len(os.listdir(real_pathTumor))

x = 0
for i in range(Nb_real_Tumor):
  if(get_className(getResult(real_tumor_image_paths[i])) == "Tumor"):
    x = x + 1
print(x)