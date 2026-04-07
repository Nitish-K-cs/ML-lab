#Implement Naive-Baye's on a) Iris dataset

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score

# Load your dataset
df = pd.read_csv("C:/Users/pc/Documents/Nitish093/Titanic.csv")

df = df[['Pclass' , 'Sex' , 'Age' , 'Survived']]

df['Age'].fillna(df['Age'].mean() , inplace= True)

df['Sex'] = df['Sex'].map({'male': 0, 'female': 1})

X = df[['Pclass' , 'Sex' , 'Age']]
y = df['Survived']

X_train, X_test , y_train , y_test = train_test_split(X,y,test_size=0.3)

model = GaussianNB()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print("Accuracy(70-30 split):" , accuracy_score(y_test , y_pred))

#split 90-10
X_train , X_test , y_train , y_test = train_test_split(X,y,test_size= 0.1)
model.fit(X_train , y_train)

y_pred = model.predict(X_test)

print("Accuracy(90-10 split:)" , accuracy_score(y_test, y_pred))

#Example prediction
sample = [[2, 0, 41]]
if model.predict(sample):
    check = "Survived"
else:
    check= "Not Survived"
print("Prediction" , check)
