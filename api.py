import flask
from flask import request, jsonify
import speech_recognition as sr
import json
import sys
import re


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

MonthDict={ 1 : "january",
       2 : "february",
       3 : "march",
       4 : "april",
       5 : "may",
       6 : "june",
       7 : "july",
       8 : "august",
       9 : "september",
       10 : "october",
       11 : "november",
       12 : "december"
}

Response={"answers":[]}
#print(content_list)
answers=[]

@app.route('/', methods=['GET'])
op=["no"]
an=["and"]
@app.route('/api/all', methods=['POST'])
def addOne():
    answers1=[]
    new = request.get_json()
    
    if new["question_key"]=="q1":
        for j in new["options"]:
            if j in content_list:
                answers1.append(j)
	    elif j in op: 
                answers1.append("NONE")
	    elif j in an:
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

    if new["question_key"]=="q3":
       for j in content_list:
          user_ans=[j]
       if(user_ans[1].isnumeric()):
          content_list.replace(" ","/")
          answers3=[]
          answers3.append(content_list)

       elif(user_ans[1].isalpha()):
          for i in MonthDict:
             if(MonthDict[i]==user_ans[1]):
                #user_ans[1]=i
                content_list.replace(user_ans[1],i)
                content_list.replace(" ","/")
                answers3=[]
                answers3.append(content_list)






          




             




             


    a={"answers":answers1}
    Response.update(a)
    return jsonify(Response)
    
    
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
