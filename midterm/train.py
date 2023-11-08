import pandas as pd
import numpy as np

from sklearn.feature_extraction import DictVectorizer
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
import pickle

# Load data
usecols = ['WinePrice','WineRating','Year','RegionalVariety','Winery']
df = pd.read_csv('./input/white-wine-price-rating.csv', usecols=usecols)
df = df.fillna(0)

# Split data into train, val nad test datsets 80-20-20 ratio
df_train_full, df_test = train_test_split(df, test_size=0.1, random_state=1)
df_train, df_val = train_test_split(df_train_full, test_size=0.11, random_state=1)

df_train = df_train.reset_index(drop=True)
df_val = df_val.reset_index(drop=True)
df_test = df_test.reset_index(drop=True)

y_train = df_train["WinePrice"].values
y_val = df_val["WinePrice"].values
y_test = df_test["WinePrice"].values

del df_train["WinePrice"]
del df_val["WinePrice"]
del df_test["WinePrice"]

# Features to model
features = ['WineRating','Year','RegionalVariety', 'Winery']

# Transform categorical variables
train_dict = df_train[features].to_dict(orient='records')
dict_vect = DictVectorizer(sparse=False)

X_train = dict_vect.fit_transform(train_dict)

# Train the data
model_rf = RandomForestRegressor()
model_rf.fit(X_train, y_train)

# save the model as pickle file
with open('model_rf.pkl', 'wb') as file:
    pickle.dump(model_rf, file)
    
# Save the dict_vect transformer as pickle file
with open('dict_vect.pkl', 'wb') as file:
    pickle.dump(dict_vect, file)