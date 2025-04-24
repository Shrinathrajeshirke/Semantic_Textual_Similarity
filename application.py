from flask import Flask, request, jsonify
from utils.model import load_model, encode_texts
from sklearn.metrics.pairwise import cosine_similarity

app = Flask(__name__)
model = load_model()

@app.route('/similarity',methods=['POST'])
def get_similarity():
    data = request.get_json()
    text1 = data['text1']
    text2 = data['text2']
    emb1 = encode_texts(model, [text1])
    emb2 = encode_texts(model, [text2])
    score = cosine_similarity([emb1[0]], [emb2[0]])[0][0]
    return jsonify({'similarity score': round(float(score),3)})

if __name__=='__main__':
    app.run(debug=True)