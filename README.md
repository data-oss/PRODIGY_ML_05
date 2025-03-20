# Food Recognition and Calorie Estimation

## Overview
This project is a **Food Recognition and Calorie Estimation** system using deep learning. It is a web application built with Flask that allows users to upload food images, predicts the food category, and estimates the calorie content based on a pre-trained deep learning model.

## Features
- **Image Upload**: Users can upload an image of food.
- **Deep Learning Model**: Uses TensorFlow and Keras to classify food images.
- **Preprocessing**: Images are resized and normalized before prediction.
- **Calorie Estimation**: Maps predicted food items to an estimated calorie count.
- **Flask Web Interface**: Simple UI for image upload and prediction display.

## Installation
To run this project locally, follow these steps:

1. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/food-recognition-calories.git
   cd food-recognition-calories
   ```

2. Create and activate a virtual environment (optional but recommended):
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

## Usage
1. Run the Flask app:
   ```sh
   python app.py
   ```
2. Open a browser and go to `http://127.0.0.1:5000/`
3. Upload a food image to get predictions and estimated calorie count.

## Dependencies
Ensure you have the following dependencies installed:
- Python 3.x
- Flask
- TensorFlow / Keras
- NumPy
- PIL (Pillow)
- OpenCV (optional for preprocessing)

## Model Training
- The model used in this project is a deep learning-based image classifier trained on a food dataset.
- The pre-trained model (`food_model.h5`) is loaded for inference.
- The `food_classes` list contains different food categories.

## Calorie Estimation
- A predefined dictionary (`calorie_dict`) is used to estimate calories per food item.
- If the food item is not in the dictionary, it returns "Unknown".

## Future Enhancements
- Expand the dataset for better classification accuracy.
- Use a more extensive calorie database for improved estimation.
- Deploy as a cloud-based service with an interactive UI.

## Contributing
Contributions are welcome! If you have suggestions for improvement, feel free to fork the repository, create a branch, and submit a pull request.

## License
This project is open-source and available under the [MIT License](LICENSE).

## Author
**Dua Zahra**  
GitHub: https://github.com/data-oss

---
Feel free to update this README file with additional insights as needed!

