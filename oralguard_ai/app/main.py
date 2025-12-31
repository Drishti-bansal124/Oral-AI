from fastapi import FastAPI, File, UploadFile
from PIL import Image
import numpy as np
import io
import tensorflow as tf

app = FastAPI()

# Load model ONCE at startup
model = tf.keras.models.load_model("app/model/model.h5")

class_names = ["Normal", "Premalignant", "Malignant"]

@app.get("/")
def home():
    return {"message": "OralGuard AI backend is running"}

@app.post("/predict")
def predict_image(file: UploadFile = File(...)):
    # Read image bytes
    image_bytes = file.file.read()
    image = Image.open(io.BytesIO(image_bytes)).convert("RGB")

    # Resize to model input size
    image = image.resize((224, 224))

    # Convert to numpy & normalize
    image_array = np.array(image) / 255.0
    image_array = np.expand_dims(image_array, axis=0)

    # Predict
    predictions = model.predict(image_array)
    predicted_index = int(np.argmax(predictions))
    confidence = float(np.max(predictions))

    return {
        "prediction": class_names[predicted_index],
        "confidence": round(confidence, 3),
        "disclaimer": "AI-based screening support only. Not a medical diagnosis."
    }
