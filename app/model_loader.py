import pickle
import os

MODEL_DIR = os.path.join(os.path.dirname(__file__), 'models')

def load_model(name):
    path = os.path.join(MODEL_DIR, f"{name}.pkl")
    with open(path, 'rb') as f:
        return pickle.load(f)
