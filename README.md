# ODE-TO-CODE HACKATHON

A Virtual Hackathon 

## Selected problem statement number

      1

## Problem Domain

      Speech Analysis
      
## TEAM MEMBERS:

      HARSHAPRIYA C R, SUPRITHA R

## TEAM NAME:

      GALAXY AI

## Solution to be demonstrated

      1. Creating a speech analysis module (Web Based) where certain questions such as
        below could be asked by the system(text form), and the specific intent of the
        answer should be displayed.

## Output Scenarios:

    For UI - output can be presented in any way.
    For API - Response 

    The output request response is demonstrated using API.

## Question SET:

    1. Do you suffer from any health diseases?
    2. What’s your annual income?
    3. What is your dob?
 
 

## Requirements

      Flask
      Python Speech Recognition module
      We are using SpeechRecognition library of Python which provides Speech-to-Text Transcription service, Flask is used to take in the Audio transcript and create both a GET       and POST request on the different route.

## Installation

            Python Speech Recognition module:
                  pip install speechrecognition
      
## TESTING:

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


