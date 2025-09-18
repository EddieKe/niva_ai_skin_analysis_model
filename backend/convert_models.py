# convert_models.py
import tensorflow as tf

def convert_and_save(model_path, output_path):
    try:
        model = tf.keras.models.load_model(model_path)
        # Add this line to remove the incompatible optimizer state
        model.compile(optimizer=model.optimizer)
        
        # Now save the model
        model.save(output_path, save_format='keras', include_optimizer=False)
        print(f"✅ Successfully converted {model_path} to {output_path} (inference only)")
    except Exception as e:
        print(f"❌ Failed to convert {model_path}: {e}")

# Run the conversion for both models
convert_and_save('./models/skin_model', './models/skin_model.keras')
convert_and_save('./models/acne_model', './models/acne_model.keras')