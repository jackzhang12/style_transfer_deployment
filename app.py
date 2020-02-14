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
        fileM.save(os.path.join('uploads', filename))
        fileS.save(os.path.join('uploads', filename2))

        return redirect(url_for('prediction', filename=filename, filename=filename2)) #im not sure how python parameters work
    return render_template('index.html')


@app.route("/aijfisj")
def hello():
	return "Hello World! pls change"



@app.route('/prediction/<filename>/<filename2>') #this is just a guess, need to look into how this works
def prediction(filename, filename2): #i think this is where the parameters are accepted
    main_image = plt.imread(os.path.join('uploads', filename))
    style_image = plt.imread(os.path.join('uploads', filename2))

    return render_template('results.html')












if __name__ == "__main__":
	app.run()