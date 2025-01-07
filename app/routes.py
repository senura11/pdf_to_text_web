from app import app  # Import the app instance
from flask import render_template, request, redirect, url_for, flash, send_file
import os
from app.pdf_converter import pdf_to_text
from app.ocr_converter import pdf_to_text_ocr

ALLOWED_EXTENSIONS = {'pdf'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file selected')
            return redirect(request.url)

        file = request.files['file']
        if file.filename == '':
            flash('No file selected')
            return redirect(request.url)

        if file and allowed_file(file.filename):
            filename = file.filename
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(file_path)

            use_ocr = 'ocr' in request.form
            output_path = os.path.join(app.config['UPLOAD_FOLDER'], 'output.txt')

            try:
                if use_ocr:
                    pdf_to_text_ocr(file_path, output_path)
                else:
                    pdf_to_text(file_path, output_path)

                with open(output_path, 'r', encoding='utf-8') as f:
                    text = f.read()

                return render_template('index.html', text=text, filename=filename)
            except Exception as e:
                flash(f'Error: {str(e)}')
                return redirect(request.url)

    return render_template('index.html')

@app.route('/download')
def download():
    output_path = os.path.join(app.config['UPLOAD_FOLDER'], 'output.txt')
    return send_file(output_path, as_attachment=True)
