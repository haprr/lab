import flask
from flask import request, jsonify
import speech_recognition as sr
import json
import sys


app = flask.Flask(__name__)
app.config["DEBUG"] = True

with app.app_context():
    exec(open('speech.py').read())
Dict={"q1":"Do you suffer from any health diseases?","q2":"What’s your annual income?","q3":"What is your dob?"}
# Create some test data for our catalog in the form of a list of dictionaries.

my_file = open("microphone-results.txt", "r")
content = my_file.read()
content_list = content.split(" ")
#func()
with open("microphone-results.txt", "w") as f1:
    f1.write(json.dumps(content_list))

my_file.close()

Request= [
    {
    "question_key": "",
    "options":[],
    "audio": ""
    }
    
]
Response={"answers":[]}
#print(content_list)
answers=[]

@app.route('/', methods=['GET'])

@app.route('/api/all', methods=['POST'])
#@app.route('/quarks', methods=['POST'])
def addOne():
    answers1=[]
    new = request.get_json()
    
    if new["question_key"]=="q1":
        for j in new["options"]:
            if j in content_list:
                answers1.append(j)
            else:
                answers1.append("NONE")
    a={"answers":answers1}
    Response.update(a)
    return jsonify(Response)
    """
    Request.append(new)
    return jsonify(Request)
    """
"""
@app.route('/api/v1/resources/books', methods=['GET'])
def api_id():
    if 'question_key' in request.args:
        key = request.args['question_key'])
    else:
        return "Error: No id field provided. Please specify an id."

    # Create an empty list for our results
    answers = []
    for "options" in request.args:
        for i in "options":
            if i in content_list:
                answers.append("yes")
    
    return jsonify(answers)
"""

if __name__=="__main__":
	app.run(use_reloader=False)
	
	

