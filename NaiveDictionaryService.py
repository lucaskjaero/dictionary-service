import json

from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

# Yes we're just storing this in memory for now
# If this has too much load after caching we can re-architect it
cedict = open("chinese/cedict.json")
chinese_dictionary = json.load(cedict)


class WordHandler(Resource):
    def get(self, language, word):
        # Default responses
        definitions = []
        message = ""
        status = "OK"

        if language == "chinese":
            definitions = [entry for entry in chinese_dictionary if entry['simplified'] == word or entry['traditional'] == word]
        else:
            status = "ERROR"
            message = "Language %s has not been implemented yet." % language

        return {"status": status, "message": message, "definitions": definitions}

api.add_resource(WordHandler, '/v1/<string:language>/definition/<string:word>')

if __name__ == '__main__':
    app.run(debug=True)
