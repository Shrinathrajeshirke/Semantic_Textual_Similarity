from sentence_transformers import SentenceTransformer

def load_model():
    return SentenceTransformer('all-MiniLM-L6-v2')

def encode_texts(model, texts):
    return model.encode(texts, convert_to_numpy=True)

