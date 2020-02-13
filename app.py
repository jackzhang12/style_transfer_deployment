import numpy as np 
import os
from flask import Flask, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename


app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def main_page():
    if request.method == 'POST':
        fileM = request.files['output']
        fileS = request.files['output2']
        filename = secure_filename(fileM.filename)
        filename2 = secure_filename(fileS.filename)
        file.save(os.path.join('uploads', filename))
        file.save(os.path.join('uploads', filename))

        return redirect(url_for('prediction', filename=filename,filename=filename2 ))
    return render_template('index.html')


@app.route("/aijfisj")
def hello():
	return "Hello World! pls change"

if __name__ == "__main__":
	app.run()

@app.route('/prediction/<filename>')
def prediction(filename, filename2):
    
    return render_template('results.html')
