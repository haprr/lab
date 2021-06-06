# ode-to-code
A Virtual Hackathon ODE-TO-CODE HACKATHON

Selected problem statement - 1

Problem Domain: Speech Analysis

Solution to be demonstrated:

      1. Creating a speech analysis module (Web Based) where certain questions such as
        below could be asked by the system(text form), and the specific intent of the
        answer should be displayed.

Output Scenarios:

    For UI - output can be presented in any way.
    For API - Response 

    The output request response is demonstrated using API.

Question SET:

    1. Do you suffer from any health diseases?
    2. What’s your annual income?
    3. What is your dob?
 
 
**We are using SpeechRecognition library of Python which provides Speech-to-Text Transcription service, Flask is used to take in the Audio transcript and create both a GET and POST request on the different route.**

TEAM MEMBERS:

      HARSHAPRIYA C R, SUPRITHA R

TEAM NAME:

      GALAXY AI
      
TESTING:

      We are using Postman tool to test our API.
      Method : POST
      URL : http://localhost:5000/api/all 

Request Body:

      {
          "question_key":"q1",
          "options":["Diabetes","Thyroid","Cancer"],
          "audio":"" //encoded utf-8 audio text("I have Diabetes")
      }

      Audio text will be converted to JSON and stored in microphone-results.txt file.

Response:

If user answers : I have Diabetes

      {
            "answer":["Diabetes"]
      }


