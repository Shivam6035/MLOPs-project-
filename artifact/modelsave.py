import pickle

from botocore import model

with open("model.pkl", "wb") as f:
    pickle.dump(model, f)

print("Model saved")