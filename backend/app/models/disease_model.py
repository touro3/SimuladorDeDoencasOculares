import tensorflow as tf
from tensorflow.keras.models import load_model

def load_disease_model():
    model = load_model('path_to_your_trained_model.h5')
    return model

def predict_disease_effect(image, model):
    # Pre-process the image and use the model to predict
    prediction = model.predict(image)
    return prediction
