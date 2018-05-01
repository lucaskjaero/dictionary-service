import json

from flask import Flask, request
from flask_restful import Resource, Api

# Yes we're just storing this in memory for now
# If this has too much load after caching we can re-architect it
chinese_dictionary = []
with open("chinese/cedict.json") as cedict:
    chinese_dictionary.extend(json.load(cedict))


def sort_by_hsk(a):
    try:
        sort_value = a['HSK']
    except KeyError:
        sort_value = 7
    return sort_value


def get_definition(word):
    return sorted([entry for entry in chinese_dictionary
                   if entry['simplified'] == word
                   or entry['traditional'] == word],
    key=sort_by_hsk)


class HSKHandler(Resource):
    def get(self, level):
        # Default responses
        entries = []
        message = ""
        status = "OK"

        if level > 6 or level < 1:
            message = "Level %s of the HSK doesn't exist, please try 1-6" % level
            status = "ERROR"
        else:
            entries = [entry for entry in chinese_dictionary
                       if "HSK" in entry
                       and entry["HSK"] == level]

        return {"status": status, "message": message, "entries": entries}
