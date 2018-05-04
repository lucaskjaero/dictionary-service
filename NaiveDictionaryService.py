import json

from flask import Flask, request
from flask_restful import Resource, Api
from flask_cors import CORS

from chinese.Chinese import get_definition, HSKHandler

app = Flask(__name__)
api = Api(app)
cors = CORS(app)

class WordHandler(Resource):
    def get(self, language, word):
        # Default responses
        entries = []
        message = ""
        status = "OK"

        if language == "chinese":
            try:
                entries = get_definition(word)

                if len(entries) == 0:
                    print("Dictionary miss: %s" % word)
                    
                    message = "No entries found for %s" % word

            except exception as e:
                status = "ERROR"
                message = "An error has occurred"

                print(e)
        else:
            status = "ERROR"
            message = "Language %s has not been implemented yet." % language

        return {"status": status, "message": message, "entries": entries}

api.add_resource(WordHandler, '/v1/<string:language>/definition/<string:word>')
api.add_resource(HSKHandler, '/v1/chinese/hsk/<int:level>')

if __name__ == '__main__':
    app.run(debug=True)
