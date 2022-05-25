from tensorflow.keras.applications import MobileNetV2
import matplotlib.pyplot as plt
from app import app
import urllib.request
from flask import Flask, flash, request, redirect, jsonify, render_template, send_file
from werkzeug.utils import secure_filename
from faceinpainting import preprocess,model
import os

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])

def allowed_file(filename):
	return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
	
@app.route('/')
def upload_form():
	return render_template('output.html')

@app.route('/main.css')
def file_downloads():
	try:
		return send_file('templates/main.css')
	except Exception as e:
		return str(e)

@app.route('/b.jpg')
def view_file():
	try:
		return send_file('static/b.jpg')
	except Exception as e:
		return str(e)

@app.route('/', methods=['POST'])
def upload_image():
	if 'file' not in request.files:
		flash('No file part')
		return redirect(request.url)
	file = request.files['file']
	if file.filename == '':
		flash('No image selected for uploading')
		return redirect(request.url)
	if file and allowed_file(file.filename):
		filename = secure_filename(file.filename)
		file.save(os.path.join(app.config['UPLOAD_FOLDER'], "a.jpg"))
		
		model()
		a = {'name': 'nabin khadka'}
		return jsonify(a)
	else:
		flash('Allowed image types are -> png, jpg, jpeg, gif')
		return redirect(request.url)

# @app.route('/output.html')
# def home():
#    return render_template('output.html')
# def display_image(filename):
# 	#print('display_image filename: ' + filename)
# 	return redirect(url_for('static', filename='/' + a.jpg), code=301)

if __name__ == "__main__":
    app.run()
    # return render_template("ui.html")
