from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

def compute_similarity(embeddings1, embeddings2):
    return cosine_similarity(embeddings1, embeddings2).diagonal()