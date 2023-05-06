from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

dimensions = pd.read_csv("dimension-data.csv")

X = dimensions.iloc[:, 0:4].values
for row in X:
    row[0:3] = sorted(row[0:3])
Y = dimensions.iloc[:, 4].values

Y = np.where(Y == 'mid', 0, 1)

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.5, random_state=15, shuffle=True)




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
plt.show()

print(classification_report(Y_test, Y_pred_round))