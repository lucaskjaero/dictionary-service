import json

from flask import Flask, request
from flask_restful import Resource, Api

from chinese.Chinese import get_definition, HSKHandler

app = Flask(__name__)
api = Api(app)


class WordHandler(Resource):
    def get(self, language, word):
        # Default responses
        entries = []
        message = ""
        status = "OK"

        if language == "chinese":
            entries = get_definition(word)
        else:
            status = "ERROR"
            message = "Language %s has not been implemented yet." % language

        return {"status": status, "message": message, "entries": entries}

api.add_resource(WordHandler, '/v1/<string:language>/definition/<string:word>')
api.add_resource(HSKHandler, '/v1/chinese/hsk/<int:level>')

if __name__ == '__main__':
    app.run(debug=True)
