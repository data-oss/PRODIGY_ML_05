from flask import Flask, request, render_template
import tensorflow as tf
import numpy as np
from PIL import Image
import os

app = Flask(__name__)

model = tf.keras.models.load_model("food_model.h5")
food_classes = ["apple_pie", "baby_back_ribs", "baklava", "beef_carpaccio", "beef_tartare", "beet_salad", "beignets",
                "bibimbap", "bread_pudding", "breakfast_burrito", "bruschetta", "caesar_salad", "cannoli", "caprese_salad",
                "carrot_cake"]

calorie_dict = {"apple_pie": 265, "hamburger": 295, "pizza": 266, "sushi": 150, "tacos": 226, "spaghetti_bolognese": 185}

def preprocess_image(image_path):
    """Preprocess image for prediction."""
    img = Image.open(image_path).convert("RGB")
    img = img.resize((224, 224))
    img = np.array(img) / 255.0
    img = np.expand_dims(img, axis=0)
    return img

@app.route("/", methods=["GET", "POST"])
def upload_predict():
    if request.method == "POST":
        image_file = request.files["image"]
        if image_file:
            image_path = "uploads/" + image_file.filename
            image_file.save(image_path)

            img = preprocess_image(image_path)
            predictions = model.predict(img)
            class_index = np.argmax(predictions)
            food_name = food_classes[class_index]
            estimated_calories = calorie_dict.get(food_name, "Unknown")

            return f"Predicted Food: {food_name}, Estimated Calories: {estimated_calories} kcal"

    return '''
    <form method="post" enctype="multipart/form-data">
        Upload Food Image: <input type="file" name="image">
        <input type="submit">
    </form>
    '''

if __name__ == "__main__":
    os.makedirs("uploads", exist_ok=True) 
    app.run(debug=True)
