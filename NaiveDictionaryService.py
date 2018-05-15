import json

from flask import Flask, request
from flask_restful import Resource, Api

from chinese.Chinese import get_definition, HSKHandler
from Logger import get_logger

app = Flask(__name__)
api = Api(app)

LOGGER = get_logger()


class WordHandler(Resource):
    def get(self, language, word):
        # Default responses
        entries = []
        message = ""
        status = "OK"
        response_code = 200

        try:
            if language == "chinese":
                entries, message = get_definition(word)
                LOGGER.info("Getting definition for %s"  % word)

                if len(entries) == 0:
                    response_code = 404

            else:
                status = "ERROR"
                message = "Language %s has not been implemented yet." % language
                LOGGER.error("Customer tried to get definitions in %s" % language)
                response_code = 400

        except exception as e:
            status = "ERROR"
            message = "An error has occurred"

            LOGGER.error("Error getting word %s: %s" % (word, e))
            response_code = 500

        return {"status": status, "message": message, "entries": entries}, response_code

api.add_resource(WordHandler, '/v1/<string:language>/definition/<string:word>')
api.add_resource(HSKHandler, '/v1/chinese/hsk/<int:level>')

if __name__ == '__main__':
    app.run(debug=False)
