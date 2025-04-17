from flask import Flask, render_template, request
from model_loader import load_model
import numpy as np

app = Flask(__name__)

models = {
    'diabetes': load_model('diabetes'),
    'heart': load_model('heart'),
    'parkinsons': load_model('parkinsons')
}

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        model_name = request.form['model']
        features = [float(request.form[f'f{i}']) for i in range(1, int(request.form['feature_count'])+1)]
        prediction = models[model_name].predict([np.array(features)])
        result = f"Prediction for {model_name.title()} model: {'Positive' if prediction[0]==1 else 'Negative'}"

    return render_template('index.html', result=result)
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
