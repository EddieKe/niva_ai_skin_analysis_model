import os
from typing import List
import numpy as np
from PIL import Image
import tensorflow as tf
# import tflite_runtime.interpreter as tflite

import cv2
import numpy as np
from PIL import Image
from io import BytesIO


from flask import Flask, request
import werkzeug
from models.recommender.rec import recs_essentials, makeup_recommendation

from io import BytesIO
from PIL import Image
from stone.api import process as stone_process
from stone.utils import ArgumentError
import cv2
from flask import jsonify
from flask_cors import CORS

app = Flask(__name__) 
CORS(app)
# api = Api(app)

# class_names1 = ['Dry_skin', 'Normal_skin', 'Oil_skin']
# class_names2 = ['Low', 'Moderate', 'Severe']
# skin_tone_dataset = 'models/skin_tone/skin_tone_dataset.csv'


# --- Global variables to hold the loaded models ---
# model1 = None
# model2 = None




# import tensorflow as tf

# --- Global variables to hold the loaded models ---
# model1 = None
# model2 = None

# def get_model():
#     """Loads the skin type and acne models using absolute paths."""
#     global model1, model2

#     # Get the absolute path to the directory where this script (app.py) is located
#     base_dir = os.path.dirname(os.path.abspath(__file__))

#     # Construct the full, absolute paths to the model files
#     model1_path = os.path.join(base_dir, 'models', 'skin_model.keras')
#     model2_path = os.path.join(base_dir, 'models', 'acne_model.keras')

#     if model1 is None:
#         try:
#             print(f"Attempting to load skin type model from: {model1_path}")
#             model1 = tf.keras.models.load_model(model1_path)
#             print('✅ Skin type model loaded successfully.')
#         except Exception as e:
#             print(f"❌ Error loading skin type model: {e}")
#             exit()

#     if model2 is None:
#         try:
#             print(f"Attempting to load acne model from: {model2_path}")
#             model2 = tf.keras.models.load_model(model2_path)
#             print("✅ Acne model loaded successfully.")
#         except Exception as e:
#             print(f"❌ Error loading acne model: {e}")
#             exit()

# app.py

# ... (other imports)

# --- Global variables for TFLite interpreters ---
interpreter1 = None
interpreter2 = None

def get_model():
    """Loads the TFLite models and allocates tensors."""
    global interpreter1, interpreter2
    base_dir = os.path.dirname(os.path.abspath(__file__))
    model1_path = os.path.join(base_dir, 'models', 'skin_model.tflite')
    model2_path = os.path.join(base_dir, 'models', 'acne_model.tflite')

    try:
        print(f"Attempting to load TFLite model from: {model1_path}")
        interpreter1 = tf.lite.Interpreter(model_path=model1_path)
        interpreter1.allocate_tensors()
        print('✅ Skin type TFLite model loaded.')
    except Exception as e:
        print(f"❌ Error loading skin type TFLite model: {e}")
        exit()

    try:
        print(f"Attempting to load TFLite model from: {model2_path}")
        interpreter2 = tf.lite.Interpreter(model_path=model2_path)
        interpreter2.allocate_tensors()
        print('✅ Acne TFLite model loaded.')
    except Exception as e:
        print(f"❌ Error loading acne TFLite model: {e}")
        exit()

def prediction_skin(img_tensor):
    """Predicts skin type using the TFLite interpreter."""
    input_details = interpreter1.get_input_details()
    output_details = interpreter1.get_output_details()
    
    interpreter1.set_tensor(input_details[0]['index'], img_tensor)
    interpreter1.invoke()
    
    pred = interpreter1.get_tensor(output_details[0]['index'])
    probabilities = tf.nn.softmax(pred[0])
    return probabilities

def prediction_acne(img_tensor):
    """Predicts acne severity using the TFLite interpreter."""
    input_details = interpreter2.get_input_details()
    output_details = interpreter2.get_output_details()

    interpreter2.set_tensor(input_details[0]['index'], img_tensor)
    interpreter2.invoke()

    pred = interpreter2.get_tensor(output_details[0]['index'])
    probabilities = tf.nn.softmax(pred[0])
    return probabilities

# ... (the rest of your app.py code stays the same)

# def get_model():
#     """Loads the original SavedModel FOLDERS directly using TFSMLayer."""
#     global model1, model2

#     base_dir = os.path.dirname(os.path.abspath(__file__))

#     # Point to the ORIGINAL model FOLDERS
#     model1_path = os.path.join(base_dir, 'models', 'skin_model')
#     model2_path = os.path.join(base_dir, 'models', 'acne_model')

#     if model1 is None:
#         try:
#             print(f"Attempting to load skin type model from FOLDER: {model1_path}")
#             # Wrap the old model in a TFSMLayer
#             model1 = tf.keras.Sequential([
#                 tf.keras.layers.TFSMLayer(model1_path, call_endpoint='serving_default')
#             ])
#             print('✅ Skin type model loaded successfully.')
#         except Exception as e:
#             print(f"❌ Error loading skin type model: {e}")
#             exit()

#     if model2 is None:
#         try:
#             print(f"Attempting to load acne model from FOLDER: {model2_path}")
#             # Wrap the old model in a TFSMLayer
#             model2 = tf.keras.Sequential([
#                 tf.keras.layers.TFSMLayer(model2_path, call_endpoint='serving_default')
#             ])
#             print("✅ Acne model loaded successfully.")
#         except Exception as e:
#             print(f"❌ Error loading acne model: {e}")
#             exit()

# app.py

def load_image_for_tf(img_bytes):
    """Prepares image from bytes for TensorFlow model prediction by resizing and normalizing."""
    # 1. Load image from bytes and convert to RGB
    img_pil = Image.open(BytesIO(img_bytes)).convert("RGB")

    # 2. Resize to the model's expected input size
    img_resized = img_pil.resize((224, 224))

    # 3. Convert to a NumPy array
    img_array = np.array(img_resized)

    # 4. Add a batch dimension
    img_tensor = np.expand_dims(img_array, axis=0)

    # 5. Normalize and cast to the correct float32 type
    img_tensor = (img_tensor / 255.0).astype(np.float32)

    return img_tensor

# def load_image_for_tf(img_bytes):
#     """Prepares image from bytes for TensorFlow model prediction with advanced preprocessing."""
#     # 1. Load image from bytes into an OpenCV format
#     nparr = np.frombuffer(img_bytes, np.uint8)
#     img_cv = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
#     # OpenCV loads images in BGR format, so we convert to RGB
#     img_rgb = cv2.cvtColor(img_cv, cv2.COLOR_BGR2RGB)

#     # --- ADVANCED PREPROCESSING STARTS HERE ---

#     # 2. Color Correction (Gray World Algorithm)
#     # This helps to remove color casts caused by ambient lighting
#     avg_r, avg_g, avg_b = np.mean(img_rgb, axis=(0, 1))
#     avg_gray = (avg_r + avg_g + avg_b) / 3
#     # Apply scaling factors to each channel to balance them
#     scale_r, scale_g, scale_b = avg_gray / avg_r, avg_gray / avg_g, avg_gray / avg_b
#     img_rgb[:, :, 0] = np.clip(img_rgb[:, :, 0] * scale_r, 0, 255)
#     img_rgb[:, :, 1] = np.clip(img_rgb[:, :, 1] * scale_g, 0, 255)
#     img_rgb[:, :, 2] = np.clip(img_rgb[:, :, 2] * scale_b, 0, 255)
    
#     # 3. Lighting Normalization (CLAHE)
#     # This enhances local contrast and normalizes lighting across the image
#     img_lab = cv2.cvtColor(img_rgb.astype(np.uint8), cv2.COLOR_RGB2LAB)
#     l_channel, a_channel, b_channel = cv2.split(img_lab)
#     clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
#     cl = clahe.apply(l_channel)
#     merged = cv2.merge([cl, a_channel, b_channel])
#     processed_img = cv2.cvtColor(merged, cv2.COLOR_LAB2RGB)
    
#     # --- ADVANCED PREPROCESSING ENDS HERE ---

#     # 4. Final Preparation for TensorFlow
#     # Resize and normalize the processed image
#     img_pil = Image.fromarray(processed_img)
#     img_resized = img_pil.resize((224, 224))
#     img_tensor = np.array(img_resized)
#     img_tensor = np.expand_dims(img_tensor, axis=0)
#     img_tensor = img_tensor / 255.0  # Normalize to [0, 1]

#     # FIX: Normalize AND cast to the correct float32 type
#     img_tensor = (img_tensor / 255.0).astype(np.float32)
    
#     return img_tensor

# def map_skin_tone_value(tone_value):
#     if tone_value == 1:
#         return 'fair'
#     elif tone_value == 2:
#         return 'light to medium'
#     elif tone_value == 3:
#         return 'medium to dark'
#     elif tone_value == 4:
#         return 'dark to deep'
#     elif tone_value == 5:
#         return 'deep'
#     else:
#         return 'unknown' # Handle any unexpected values



# if __name__ == '__main__':
#     app.run(debug=True)



# def prediction_skin(img_tensor):
#     """Predicts skin type probabilities from an image tensor."""
#     pred = model1(img_tensor)
#     probabilities = tf.nn.softmax(pred[0])
#     return probabilities # Return the full probability tensor

# def prediction_acne(img_tensor):
#     """Predicts acne severity probabilities from an image tensor."""
#     pred = model2(img_tensor)
#     probabilities = tf.nn.softmax(pred[0])
#     return probabilities # Return the full probability tensor


# --- Recommendation Logic ---
def generate_routine(skin_type, acne_type):
    morning_routine = ["Cleanser", "Moisturizer", "Sunscreen"]
    evening_routine = ["Cleanser", "Moisturizer"]

    if 'Dry' in skin_type:
        morning_routine[0] = "Cream-based Cleanser"
        evening_routine[0] = "Oil-based Cleanser"
        evening_routine[1] = "Night Cream"

    elif 'Oil' in skin_type:
        morning_routine[0] = "Gel-based Cleanser"
        evening_routine[0] = "Foam Cleanser"
        morning_routine.insert(1, "Serum")  # Add a serum step

    # Add more logic for acne_type
    if 'Severe' in acne_type:
        # Insert a spot treatment step for severe acne
        evening_routine.insert(1, "Spot Treatment")
    
    # You can add more complex logic for other skin types and acne levels.
    
    return {
        "morning": morning_routine,
        "evening": evening_routine
    }






@app.route('/analyze', methods=['POST'])
def analyze_skin():
    """Handles image upload and returns a full skin analysis with recommendations."""
    if 'image' not in request.files:
        return jsonify({'error': 'No image file provided'}), 400

    file = request.files['image']
    
    # Create the full, absolute path for the temporary file
    from werkzeug.utils import secure_filename
    base_dir = os.path.abspath(os.path.dirname(__file__))
    temp_filename = secure_filename(file.filename or 'temp_image.png')
    temp_filepath = os.path.join(base_dir, temp_filename)
    
    file.save(temp_filepath)

    try:
        # --- 1. Read file bytes ---
        img_bytes = open(temp_filepath, 'rb').read()

        # --- 2. Skin Type and Acne Analysis ---
        try:
            img_tensor = load_image_for_tf(img_bytes)
            
            # --- Skin Type Analysis with Combination Logic ---
            skin_type_classes = ['Dry', 'Normal', 'Oily']
            skin_probs = prediction_skin(img_tensor).numpy() # Convert tensor to numpy array
            
            oily_prob = skin_probs[2]  # Corresponds to 'Oily_skin'
            dry_prob = skin_probs[0]   # Corresponds to 'Dry_skin'
            
            # Heuristic rule for "Combination" skin
            if oily_prob > 0.35 and dry_prob > 0.35:
                skin_type = 'Combination'
            else:
                top_skin_index = np.argmax(skin_probs)
                skin_type = skin_type_classes[top_skin_index]

            # --- Acne Analysis with Confidence Score ---
            acne_classes = ['Low', 'Moderate', 'Severe']
            acne_probs = prediction_acne(img_tensor).numpy()
            top_acne_index = np.argmax(acne_probs)
            
            acne_analysis = {
                'label': acne_classes[top_acne_index],
                'confidence': float(acne_probs[top_acne_index])
            }

        except Exception as e:
            print(f"Error during TF model prediction: {e}")
            return jsonify({'error': 'Failed to analyze skin type or acne.'}), 500

        # --- 3. Skin Tone Analysis ---
        try:
            results = stone_process(temp_filepath, return_report_image=False)
            if not results or not results.get('faces'):
                return jsonify({'error': 'No face detected in the image.'}), 400

            face_data = results['faces'][0]
            dominant_colors = face_data.get('dominant_colors', [])

            # Find the dominant color with the highest percentage
            if dominant_colors:
                # We cast percent to float to ensure correct sorting
                top_dominant_color = max(dominant_colors, key=lambda x: float(x.get('percent', 0)))
                
                # Construct the skin tone info using the most dominant color
                skin_tone_info = {
                    'color_hex': top_dominant_color.get('color'),
                    'label': 'Dominant Tone',
                    'accuracy': float(top_dominant_color.get('percent')),
                    'dominant_colors': dominant_colors
                }
            else:
                # Fallback in case no dominant colors are found
                skin_tone_info = {
                    'color_hex': '#FFFFFF',
                    'label': 'Not Detected',
                    'accuracy': 0.0,
                    'dominant_colors': []
                }

        except Exception as e:
            print(f"Error during skin tone analysis: {e}")
            return jsonify({'error': 'Failed to analyze skin tone.'}), 500

        # --- 4. Generate Recommendations ---
        skincare_routine = generate_routine(skin_type, acne_analysis)
        makeup_recs = makeup_recommendation(skin_tone_info['label'], skin_type)
        
        # --- 5. Construct Final JSON Response ---
        response_data = {
            'analysis': {
                'skin_type': skin_type,
                'acne_severity': acne_analysis,
                'skin_tone': skin_tone_info
            },
            'recommendations': {
                'skincare_routine': skincare_routine,
                'makeup': makeup_recs
            }
        }
        return jsonify(response_data), 200

    finally:
        # --- CLEANUP ---
        # This block will always execute, ensuring the file is deleted once.
        if os.path.exists(temp_filepath):
            os.remove(temp_filepath)

# --- Main Execution ---
if __name__ == '__main__':
    get_model()  # Load models only once at startup
    # app.run(debug=True, port=5000)
    app.run(host='0.0.0.0', port=5000, debug=False)


@app.route('/')
def health_check():
    return "OK", 200