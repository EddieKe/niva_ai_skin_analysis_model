#!/bin/bash

echo "--- STEP 1: Setting up legacy environment to convert models ---"
pyenv local 3.9.18
source legacy_venv/bin/activate

echo "--- STEP 2: Converting models to .keras format ---"
# FIXED: Use the correct filename
python convert_models.py

echo "--- STEP 3: Verifying that .keras files were created ---"
ls -l models/

echo "--- STEP 4: Deactivating legacy environment ---"
deactivate

echo "--- STEP 5: Activating and setting up main application environment ---"
source venv/bin/activate

# ADDED: Install all required dependencies into the main venv
echo "--- Installing dependencies from requirements.txt ---"
pip install -r requirements.txt

echo "--- STEP 6: Starting the Flask application ---"
python app.py