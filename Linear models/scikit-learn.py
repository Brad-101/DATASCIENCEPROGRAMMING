#excecution steps

#Step 1 choose a class model
from sklearn.linear_model import LinearRegression

#Step 2 arrange data into feature matrix
import pandas as pd
import numpy as np

df = pd.read_csv('HousingData.csv')
x = df[['RM']]
y = df['MEDV']

#Step 3 choose model hyperparameters
model = LinearRegression()

#Step 4 fit the model to the data.
model.fit(x,y)

#Step 5 apply the model to new data(predicting house of a price of 6 rooms)
new_house = np.array([[6]])
prediction = model.predict(new_house)
print("Prediction price:",prediction)

#Step 6 evaluate the model performance
print("R² Score:", model.score(x, y))
