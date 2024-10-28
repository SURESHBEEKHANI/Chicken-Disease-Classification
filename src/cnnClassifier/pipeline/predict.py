import numpy as np
from tensorflow.keras.models import load_model  # type: ignore
from tensorflow.keras.preprocessing import image  # type: ignore
import os

class PredictionPipeline:
    """
    A pipeline for predicting Coccidiosis in poultry images using a pre-trained model.
    
    Attributes:
        filename (str): The path to the image file to be classified.
    """
    
    def __init__(self, filename: str):
        """
        Initializes the PredictionPipeline with the image filename.
        
        Args:
            filename (str): Path to the image file.
        """
        self.filename = filename

    def load_model(self):
        """
        Loads the trained model from the specified path.
        
        Returns:
            model: The loaded Keras model.
        """
        model_path = os.path.join("artifacts", "training", "model.h5")
        try:
            model = load_model(model_path)
            return model
        except Exception as e:
            raise FileNotFoundError(f"Failed to load model. Ensure the model exists at '{model_path}'. Error: {e}")

    def preprocess_image(self):
        """
        Loads and preprocesses the image to prepare it for model prediction.
        
        Returns:
            np.array: The preprocessed image array.
        """
        try:
            img = image.load_img(self.filename, target_size=(224, 224))
            img_array = image.img_to_array(img)
            img_array = np.expand_dims(img_array, axis=0)
            return img_array
        except Exception as e:
            raise ValueError(f"Error in processing image. Ensure the image file is valid and accessible. Error: {e}")

    def predict(self):
        """
        Runs the prediction pipeline on the input image.
        
        Returns:
            list: A dictionary with the prediction result.
        """
        model = self.load_model()
        img_array = self.preprocess_image()
        
        result = np.argmax(model.predict(img_array), axis=1)
        prediction = 'Healthy' if result[0] == 1 else 'Coccidiosis'
        
        return [{"image": prediction}]
