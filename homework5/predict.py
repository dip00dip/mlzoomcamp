import pickle 
from sklearn.feature_extraction import DictVectorizer
from sklearn.linear_model import LogisticRegression

dv_file = "dv.bin"

with open(dv_file, 'rb') as f_in: 
    dv = pickle.load(f_in)

model_file = "model1.bin"

with open(model_file, 'rb') as f_in: 
    model = pickle.load(f_in)

customer = {"job": "retired", "duration": 445, "poutcome": "success"}

X = dv.transform([customer])
y_pred = model.predict_proba(X)[0, 1]

print('input:', customer)
print('output:', y_pred)
