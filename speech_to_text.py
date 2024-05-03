import speech_recognition as sr
import pyttsx3 

#Initialize the recognizer
r = sr.Recognizer()

def  record_text():
    #Loop in case of errors
    while(1):
        try:
            #Use microphone as source for input
            with sr.Microphone() as source:
                #Prepare recognizer to receive input
                r.adjust_for_ambient_noise(source, duration=0.2)

                #Listens to user input
                audio = r.listen(source)

                # Using google to recognize audio
                MyText = r.recognize_google(audio)

                return MyText
            
        except sr.RequestError as e:
            print("Could not request results; {0}".format(e))
         
        except sr.UnknownValueError:
            print("unknown error occurred")
    return

def output_text(text):
    f = open("mytext.txt", "a")
    f.write(text)
    f.write("\n")
    f.close()
    pass

while(1):
    text = record_text()
    output_text(text)

    print("Wrote Text")
