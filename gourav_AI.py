import pyttsx3
import datetime
import speech_recognition as sr
import smtplib
import pyaudio
import wikipedia
import webbrowser
import os
import random
from turtle import title
from  win10toast import ToastNotifier
from pkg_resources import Requirement
import time




engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

name_email = {
     "gourav": "gouravhds10@gmail.com",
     "ruben" : "rda66@sfu.ca",
     "krish" : "kba89@sfu.ca",
     "radhika" : "radhikagaikwad1653@gmail.com",
     "sarthak" : "sarthak.bishnoi@seaspan.com"
}

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wish_me(name):
    current_hour = int(datetime.datetime.now().hour)
    if current_hour < 12 and current_hour >= 0:
        speak(f'Good Morning,{name}!')

    elif 12 <= current_hour < 18:
        speak(f"Good Afternoon, {name}!")
    
    else:
        speak(f"Good Evening, {name}!")
    
    print("I am Gourav's Voice Assistant. How can I assist you today?")
    speak("I am Gourav's Voice Assistant. How can I assist you today?")

def take_command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.pause_threshold = 1
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        command = recognizer.recognize_google(audio, language='en-in')
        print(f"User said: {command}\n")
    
    except Exception as e:
        return "None"
    
    return command.lower()


def sendEmail(to, subject, message):
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login("asd048691@gmail.com", "olfctpcaihfdnerh") 
        email_message = f"Subject: {subject}\n\n{message}"
        server.sendmail("asd048691@gmail.com",to, email_message)
        server.close() 

if __name__ == "__main__":
    speak("What is your name?")
    name = input("Please enter your name: ").strip().lower()  
    if name != "None":
        wish_me(name)
        while True:
            query = take_command()

            if 'wikipedia' in query:
                speak("Searching Wikipedia...")
                query = query.replace("wikipedia", "")
                results = wikipedia.summary(query, sentences=2)
                speak("According to Wikipedia")
                print(results)
                speak(results)
            
            elif 'open youtube' in query:
                webbrowser.open("youtube.com")
                speak("Opening YouTube")
            
            elif 'open youtube' in query:
                webbrowser.open("google.com")
                speak("Opening Google")
            
            elif 'open stackoverflow' in query:
                webbrowser.open("stackoverflow.com")
                speak("Opening Stack Overflow")
            
            elif 'open github' in query:    
                webbrowser.open("github.com")
                speak("Opening GitHub")
            
            elif 'open linkedin' in query:
                webbrowser.open("linkedin.com")
                speak("Opening LinkedIn")
            
            elif 'open my experience' in query:
                webbrowser.open("https://myexperience.sfu.ca/myAccount/dashboard.htm")
                speak("Opening your My Experience SFU page")

            elif 'time' in query:
                current_time = datetime.datetime.now().strftime("%H:%M:%S")
                speak(f"Sir, The current time is {current_time}")
            
            elif 'open my email' in query or 'open outlook' in query:
                speak("Opening your email inbox")
                os.startfile("outlook.exe")

            elif 'play music' in query:
                url = {"https://music.youtube.com/watch?v=dQw4w9WgXcQ&feature=share",
                       "https://music.youtube.com/watch?v=FfOwqhckUH8&si=rbHB_n1hTx9lIDDS",
                       "https://music.youtube.com/watch?v=9Jjz_AzC6IA&si=UIxrw-At6fsj--wp",
                       "https://music.youtube.com/watch?v=Ld_fabIEmek&si=Je0rDu3GI2-92Bgy",
                       "https://music.youtube.com/watch?v=D2O6hDnkhsA&si=KpxoVH9x2JsoYGDW",
                       "https://music.youtube.com/watch?v=NxsKRO3ERTg&si=SGocMrV5RzNmE8Gp",
                       "https://music.youtube.com/watch?v=WSy0sjZiO8I&si=CCYz-KQR4G-9ceE-",
                       "https://music.youtube.com/watch?v=hAsQhAYje_I&si=6QqLnpAGrlKZlssV"
                       "https://music.youtube.com/watch?v=5fU-94bz4Jc&si=9aBJjVUDucPxKylC"
                       }

                webbrowser.open(random.choice(list(url)))

            elif 'open code' in query:
                code_path = "C:\\Users\\goura\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
                os.startfile(code_path)
                speak("Opening Visual Studio Code")
            
            elif 'open notepad' in query:
                notepad_path = "C:\\Windows\\System32\\notepad.exe"
                os.startfile(notepad_path)
                speak("Opening Notepad")
            
            elif 'open calculator' in query:
                calculator_path = "C:\\Windows\\System32\\calc.exe"
                os.startfile(calculator_path)
                speak("Opening Calculator")
            
            elif 'what is your name' in query:
                speak("I am Gourav's AI, your personal assistant.")
            
            elif 'who are you' in query:
                speak("I am Gourav's AI, created to assist you with various tasks.")
            
            elif 'joke' in query:
                jokes = [
                    "Why don't scientists trust atoms? Because they make up everything!",
                    "Why did the scarecrow win an award? Because he was outstanding in his field!",
                    "What do you call fake spaghetti? An impasta!"
                ]
                joke = random.choice(jokes)
                speak(joke)
            
            elif 'weather' in query:
                speak("Please tell me the city name.")
                city = take_command()
                if city != "None":
                    webbrowser.open(f"https://www.google.com/search?q=weather+in+{city}")
                    speak(f"Here is the weather information for {city}.")
                else:
                    speak("I didn't catch that. Please try again.")
            
            elif 'search' in query:
                speak("What would you like to search for?")
                search_query = take_command()
                if search_query != "None":
                    webbrowser.open(f"https://www.google.com/search?q={search_query}")
                    speak(f"Here are the search results for {search_query}.")
                else:
                    speak("I didn't catch that. Please try again.")
            

            elif 'send email' in query or 'send an email' in query:
                try:
                    speak("What is the recipient's name?")
                    recipient_name = take_command()
                    if recipient_name == "None" or recipient_name.lower() not in name_email:
                        speak("I didn't catch that. Please type the recipient's name.")
                        recipient_name = input("Recipient's name: ").lower()
                
                    if recipient_name in name_email:
                        recipient_email = name_email[recipient_name]
                        speak(f"What is the subject of the email to {recipient_name}?")
                        subject = take_command()
                        speak(f"What is the message for {recipient_name}?")
                        message = take_command()
                        sendEmail(recipient_email, subject, message)
                        speak(f"Email sent to {recipient_name} at {recipient_email} with subject '{subject}' and message '{message}'.")
                    
                    else:
                        speak("I don't have that person's email address.")

                except Exception as e:
                    speak("Sorry, I couldn't send the email. Please try again later.")
                    print(f"Error: {e}")
            
            elif 'set reminder' in query or 'set a reminder' in query:             
                speak("What would you like to be reminded about?")
                title = take_command()

                if title != "None" and title != "":
                    reminder_time = None
                    
                    speak("What is the message for the reminder?")
                    msg= take_command()

                    speak("How many minutes from now would you like to be reminded?Please type in the number.")    
                    time_in_minutes = float(input("Enter the number of minutes: "))

                    seconds = int(time_in_minutes) * 60
                    time.sleep(seconds)
                    toaster = ToastNotifier()
                    toaster.show_toast(title, msg, duration=10, threaded=True)
                    while toaster.notification_active():
                        time.sleep(0.1) 
                    
            elif 'dil ki baat' in query or 'tell me a secret' in query or 'secret' in query:
                speak("I love you Radhika! You are my sunshine and my everything. I cherish every moment with you, and I am grateful for your love and support. You make my life complete, and I can't imagine a day without you. You are the reason I smile, and I will always be here for you. I love you more than words can express.")

            elif 'exit' in query or 'quit' or 'band kar' in query:
                print("Goodbye! Have a great day!")
                speak("Goodbye! Have a great day!")
                break


    else:
        speak("Did not catch your name. Please try again.")
        
        

   