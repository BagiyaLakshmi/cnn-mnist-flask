from flask import Flask, render_template, request 
import pickle 
from PIL import Image
import numpy as np


app = Flask(__name__)

model = pickle.load(open("model1.pkl", 'rb'))

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/upload", methods=['post'])
def pred():
    file = request.files['image']

    labels ={
        0:"Zero", 1:"One", 2:"Two", 3:"Three", 4:"Four",
        5:"Five", 6:"Six", 7:"Seven", 8:"Eight", 9:"Nine"
    }

    file = Image.open(file.stream)
    file = file.convert("L")
    file = file.resize((28,28))
    file = np.array(file) 

    pred = model.predict(file.reshape(1, 28, 28, 1) )

    labidx = np.argmax(pred)

    
    return render_template("success.html",
                           data=labels[labidx])

if __name__ =='__main__':
    app.run()
