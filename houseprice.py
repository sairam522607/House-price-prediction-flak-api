from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

model = pickle.load(open('housepricemodel.sav','rb'))

@app.route('/houseprice')
def home():
  result = ''
  return render_template("house_index.html", **locals())


@app.route('/predict', methods=['POST','GET'])
def predict():
  SqFt=float(request.form['SqFt'])
  Bedrooms = request.form['Bedrooms']
  Bathrooms = request.form['Bathrooms']
  Offers = float(request.form['Offers'])
  Brick = 1 if request.form['Brick'].lower() == 'yes' else 0
  
  input_data = np.array([[SqFt, Bedrooms, Bathrooms, Offers, Brick]], dtype=np.float32)
  result = model.predict(input_data)[0]

  #result = model.predict([[SqFt, Bedrooms, Bathrooms, Offers, Brick]])[0]
  return render_template("house_index.html", **locals())


if __name__ == '__main__':
  app.run(debug = True)