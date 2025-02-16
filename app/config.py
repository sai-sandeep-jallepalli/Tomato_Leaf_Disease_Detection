import os

CONFIG = {
    
    'SECRET_KEY': 'your_secret_key_here',
    
    'BASE_DIR': os.path.abspath(os.path.dirname(__file__)),
    
    'UPLOAD_FOLDER': os.path.join(os.path.abspath(os.path.dirname(__file__)), 'static', 'uploads'),
    
    'DATASET_URL' : os.environ.get('DATASET_URL', 'https://drive.google.com/uc?id=1f6Jq3vk8V6z4wzGqDdXQsT51RN-l2fHj'),
    
    'DATASET_PATH': os.path.join(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')), 'dataset'),
    
    'MODEL_PATH': os.path.join(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')), 'model.h5'),
    
    'IMAGE_SIZE': (128, 128),
    
    'BATCH_SIZE': 32,
    
    'EPOCHS': 10
    
}