# Module 
import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import time
import pyautogui
import openai
import keyboard
# -----------------------------------------------------------------------------------------------------------------------------------------------------
# Choisir la voix de l'assistant
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)
rate = engine.getProperty('rate')
engine.setProperty('rate', 185)
#--------------------------------------------------------------------------------------------------------------------------------------------------------

#--------------------------------------------------------------------------------------------------------------------------------------------------------
#Open ai
openai.api_key = ""
def gpt_answer(text):
    completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": text+" with a maximum of 1500 characters"}]
    )
    return(completion.choices[0].message.content)
def gpt_answer_coding(text):
    completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": "I want you to act as a Python programmer and create a program that "+text+" just write the code ,don't write any text"}]
    )
    generated_code = completion.choices[0].message.content
    for line in generated_code.splitlines():
        keyboard.write(line)
        keyboard.press("enter")
        keyboard.release("enter")
        time.sleep(0.1)
def gpt_answer_writting(text):
    completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content":"Create a newsletter article about"+text+" that resume the subject with 1500 characters at maximum"}]
    )
    return(completion.choices[0].message.content)



#--------------------------------------------------------------------------------------------------------------------------------------------------------




def write_to_active_window(text):
    time.sleep(2)  
    pyautogui.write(text)
    pyautogui.press('enter')
def speak(text):
    engine.say(text)
    engine.runAndWait()
    
def wishMe():
    hour=datetime.datetime.now().hour
    if hour>=0 and hour<12:
        speak("Hello,Good Morning")
        print("Hello,Good Morning")
    elif hour>=12 and hour<18:
        speak("Hello,Good Afternoon")
        print("Hello,Good Afternoon")
    else:
        speak("Hello,Good Evening")
        print("Hello,Good Evening")

def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio=r.listen(source)

        try:
            statement=r.recognize_google(audio,language='en-in')
            print(f"user said:{statement}\n")

        except Exception as e:
            speak("Pardon me, please say that again")
            return "None"
        return statement

speak("Loading your personal assistant Ava")

#--------------------------------------------------------------------------------------------------------------------------------------------------------




if __name__=='__main__':


    while True:
        speak("Tell me how can I help you now?")
        statement = takeCommand().lower()
        if statement==0:
            continue
        
        if "goodbye" in statement or "ok bye" in statement or "stop" in statement:
            speak('your personal assistant Ava is shutting down,Good bye')
            print('your personal assistant Ava is shutting down,Good bye')
            break
        
        if 'wikipedia' in statement:
            speak('Searching Wikipedia...')
            statement = statement.replace("wikipedia", "")
            results = wikipedia.summary(statement, sentences=3)
            speak("According to Wikipedia")
            print(results)
            write_to_active_window(results)
#--------------------------------------------------------------------------------------------------------------------------------------------------------

        if 'search' in statement:
             speak('Searching with Gpt...')
             statement = statement.replace("search", "")
             conf = input("Enter Y/N To conitnue")
             if conf =="Y":
                speak("According to GPT")
                results = gpt_answer(statement)
                print(results)
                write_to_active_window(results)
                
        if 'create' in statement:
             speak('Coding with Gpt...')
             statement = statement.replace("create", "")
             conf = input("Enter Y/N To conitnue")
             if conf =="Y":
                speak("According to GPT")
                results = gpt_answer_coding(statement)
             else:
                 pass
             
        if 'article' in statement:
             speak('Writting with Gpt...')
             statement = statement.replace("article", "")
             conf = input("Enter Y/N To conitnue")
             if conf =="Y":
                speak("According to GPT")
                results = gpt_answer_writting(statement)
                print(results)
                write_to_active_window(results)
                
# #--------------------------------------------------------------------------------------------------------------------------------------------------------


        elif 'open youtube' in statement:
            webbrowser.open("https://www.youtube.com")
            speak("youtube is open now")
            time.sleep(5)

        elif 'open google' in statement:
            webbrowser.open("https://www.google.com")
            speak("Google chrome is open now")
            time.sleep(5)

        elif 'open gmail' in statement:
            webbrowser.open("gmail.com")
            speak("Google Mail open now")
            time.sleep(5)
        elif 'time' in statement:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"the time is {strTime}")
