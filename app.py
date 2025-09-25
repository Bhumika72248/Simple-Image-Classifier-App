import streamlit as st
from PIL import Image
from transformers import pipeline

# ---- App Setup ----
st.set_page_config(
    page_title="Simple Image Classifier",
    page_icon="🖼️",
    layout="centered",
    initial_sidebar_state="collapsed",
)

st.title("🖼️ Simple Image Classifier")
st.write("Upload an image and the app will classify it using a Hugging Face model.")
st.write("---")

# ---- Model Loading ----
# Use a pre-trained image classification model from Hugging Face
# This is a very small model, perfect for a quick demo.
try:
    classifier = pipeline("image-classification", model="google/vit-base-patch16-224")
except Exception as e:
    st.error(f"Error loading model: {e}")
    st.info("The model may be a large file. Please ensure you have a stable internet connection.")
    classifier = None

# ---- Image Upload & Processing ----
uploaded_file = st.file_uploader(
    "Choose an image...",
    type=["jpg", "jpeg", "png", "webp"],
    help="Upload an image file to classify."
)

if uploaded_file is not None:
    try:
        # Display the uploaded image
        image = Image.open(uploaded_file).convert("RGB")
        st.image(image, caption="Uploaded Image", use_column_width=True)
        st.write("")
        st.write("### Classifying...")
        
        if classifier:
            # Perform the classification
            with st.spinner("Analyzing image..."):
                predictions = classifier(image)

            st.write("### Prediction Results:")
            for p in predictions:
                st.write(f"- **{p['label']}**: {p['score']:.2f}%")
        else:
            st.warning("Model could not be loaded. Please try again.")

    except Exception as e:
        st.error(f"An error occurred during processing: {e}")
        st.info("Please make sure the uploaded file is a valid image.")

st.write("---")
st.write("Built with ❤️ using Streamlit and Hugging Face.")
st.write("[Learn more about Hugging Face](https://huggingface.co/)")
st.write("[Learn more about Streamlit](https://streamlit.io/)")
