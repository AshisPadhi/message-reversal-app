from flask import Flask,jsonify
import json
import os

app = Flask(__name__)

rel_json_path = 'data.json'
#abs_json_path = os.path.join(os.getcwd(), rel_json_path)
#print(abs_json_path)

def read_json_data(abs_json_path):
    try:
        with open(abs_json_path, 'r') as file:
            json_data=file.read()
            return json_data
    except FileNotFoundError:
        return jsonify({"error": f"File not found: {abs_json_path}"}), 404
    except Exception as e:
        return jsonify({"error": f"Error reading JSON file: {e}"}), 500

@app.route('/')
def render_json():
    abs_json_path = os.path.join(os.getcwd(), rel_json_path)
    json_data=read_json_data(abs_json_path)
    try:
        parsed_json = json.loads(json_data)
        return jsonify(parsed_json)
    except json.JSONDecodeError as e:
        return jsonify({"error": f"Error decoding JSON: {e}"}), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
