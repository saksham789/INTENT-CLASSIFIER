from flask import Flask
from apis import blueprint as api
# from waitress import serve
# from flask_cors import CORS

app = Flask(__name__)
# CORS(app)
app.register_blueprint(api,url_prefix = "/api/v1")
app.config["SWAGGER_UI_JSONEDITOR"] = True
if __name__ == "__main__":
    app.run(host='0.0.0.0')