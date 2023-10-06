import sys
import requests as rq
import json


definition_endpoint = "https://api.dictionaryapi.dev/api/v2/entries/en/"


def search_definition(word):

    endpoint_data = definition_endpoint + word
    definition_api_response = rq.get(endpoint_data)
    if(definition_api_response.status_code == 200):
        json_response = json.loads(definition_api_response.text)
        print(json_response)
    else:
        print("There is no result for the requested word")




if len(sys.argv) < 2:
    print("None word to define recieved")
else:
    print(f"This is the definition of word: {sys.argv[1]},  according to: {definition_endpoint}")
    search_definition(sys.argv[1])
