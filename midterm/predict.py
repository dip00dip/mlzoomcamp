import pickle

from flask import Flask
from flask import request
from flask import jsonify


dv_file = "dict_vect.pkl"

with open(dv_file, 'rb') as f_in: 
    dv = pickle.load(f_in)

model_file = "model_rf.pkl"

with open(model_file, 'rb') as f_in: 
    model = pickle.load(f_in)

app = Flask('credit')

@app.route('/predict', methods=['POST'])
def predict():
    wine = request.get_json()

    X = dv.transform([wine])
    y_pred = model.predict(X)

    result = {
      'wine_price': float(y_pred),
    }

    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=9696)
