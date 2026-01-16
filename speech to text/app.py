import speech_recognition as sr

for index, name in enumerate(sr.Microphone.list_microphone_names()):
    print(f"Microphone with index {index} available: {name}")

def main():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening......")
        r.pause_threshold = 1
        audio = r.listen(source)
        text=r.recognize_google(audio, language='en-in')
        print(text)





if __name__=="__main__":
    main()


