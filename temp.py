
from helper import load_model, give_top_matching_intent, load_embedding_library
from sentence_transformers import SentenceTransformer, util


model = load_model()
embedding_db = load_embedding_library()
print(embedding_db[0][1].shape)
response = give_top_matching_intent("i am not ahppy with retuns",embedding_db,3,model)
print(response)