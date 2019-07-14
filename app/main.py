from flask import Flask, request, Response, jsonify
from fastai import *
from fastai.text import *
import pickle

app = Flask(__name__)
app.model = None

@app.route('/')
def index():
    return 'JJKoh is the best!'

@app.route('/deploy', methods=['POST'])
def deploy():
    # app.model = pickle.dumps(request.files['model'])
    # model = request.files['model']
    # if model:
    #     model.save('./model.pkl')
    # app.model = load_learner(Path('.'), 'model.pkl')
    app.model = load_learner(Path('.'), request.files['model'])
    if not app.model:
        return jsonify({'message': 'model failed to deploy'}), 400
    return jsonify({'message': 'model successfully deployed!'}), 200

@app.route('/predict', methods=['POST'])
def predict():
    if not app.model:
        return jsonify({'message': 'no active model'}), 400 
    preds = app.model.predict(request.get_json()['text'])
    return jsonify({'prob_neg': preds[2][0].item(), 'prob_pos': preds[2][1].item()})

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080)
