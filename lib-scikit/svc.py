from sklearn.svm import LinearSVC, SVC, NuSVC
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




model = NuSVC(gamma="auto")
model.fit(X_train, Y_train)
Y_pred = model.predict(X_test)


accuracy = accuracy_score(Y_test, Y_pred)
print('Accuracy', accuracy)

cm = confusion_matrix(Y_test, Y_pred)


plt.matshow(cm)
plt.title('Confusion Matrix')
plt.colorbar()
plt.ylabel('True label')
plt.xlabel('Predicted label')
# plt.show()

print(classification_report(Y_test, Y_pred))

# print('w = ',model.coef_)
# print('b = ',model.intercept_)


dimensions2 = pd.read_csv("dimension-data.csv")
X = dimensions2.iloc[:, 0:4].values
for row in X:
    row[0:3] = sorted(row[0:3])
Y = dimensions2.iloc[:, 4].values

Y = np.where(Y == 'mid', 0, 1)

Y_pred = model.predict(X)

accuracy = accuracy_score(Y, Y_pred)
print('high confidence data accuracy', accuracy)


exit()

def logistic_regression_formula(x):
    coef = [0.00289793, 0.00378891, 0.0265589,  0.08627508 ]
    intercept = -4.60768847
    probability = sum(w * feature for w, feature in zip(coef, x)) + intercept
    return probability

X_test = X
Y_test = Y
i = 0   
for x, y in zip(X_test, Y_test):
    prob =  logistic_regression_formula(x)
    if prob > 0.5 :
        r = 1
    else:
        r = 0
    if r != y :
        i += 1
print(1 - i/len(X_test))
print('end', len(X_test))
