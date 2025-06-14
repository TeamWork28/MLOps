import joblib
import os

def test_model_exists():
    assert os.path.exists("model.joblib"), "Model file not found!"

test_model_exists()
print("Test passed: model exists.")
