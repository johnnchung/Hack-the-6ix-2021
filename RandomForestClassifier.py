import numpy as np 
import pandas as pd 
import seaborn as sns
import joblib 
import sklearn
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import whois

df_csv = pd.read_csv('combined_dataset.csv')
df_test = df_csv
df_test = df_test.drop(columns = ['isIp', 'ranking'])
df = df_test.drop(columns = ['domain'])
pd.set_option("display.max_columns", None)

# splitting the dataset in x ,and y.
x = df.drop('label',axis=1)
y = df['label']

# using the linear regression model. 
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)

model = RandomForestClassifier(n_jobs = 1)
model.fit(x_train, y_train)

joblib.dump(model, 'model.joblib')