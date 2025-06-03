import numpy as np
import tensorflow as tf
import os
from tensorflow.keras.preprocessing.image import load_img, img_to_array
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input

foto = r'C:\Users\glara\Desktop\Clasificador\images.jpg'
mapeoClases = {i: clase for i, clase in enumerate(sorted(os.listdir(r'C:\Users\glara\Desktop\Clasificador\modelo')))}

# Cargar el modelo entrenado
modelo = tf.keras.models.load_model('modeloPlantas.h5')

# Cargar y preprocesar la imagen a analizar
def preprocesoImagen(image_path):
    image = load_img(image_path, target_size=(224, 224))
    image_array = img_to_array(image)
    image_array = np.expand_dims(image_array, axis=0)
    imagenPreprocesada = preprocess_input(image_array)
    return imagenPreprocesada

# Realizar analisis
def analizaPlanta(dirImagen, label_mapping):
    preprocessed_image = preprocesoImagen(dirImagen)
    predictions = modelo.predict(preprocessed_image)
    
    # Mapear las predicciones del modelo a to labels
    predicted_label_index = np.argmax(predictions)
    predicted_label = label_mapping[predicted_label_index]
    confidence = predictions[0][predicted_label_index]
    
    return predicted_label, confidence

# Provide the path to the image you want to classify
planta, confianza = analizaPlanta(foto, mapeoClases)

# Print the prediction
print(f"Planta: {planta}")
print(f"Confianza: {confianza:.2f}")
