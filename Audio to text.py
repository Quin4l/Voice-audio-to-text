import whisper
import time
import speech_recognition as sr

startT = time.time()

def voice_to_text():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("You can now speak")
        audio = r.listen(source)
        try:
            return r.recognize_whisper(audio).strip()
        except sr.UnknownValueError:
            print("Whisper could not understand audio")
        except sr.RequestError:
            print("Could not request results from Whisper")


def single_audio_to_text():
    #put your file here
    file = ''
    #specify your model. By default you should use the base model
    model = whisper.load_model('base')
    transcribe = model.transcribe(file)
    cleaning_string = transcribe["text"].strip().partition(".")
    output = "".join(cleaning_string)
    return output

def multiple_audios_to_text():
    #where the text is saved
    text = []

    #this loops through 50 example recordings, then appends it to the text variable
    for x in range(50):
        x += 1
        #Files I had recorded had a numbered filename. So plan accordingly.
        #an example syntax I had was "recording_"+str(x)+".wav
        #this would allow the function to continue accessing the files as it counts up automatically
        file = ""
        #specify your model. By default you should use the base model
        model = whisper.load_model('base')
        transcribe = model.transcribe(file)
        cleaning_string = transcribe["text"].strip().partition(".")
        cleaned_string = "".join(cleaning_string)
        text.append(cleaned_string)

    #this joins the text variable which up until now is a list of strings. This makes it into one cohesive string.
    output = " ".join(text)
    return output


#this part is to save whatever you have written as a text file.
#specify which function you are using. Whether it be the voice to text, single or multiple audios to text.
text =
print(text)
#write the file path here
path = ""
# saves the file to your filepath
with open(path,'w') as f:
    f.write(text)
    print("done")



print("This took",round(time.time()-startT,3),"seconds")