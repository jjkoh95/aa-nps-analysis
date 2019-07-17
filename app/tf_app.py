from flask import Flask, request, Response, jsonify
import pickle
# import tensorflow as tf
from tensorflow import keras
import tensorflow_hub as hub
import numpy as np

app = Flask(__name__)
app.model = None

@app.route('/')
def index():
    return 'JJKoh is the best!'

@app.route('/deploy', methods=['POST'])
def deploy():
    model = request.files['model']
    model.save('./model.h5')
    app.model = keras.models.load_model('./model.h5',
                                        custom_objects={'KerasLayer': hub.KerasLayer})
    # app.model = keras.models.load_model(request.files['model'], custom_objects={'KerasLayer': hub.KerasLayer})
    if not app.model:
        return jsonify({'message': 'model failed to deploy'}), 400
    return jsonify({'message': 'model successfully deployed!'}), 200

@app.route('/predict', methods=['POST'])
def predict():
    if not app.model:
        return jsonify({'message': 'no active model'}), 400 
    preds = app.model
    preds = app.model.predict(np.array([request.get_json()['text']]))
    # print(preds[0][0])
    return jsonify({'prob': str(preds[0][0])}), 200

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080)
