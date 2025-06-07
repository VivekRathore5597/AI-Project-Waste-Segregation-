
import streamlit as st
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import img_to_array, load_img
import numpy as np
import os

# Load model
model_path = os.path.join("model", "waste_classifier.h5")
model = load_model(model_path)
classes = ['cardboard', 'compost', 'glass', 'metal', 'paper', 'plastic', 'trash']

st.title("AI Waste Segregation")
st.write("Upload a waste image and get classification results instantly!")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
if uploaded_file is not None:
    image = load_img(uploaded_file, target_size=(150, 150))
    st.image(image, caption='Uploaded Image', use_column_width=True)

    img_array = img_to_array(image) / 255.0
    img_array = np.expand_dims(img_array, axis=0)

    prediction = model.predict(img_array)
    predicted_class = classes[np.argmax(prediction)]

    st.subheader("Prediction:")
    st.success(predicted_class)
