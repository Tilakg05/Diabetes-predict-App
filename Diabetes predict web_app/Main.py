import numpy as np
from flask import Flask, request, render_template, url_for

import pickle

main = Flask(__name__)

model = pickle.load(open("modelSVM.pkl", "rb"))

@main.route("/")
def general():
    return render_template("General.html")

@main.route("/infodiabete")
def infodiabetes():
    return render_template("InfoDiabetes.html")    

@main.route("/symptoms")
def symptoms():
    return render_template("Symptoms.html ")

@main.route("/prediabetes")
def prediabetes():
    return render_template("PreDiabetes.html ")

@main.route("/contact")
def contact():
    return render_template("contact.html")    

@main.route('/predict',methods=['POST'])
def predict():
   if request.method == 'POST': 
    int_features = [int(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)

    if prediction == 2:
        pred = "You have Diabetes!"
    elif prediction == 1:
        pred = "You have a Pre-Dibaties!"
    elif prediction == 0:
        pred = "You don't have Diabetes!"
    
    output = pred
    
    return render_template('general.html', prediction_text='Predicted Class: {}'.format(output))


if __name__ == "__main__":
    main.run(debug=True)