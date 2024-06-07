import pickle 
from flask import Flask,render_template,request
from sklearn.preprocessing import StandardScaler

app = Flask(__name__)

scaler = pickle.load(open("models/standardscaler.pkl", "rb"))
model = pickle.load(open("models/predictionmodel.pkl", "rb"))


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict',methods=['GET', 'POST'])
def predict_datapoint():
    result=''
    if request.method == 'POST':
        Pregnancies = int(request.form.get('Pregnancies'))
        Glucose = int(request.form.get('Glucose'))
        BloodPressure = int(request.form.get('BloodPressure'))
        SkinThickness = int(request.form.get('SkinThickness'))
        Insulin = int(request.form.get('Insulin'))
        BMI = int(request.form.get('BMI'))
        DiabetesPedigreeFunction = int(request.form.get('DiabetesPedigreeFunction'))
        Age = float(request.form.get("Age"))


        
        new_data = scaler.transform([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
        predict = model.predict(new_data)

        if predict[0] == 1:
            result = 'Diabetic'
        else:
            result = 'Non-Diabetic'
        
        return render_template('predict.html', result=result)
    else:
        return render_template('predict.html')

if __name__ == '__main__':
    app.run(debug=True)