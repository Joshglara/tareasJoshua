#Importar bibliotecas
#Utilidades keras
import tensorflow as tf
from tensorflow.keras.layers import GlobalAveragePooling2D, Dense, Dropout
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras.models import Model
#Para dividir datasets
import os
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import math

# Declarar el directorio con los datos
imagenes = r'C:\Users\glara\Desktop\Clasificador\modelo'
batch_size = 32
num_classes = len(os.listdir(imagenes))
epocas = 1

# Listamos todas las carpetas(clases) en el directorio
clases = os.listdir(imagenes)

# Dividimos los datos de entrenamiento y validacion
divisionDatos = 0.7

# Usar ImageDataGenerator para crear sonido en los datos
entrenar_datagen = ImageDataGenerator(
    rescale=1.0 / 255,
    rotation_range=20,
    width_shift_range=0.2,
    height_shift_range=0.2,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True,
    fill_mode='nearest',
    validation_split= 1-divisionDatos
)

# Cargamos y pre-procesamos los datos de prueba con el generador
entrenar_generator = entrenar_datagen.flow_from_directory(
    imagenes,
    target_size=(224, 224),
    batch_size=batch_size,
    class_mode='categorical',
    subset='training'
)

# Realizamos lo mismo para el set de validacion
validacion_generator = entrenar_datagen.flow_from_directory(
    imagenes,
    target_size=(224, 224),
    batch_size=batch_size,
    class_mode='categorical',
    subset='validation'
)

# Usar el modelo base MobileNetV2
base_model = MobileNetV2(weights='imagenet', include_top=False, input_shape=(224, 224, 3))

# Para clasificación
x = base_model.output
x = GlobalAveragePooling2D()(x)
x = Dense(512, activation='relu')(x)
x = Dropout(0.5)(x)  # Para regularizacion
predictions = Dense(num_classes, activation='softmax')(x)

model = Model(inputs=base_model.input, outputs=predictions)

# Cementar las capas del modelo
for layer in base_model.layers:
    layer.trainable = False

# Compilar el modelo
model.compile(optimizer=tf.keras.optimizers.Adam(learning_rate=0.001),
            loss='categorical_crossentropy',
            metrics=['accuracy'])

# Entrenar el modelo
history = model.fit(
    entrenar_generator,
    steps_per_epoch=entrenar_generator.samples // batch_size,
    epochs=epocas,
    validation_data=validacion_generator,
    validation_steps=validacion_generator.samples // batch_size
)

# Guardar el modelo
model.save('modeloPlantas.h5')
