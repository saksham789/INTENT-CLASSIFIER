from scipy import spatial
from sklearn.metrics.pairwise import cosine_similarity
from sentence_transformers import SentenceTransformer, util
import numpy as np

def load_model():
  model = SentenceTransformer('distilbert-base-nli-stsb-quora-ranking');
  return model
     

def give_top_matching_intent(query_sentence, emb_db, top_intents_count,model):
  distance = []
  query_sentence_embedding = model.encode(query_sentence);
  for i in range(len(emb_db)):
    distance.append({"intent":emb_db[i][0],"similarity_score":float(get_similarity(emb_db[i][1], query_sentence_embedding))})
  distance = sorted(distance, key = lambda x:x["similarity_score"], reverse = True);
  return distance[:top_intents_count];


def get_similarity(primary_embedding, secondary_embedding):
  return 1 - spatial.distance.cosine(primary_embedding,secondary_embedding)

def load_embedding_library():
  embedding_db = np.load("intent_embedding_db.npy",allow_pickle=True);
  return embedding_db;


def get_intent(query, top_intent_count):
  query_embbeding = model.encode(query);
  top_matching_intents = give_top_matching_intent(query_embbeding, embedding_db, 3)
  return top_matching_intents;
