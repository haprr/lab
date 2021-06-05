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

options=["no"]
an=["and"]

@app.route('/api/all', methods=['POST'])
def addOne():
    answers1=[]
    new = request.get_json()
    if new["question_key"]=="q1":
        for j in new["options"]:
            if j in content_list:
                answers1.append(j)
			else if j in content_list: 
                answers1.append("NONE")
			else if j in an:
				answers1.append("Others")
			else:
				answers1.append([])
	if new["question_key"]=="q2":
		for j in content_list:
			user_ans=re.findall('[0-9]+',j)

		for i in new["options"]:
			req_ans=re.findall('[0-9]+',i)
			for u in user_ans:
				if(len(req_ans)==1):
                                        for r in req_ans:
						if(u==r):
							answers1.append(i)
					a={"answers":answers1}
					Response.update(a)
					return jsonify(Response)

				elif(len(req_ans)==2):
					if((u>=req_ans[0]) and (u<=req_ans[1])):
						answers1.append(i)
						a={"answers":answers1}
						Response.update(a)
						return jsonify(Response)
	
    a={"answers":answers1}
    Response.update(a)
    return jsonify(Response)
    

if __name__=="__main__":
	app.run(use_reloader=False)
	
	

