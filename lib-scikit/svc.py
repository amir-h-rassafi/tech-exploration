from sklearn.svm import SVC
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

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.8, random_state=15, shuffle=True)




model = SVC()
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
plt.show()

print(classification_report(Y_test, Y_pred))



dimensions2 = pd.read_csv("dimension-data.csv")
X = dimensions.iloc[:, 0:4].values
for row in X:
    row[0:3] = sorted(row[0:3])
Y = dimensions.iloc[:, 4].values

Y = np.where(Y == 'mid', 0, 1)

Y_pred = model.predict(X)

accuracy = accuracy_score(Y, Y_pred)
print('high confidence data accuracy', accuracy)