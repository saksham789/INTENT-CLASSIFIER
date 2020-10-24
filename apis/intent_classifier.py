from flask_restx import Namespace,Resource,fields
from helper import load_model, give_top_matching_intent, load_embedding_library
from flask import jsonify
from sentence_transformers import SentenceTransformer, util
import numpy as np
api = Namespace("Intent_Classifier",description = "Classify Intents for Vendors")

model = None
embedding_db = None

payload = api.model("Intent Classifier",{
	"Input_Query":fields.String(required = True, description = "Input query from vendors"),
	"Top_intents":fields.Integer(required=False,description= "Top Predictions count",default = 3)
})

intent_confidence = api.model("Intents_confidence",{
	"intent":fields.String(),
	"confidence":fields.Float()
})

total_response = api.model("Finalresponse",{
	"TopKIntents":fields.List(fields.Nested(intent_confidence))
})

model = load_model()
embedding_db = load_embedding_library()

@api.route("/intent_prediction")
class Prediction(Resource):

	@api.expect(payload)
	def post(self):
		query = self.api.payload["Input_Query"]
		kintents = self.api.payload["Top_intents"]

		try:
			response = give_top_matching_intent(query,embedding_db,kintents,model)
			return response,200
		except Exception as e:
			self.api.abort(500,f"Error in intent classifier - {e}")

