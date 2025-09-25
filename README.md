# Simple Image Classifier App

This repository contains a simple, yet powerful, web application for classifying images.  
Built with **Python**, it leverages the **Streamlit** framework to create an interactive user interface and the **Hugging Face Transformers** library to perform image classification using a state-of-the-art pre-trained model.

The app allows users to upload an image and instantly see a list of predicted labels with their corresponding confidence scores.

---

## ✨ Features

- **User-friendly Interface**: A clean and intuitive web interface for uploading images.  
- **Powerful Backend**: Uses a pre-trained **Vision Transformer (ViT)** model from Google for accurate classification.  
- **Error Handling**: Provides clear messages for potential issues like network errors during model download.  
- **Real-time Prediction**: Classifies images instantly after upload with a loading indicator.  

---

## 🚀 Getting Started

To run this application locally, follow these steps:

### 1. Clone the repository, install the required libraries, and run the app
```bash
# Clone the repository
git clone https://github.com/your-username/simple-image-classifier-app.git
cd simple-image-classifier-app

# Install dependencies
pip install streamlit transformers torch Pillow

# Run the app
streamlit run app.py
