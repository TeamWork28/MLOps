from sklearn.linear_model import LogisticRegression
from sklearn.datasets import load_iris
import joblib

X, y = load_iris(return_X_y=True)
model = LogisticRegression(max_iter=200)
model.fit(X, y)
joblib.dump(model, "model.joblib")
print("Model trained and saved.")
