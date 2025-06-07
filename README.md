
# AI-Powered Waste Segregation System

This project classifies waste images into categories like cardboard, glass, metal, paper, plastic, and trash using a Convolutional Neural Network (CNN) and deploys it using Streamlit.

## 💾 Dataset
Use the [Garbage Classification Dataset](https://www.kaggle.com/datasets/sumn2u/garbage-classification-v2) and place the organized image folders into `dataset/`.

## 🚀 How to Run

1. Install dependencies:
```bash
pip install -r app/requirements.txt
```

2. Train the model:
```bash
Run notebooks/waste_classification.ipynb
```

3. Run the Streamlit app:
```bash
streamlit run app/app.py
```
