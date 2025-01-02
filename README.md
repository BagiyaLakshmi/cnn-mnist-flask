# CNN-MNIST-Flask

This project is a simple Flask web application that utilizes a Convolutional Neural Network (CNN) model to classify images of handwritten digits (0-9) from the MNIST dataset. Users can upload an image of a digit, and the application will predict the digit's class.

## Features
- **Web Interface**: A user-friendly interface for uploading digit images.
- **CNN Model Integration**: Utilizes a pre-trained CNN model for digit classification.
- **Dynamic Results**: Displays the predicted class for the uploaded image.

---

## Prerequisites

Before running the project, ensure you have the following installed:
- Python 3.x
- Flask
- PIL (Pillow)
- NumPy
- scikit-learn (or equivalent for `pickle` support)

---

## Installation and Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/cnn-mnist-flask.git
   cd cnn-mnist-flask
   ```

2. Install dependencies:
   ```bash
   pip install flask pillow numpy
   ```

3. Place your pre-trained model (`model1.pkl`) in the project directory.

4. Ensure the `templates/` folder contains the following HTML files:
   - `home.html`: The homepage with an image upload form.
   - `success.html`: Displays the predicted class.

5. (Optional) Add a `static/` folder for styles (e.g., CSS).

---

## Running the Application

1. Start the Flask server:
   ```bash
   python app.py
   ```

2. Open your browser and navigate to:
   ```
   http://127.0.0.1:5000/
   ```

3. Upload an image of a digit (28x28 pixels, grayscale).

4. View the predicted class on the result page.

---

## File Structure

```
cnn-mnist-flask/
|-- app.py               # Main Flask application
|-- model1.pkl           # Pre-trained CNN model
|-- templates/
|   |-- home.html        # Upload page
|   |-- success.html     # Result page

```

---

## Notes
- The uploaded image is resized to 28x28 pixels and converted to grayscale before prediction.
- Ensure the CNN model expects input in the format `(1, 28, 28, 1)`.
- Update the `labels` dictionary in `app.py` if using a different dataset.

---

## Future Improvements
- Add error handling for invalid file uploads.
- Enhance the user interface with better styling.
- Extend support for different image formats.

---
