import speech_recognition as sr
import sys
r = sr.Recognizer()
m = sr.Microphone()


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
				f.close()
				break
		else:  
			print("You said {}".format(value))
			with open("microphone-results.txt", "wb") as f:
				f.write(format(value).encode("utf-8"))
				f.close()
				break
					
	except sr.UnknownValueError:
		print("Sorry! Didn't catch that")
	except sr.RequestError as e:
		print("Uh oh! Couldn't request results from Google Speech Recognition service; {0}".format(e))	


