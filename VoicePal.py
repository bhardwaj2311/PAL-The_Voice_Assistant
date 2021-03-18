from gtts import gTTS
import playsound
import os
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import smtplib

dict = {"abhinav":"xwz@gmail.com","harsh":"abc@gmail.com"}

def text2int(textnum, numwords={}):
    
    '''
    This function can convert text to int.
    '''
    if not numwords:
      units = [
        "zero", "one", "two", "three", "four", "five", "six", "seven", "eight",
        "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
        "sixteen", "seventeen", "eighteen", "nineteen",
      ]

      tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

      scales = ["hundred", "thousand", "million", "billion", "trillion"]

      numwords["and"] = (1, 0)
      for idx, word in enumerate(units):    numwords[word] = (1, idx)
      for idx, word in enumerate(tens):     numwords[word] = (1, idx * 10)
      for idx, word in enumerate(scales):   numwords[word] = (10 ** (idx * 3 or 2), 0)

    current = result = 0
    for word in textnum.split():
        if word not in numwords:
          raise Exception("Illegal word: " + word)

        scale, increment = numwords[word]
        current = current * scale + increment
        if scale > 100:
            result += current
            current = 0
        
    final = result + current
    final = str(final)
    return final

def speak(text):
    '''
    This function lets PAL speak.
    
    '''
    tts = gTTS(text=text,lang="en-in", slow=False)
    filename = "voice1.mp3"
    tts.save(filename)
    playsound.playsound(filename)
    os.remove(filename)
    
def greeting():
    """
    This function lets PAL wish the user according to the current time.


    """
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<17:
        speak("Good Afternoon!")
    else:
        speak("Good evening!")
        
    speak("I'm PAL , How may I help you?")   
    
    
def accept():
    '''
    This function lets PAL take the voice commands from the user.

    '''
    r = sr.Recognizer()
    mic = sr.Microphone()
    with mic as source:
        print("listening...")
        audio = r.listen(source)
        r.energy_threshold = 10
    
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-in")
        print(query)
        
    except Exception as e:
        speak("Say that again please! ")
        return "NONE"
    
    return query   

def SendEmail(reciever,msg):
    '''
    This function lets PAL send mail to the chosen recipient 
    from the voice command of the user.

    '''
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('Sender mail', 'sender password')
    server.sendmail('Sender mail', reciever, msg)
    server.close()
    
    
 
    
if __name__ == "__main__":
    greeting()
    
    while True:
        
        query = accept().lower()
        
        if "wikipedia" in query:
            speak("Searching Wikipedia...")
            query = query.replace("Wikipedia","")
            result = wikipedia.summary(query, sentences=1)
            speak("According to wikipedia ")
            speak(result)
            print(result)
            
        
        elif "open youtube" in query:
            webbrowser.open_new('www.youtube.com')
            
            
        elif "open google" in query:
            webbrowser.open('www.google.com')
            
        elif "open geeks for geeks" in query:
            webbrowser.open('www.geeksforgeeks.org')
            
        elif "open whatsapp" in query:
            webbrowser.open('web.whatsapp.com')
            
        elif "open amazon prime" in query:
            webbrowser.open('www.primevideo.com')
            
        elif "open netflix" in query:
            webbrowser.open('www.netflix.com/in/')
            
        elif "play songs" in query:
            dir = "F:\songs"
            list = os.listdir(dir)
            for i in range(len(list)):
                print(f"{i} - {list[i]}")
            
            speak("which song you wanna play?")
            num = accept().lower()
            num = str(num)
            num = int(num)
            os.startfile(os.path.join(dir,list[num]))
            
        elif "open download" in query:
            dir = "C:\\Users\\abhi\\Downloads"
            os.startfile(dir)
            
        elif "the time" in query:
            time = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {time}")
            
        elif "the date" in query:
            date = datetime.datetime.today().strftime("%y-%m-%d")
            speak(f"The date is {date}")
            
        elif "send email" in query:
            for i in dict.keys():
                print(i)
            speak("Whom do yo want to send mail to?")
            reciever = accept().lower()
            reciever_mail = dict[reciever]
            try:
                speak("What should I say...")
                msg = accept()
                SendEmail(reciever_mail,msg)
                speak("The e-mail has been sent successfully!")
            except Exception as e:
                print(e)
                speak("Sorry, unable to send the e-mail.")
                

        elif "Bye" or "Goodnight" in query:
            speak("Take care")
            break
        
                
                
                
                
                
            
            
            
        
            
            
        
    





