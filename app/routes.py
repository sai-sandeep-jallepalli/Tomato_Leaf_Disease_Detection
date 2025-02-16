from flask import Blueprint, render_template, request, redirect, url_for, flash
import os
import tempfile
from werkzeug.utils import secure_filename

# Create a blueprint named 'main'
main = Blueprint('main', __name__)

@main.route('/', methods=['GET', 'POST'])
def index():
    
    if request.method == 'POST':
        if 'image' not in request.files:
            flash('No image part in the request.')
            return redirect(request.url)
        
        file = request.files['image']
        if file.filename == '':
            flash('No file selected for uploading.')
            return redirect(request.url)
        
        
        allowed_extensions = {'png', 'jpg', 'jpeg', 'gif'}
        
        if '.' in file.filename:
            ext = file.filename.rsplit('.', 1)[1].lower()
            if ext not in allowed_extensions:
                flash('Unsupported file extension.')
                return redirect(request.url)
            
        else:
            flash('File does not have an extension.')
            return redirect(request.url)
        
        temp_dir = tempfile.mkdtemp()
        filename = secure_filename(file.filename)
        temp_path = os.path.join(temp_dir, filename)
        file.save(temp_path)
        
        from detect import detect_image
        prediction = detect_image(temp_path)
        
        os.remove(temp_path)
        os.rmdir(temp_dir)
        
        return render_template('index.html', prediction=prediction)
    
    return render_template('index.html')
