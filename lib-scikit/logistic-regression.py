from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

dimensions = pd.read_csv("dimension-data2.csv")

X = dimensions.iloc[:, 0:4].values
for row in X:
    row[0:3] = sorted(row[0:3])
Y = dimensions.iloc[:, 4].values

Y = np.where(Y == 'mid', 0, 1)

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=15, shuffle=True)




model = LogisticRegression()
model.fit(X_train, Y_train)
Y_pred = model.predict(X_test)
Y_pred_round = [0 if i < 0.5 else 1 for i in Y_pred]
coef = model.coef_
intercept = model.intercept_
print(coef, intercept)


accuracy = accuracy_score(Y_test, Y_pred_round)
print('Accuracy', accuracy)

cm = confusion_matrix(Y_test, Y_pred_round)


plt.matshow(cm)
plt.title('Confusion Matrix')
plt.colorbar()
plt.ylabel('True label')
plt.xlabel('Predicted label')
# plt.show()

print(classification_report(Y_test, Y_pred_round))

def logistic_regression_formula(x, coef = None, intercept = None):
    if coef is None:
        coef = [0.02932585, 0.01655529, 0.11812993, 0.27142221]
    if intercept is None:
        intercept = -20.26230048
    linear_sum = sum(w * feature for w, feature in zip(coef, x)) + intercept
    probability = 1 / (1 + np.exp(-linear_sum))
    return probability

i = 0   
for x, y in zip(X_test, Y_test):
    prob =  logistic_regression_formula(x, coef[0], intercept)
    if prob > 0.5 :
        r = 1
    else:
        r = 0
    if r != y :
        # print(y,x, prob) 
        i += 1
print(1 - i/len(X_test), len(X_test))

dimensions2 = pd.read_csv("dimension-data.csv")
X = dimensions2.iloc[:, 0:4].values
for row in X:
    row[0:3] = sorted(row[0:3])
Y = dimensions2.iloc[:, 4].values

Y = np.where(Y == 'mid', 0, 1)

Y_pred = model.predict(X)

accuracy = accuracy_score(Y, Y_pred)
print(accuracy)
