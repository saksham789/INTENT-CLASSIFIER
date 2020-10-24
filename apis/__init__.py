from flask_restx import Api
from flask import Blueprint

blueprint = Blueprint("api",__name__)
from apis.intent_classifier import api as ns1

api = Api(blueprint)
api.add_namespace(ns1)