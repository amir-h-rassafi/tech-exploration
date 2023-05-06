from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, accuracy_score, confusion_matrix, classification_report
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

dimensions = pd.read_csv("dimension-data.csv")

X = dimensions.iloc[:, 0:4].values
Y = dimensions.iloc[:, 4].values

Y = np.where(Y == 'mid', 0, 1)

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42, shuffle=True)


model = LinearRegression()
model.fit(X_train, Y_train)
Y_pred = model.predict(X_test)


mse = mean_squared_error(Y_test, Y_pred)
accuracy = accuracy_score(Y_test, Y_pred)
print(accuracy, mse)


cm = confusion_matrix(Y_test, Y_pred)

plt.matshow(cm)
plt.title('Confusion Matrix')
plt.colorbar()
plt.ylabel('True label')
plt.xlabel('Predicted label')
plt.show()

print(classification_report(Y_test, Y_pred))