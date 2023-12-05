from flask import Flask, jsonify
from urllib.request import urlopen
import json

app_reverse = Flask(__name__)

def get_original_message():
    #return ("Mocked Service Response")
    #Make a request to the first service
    first_service_url = 'http://127.0.0.1:8000/'
    with urlopen(first_service_url) as response:
        # Load JSON data from the response
        json_data = json.load(response)
        # Reverse the message
        reversed_message = json_data['message'][::-1]
        return reversed_message

@app_reverse.route('/')
def get_reversed_json():
    reversed_message = get_original_message()
    reversed_json_data = {
        "id": "1",
        "reversed_message": reversed_message
    }
    return jsonify(reversed_json_data)

if __name__ == '__main__':
    app_reverse.run(host="0.0.0.0", debug=True, port=9000)