#Import the libraries
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import pickle

#import the dataset
df = pd.read_csv('BankNote_Authentication.csv')

df.head()

#%%

X= df.iloc[:,:-1]
Y = df.iloc[:,-1]
X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.2,random_state=0)

#%%
classifier = RandomForestClassifier()
classifier.fit(X_train,Y_train)
#%%Prediction
y_pred = classifier.predict(X_test)
score = accuracy_score(Y_test, y_pred)

#%% Create a pickle file for serialization


pickle_out = open("bank_classifier.pkl","wb")
pickle.dump(classifier,pickle_out)
pickle_out.close()
#%%

