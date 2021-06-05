import flask
from flask import request, jsonify
import speech_recognition as sr

r = sr.Recognizer()
m = sr.Microphone()

try:
    print("A moment of silence, please...")
    with m as source: r.adjust_for_ambient_noise(source)
    print("Set minimum energy threshold to {}".format(r.energy_threshold))
    while True:
        print("Say something!")
        with m as source: audio = r.listen(source)
        print("Got it!")
        try:
            value = r.recognize_google(audio)
            if str is bytes:  
                print(u"You said {}".format(value).encode("utf-8"))
                with open("microphone-results.txt", "wb") as f:
                    f.write(format(value).encode("utf-8"))
                    break

            else:  
                print("You said {}".format(value))
                with open("microphone-results.txt", "wb") as f:
                    f.write(format(value).encode("utf-8"))
                    break
        except sr.UnknownValueError:
            print("Sorry! Didn't catch that")
        except sr.RequestError as e:
            print("Uh oh! Couldn't request results from Google Speech Recognition service; {0}".format(e))
except KeyboardInterrupt:
    pass



Dict={"q1":"Do you suffer from any health diseases?","q2":"What’s your annual income?","q3":"What is your dob?"}
# Create some test data for our catalog in the form of a list of dictionaries.

my_file = open("microphone-results.txt", "r")
content = my_file.read()
content_list = content.split(" ")
my_file.close()
