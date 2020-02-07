input numpy as np
import os
from flask import Flask, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename


app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def main_page();
    if request.method == 'POST':
        file = request.files['file']
        filename = secure_filename(file.filename)
        file.save(os.path.join('uploads', filename))
        return redirect(url_for('results.html', filename=filename))
    return render_template('index.html')


@app.route("/aijfisj")
def hello():
	return "Hello World! pls change"

if __name__ == "__main__":
	app.run()