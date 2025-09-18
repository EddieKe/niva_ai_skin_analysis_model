# # convert_to_tflite.py
# import tensorflow as tf
# import os

# def convert_keras_to_tflite(keras_model_path, tflite_model_path):
#     """Converts a .keras model to an optimized .tflite model."""
#     try:
#         model = tf.keras.models.load_model(keras_model_path)
#         converter = tf.lite.TFLiteConverter.from_keras_model(model)

#         # This enables optimization to reduce the file size
#         converter.optimizations = [tf.lite.Optimize.DEFAULT]

#         tflite_model = converter.convert()

#         with open(tflite_model_path, 'wb') as f:
#             f.write(tflite_model)
#         print(f"✅ Successfully converted {keras_model_path} to {tflite_model_path}")
#     except Exception as e:
#         print(f"❌ Failed to convert {keras_model_path}: {e}")

# # Define the paths for your models
# models_dir = './models'
# skin_model_keras = os.path.join(models_dir, 'skin_model.keras')
# acne_model_keras = os.path.join(models_dir, 'acne_model.keras')
# skin_model_tflite = os.path.join(models_dir, 'skin_model.tflite')
# acne_model_tflite = os.path.join(models_dir, 'acne_model.tflite')

# # Run the conversion for both models
# convert_keras_to_tflite(skin_model_keras, skin_model_tflite)
# convert_keras_to_tflite(acne_model_keras, acne_model_tflite)


# import tensorflow as tf

# def convert_saved_model_to_tflite(model_dir, tflite_path):
#     """Converts a SavedModel directory directly to a .tflite file."""
#     try:
#         print(f"Converting from {model_dir} to {tflite_path}...")
#         converter = tf.lite.TFLiteConverter.from_saved_model(model_dir)
#         converter.optimizations = [tf.lite.Optimize.DEFAULT]
#         tflite_model = converter.convert()

#         with open(tflite_path, 'wb') as f:
#             f.write(tflite_model)
#         print(f"✅ Successfully created {tflite_path}")
#     except Exception as e:
#         print(f"❌ Failed to convert {model_dir}: {e}")

# # Define paths
# skin_model_dir = './models/skin_model'
# acne_model_dir = './models/acne_model'
# skin_model_tflite = './models/skin_model.tflite'
# acne_model_tflite = './models/acne_model.tflite'

# # Run conversions
# convert_saved_model_to_tflite(skin_model_dir, skin_model_tflite)
# convert_saved_model_to_tflite(acne_model_dir, acne_model_tflite)





# convert_to_tflite.py
import tensorflow as tf
import os
import numpy as np
from PIL import Image

def representative_dataset_generator():
    """Generates a representative dataset from sample images."""
    for filename in os.listdir('./sample_images'):
        if filename.endswith(('.png', '.jpg', '.jpeg')):
            img_path = os.path.join('./sample_images', filename)
            img = Image.open(img_path).resize((224, 224))
            img_array = np.array(img, dtype=np.float32)
            img_tensor = np.expand_dims(img_array, axis=0)
            img_tensor /= 255.0
            yield [img_tensor]

def convert_and_quantize(model_dir, tflite_path):
    """Converts and quantizes a SavedModel to a .tflite file."""
    try:
        print(f"Converting and quantizing from {model_dir} to {tflite_path}...")
        converter = tf.lite.TFLiteConverter.from_saved_model(model_dir)

        # --- Quantization Settings ---
        converter.optimizations = [tf.lite.Optimize.DEFAULT]
        converter.representative_dataset = representative_dataset_generator
        converter.target_spec.supported_ops = [tf.lite.OpsSet.TFLITE_BUILTINS_INT8]
        converter.inference_input_type = tf.float32  # Input is still float32
        converter.inference_output_type = tf.float32 # Output is still float32
        # --- End Quantization ---

        tflite_model = converter.convert()

        with open(tflite_path, 'wb') as f:
            f.write(tflite_model)
        print(f"✅ Successfully created quantized model: {tflite_path}")
    except Exception as e:
        print(f"❌ Failed to convert {model_dir}: {e}")

# Define paths
skin_model_dir = './models/skin_model'
acne_model_dir = './models/acne_model'
skin_model_tflite = './models/skin_model.tflite'
acne_model_tflite = './models/acne_model.tflite'

# Run conversions
convert_and_quantize(skin_model_dir, skin_model_tflite)
convert_and_quantize(acne_model_dir, acne_model_tflite)