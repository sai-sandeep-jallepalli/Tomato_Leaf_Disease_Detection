import os
import gdown
import zipfile
from .config import CONFIG

def download_dataset():
    if not os.path.exists(CONFIG['DATASET_PATH']):
        os.makedirs(CONFIG['DATASET_PATH'], exist_ok=True)
        
    zip_path = os.path.join(CONFIG['DATASET_PATH'], 'dataset.zip')
    
    if not os.path.exists(zip_path):
        print("Downloading dataset from Google Drive...")
        gdown.download(CONFIG['DATASET_URL'], zip_path, quiet=False)
        
    train_dir = os.path.join(CONFIG['DATASET_PATH'], 'Tomato', 'train')
    val_dir = os.path.join(CONFIG['DATASET_PATH'], 'Tomato', 'validation')
    
    if not (os.path.exists(train_dir) and os.path.exists(val_dir)):
        print("Extracting dataset...")
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall(CONFIG['DATASET_PATH'])



