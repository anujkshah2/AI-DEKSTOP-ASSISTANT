from ast import Try
from base64 import decode
from cgitb import html, text
import chunk
from email import encoders, message
from email.mime import audio
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from importlib.resources import path
import json
from lib2to3.pgen2.literals import evalString
from logging import exception
from multiprocessing import Condition
import re
from tokenize import Special
import traceback
from tracemalloc import take_snapshot
from turtle import st, up
from unittest import result
import webbrowser
import PyPDF2
import pyttsx3
import speech_recognition as sr
from datetime import datetime
import wikipedia
import webbrowser
import os
import random
import smtplib
import pywhatkit
import urllib.request
import re
#import cv2
from requests import get, request
import sys
import pyjokes
import pyautogui
import requests
import operator
from bs4 import BeautifulSoup
from pywikihow import search_wikihow

#if you had error with pyaudio check this link and download pyaudio https://www.lfd.uci.edu/~gohlke/pythonlibs/
engine=pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print (voices[0].id)
engine.setProperty('voice',voices[0].id)
engine.setProperty('rate' , 170)

def speak (audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour= int (datetime.now().hour)
    if hour>=0 and hour <=12:
        speak ("good morning!")
    elif hour>=12 and hour<18:
        speak ("good afternoon !") 
    else:
        speak ("good Evening sir!")  
    speak ("Hi sir this is Jaeger. ")
    speak("you can also call me by the name of mike ")
    
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('dummyonehunk@gmail.com', 'anujkshah')
    server.sendmail('', to, content)
    server.close()

def  news():
    #newsapi.org// for apikey
    speak("News for today.. ")
    url = "https://newsapi.org/v2/top-headlines?sources=the-times-of-india&apiKey=bdf117847390497e9b7830cd347cd437"
    news = requests.get(url).text
    news_dict = json.loads(news)
    arts = news_dict['articles']
    for article in arts:
        speak(article['title'])
        print(article['title'])
        
def stockmrkt():
    speak("today's stock market...") 
    url = "https://newsapi.org/v2/top-headlines?country=in&category=business&apiKey=bdf117847390497e9b7830cd347cd437"
    news = requests.get(url).text
    news_dict = json.loads(news)
    arts = news_dict['articles']
    for article in arts:
        speak(article['title'])
        print(article['title'])

def pdf_reader():
    book=open('py3.pdf.pdf','rb')
    pdfReader=PyPDF2.PdfFileReader(book)#pip install pyPDF
    pages=pdfReader.numPages
    speak(f"toal number of pages in this book {pages}")
    pg=int(input("enter page number:"))
    page=pdfReader.getPage(pg)
    text=page.extractText()
    speak (text)

def takeCommand():
    
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in') #Using google for voice recognition.
        print(f"User said: {query}\n")  #User query will be printed.

    except Exception as e:
        # print(e)    
        print("Say that again please...")  #Say that again will be printed in case of improper voice 
        #speak("sir i can't hear you say that again please")
        return "None" #None string will be returned
    
    return query
   
def taskExecution():
    wishme()
    while True:
    #if 1:
        query = takeCommand().lower() #Converting user query into lower case
        
        # Logic for executing tasks based on query
        if'wikipedia'in query or 'who is'in query:  #if wikipedia found in the query then this block will be executed
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=1) 
            speak("According to Wikipedia")
            print(results)
            speak(results)
        
        elif'song'in query or 'search on youtube' in query:
                speak("what would you like to search on youtube")
                content=takeCommand()
                '''link=html=urllib.request.urlopen("https://www.youtube.com/results?search_query="+content)
                video_ids=re.findall(r"watch\?v=(\S{25})",html.read().decode())
                video=("https://www.youtube.com/results?search_query="+video_ids[0])
                webbrowser.open(video)'''
                speak('alright sir , you can see the result on screen..')
                pywhatkit.playonyt(content)
                
        
        elif'open youtube'in query:
                webbrowser.open('www.youtube.com')     
        
        elif"google"in query:
            speak('sir, what would you like to search on google browser')
            sm=takeCommand()
            #webbrowser.open(f"{sm}")
            pywhatkit.search(sm)
            
        elif'my channel'in query:
            webbrowser.open("https://www.youtube.com/channel/UCoQgPaP5yingIbPwyjTRMuA")   

        elif'music'in query:
            music_dir ='E:\\my music'
            songs=os.listdir(music_dir)
            n=random.randint(0,200)
            #print(songs)
            os.startfile(os.path.join(music_dir,songs[n]))
        
        elif'time'in query:
            strTime= datetime.now().strftime("%H %M %S")
            speak(f"sir it's {strTime}now ")

        elif'open notepad'in query:
            path="C:\\Windows\\system32\\notepad.exe"
            os.startfile("C:\\Windows\\system32\\notepad.exe",)   
        
        elif'command prompt'in query:
            os.system("start cmd")
        
        elif'open camera'in query:
            '''cap=cv2.VideoCapture(0)
            while True:
                ret,img=cap.read()
                cv2.imshow('webcam',img)
                k=cv2.waitKey(50)
                if k==27:
                    break
            cap.release()
            cv2.destroyAllWindows()'''
        
        elif'ip address'in query:
             ip=get("https://api.ipify.org").text
             print(ip)
             speak(f"your ip adress is {ip}")
        
        elif'facebook'in query:
            webbrowser.open("www.facebook.com")

        elif'send message'in query:
            speak("what would you like to send messege")
            msg=takeCommand
            pywhatkit.sendwhatmsg('+918368864957','this trail',20,40)
        
        elif'you can sleep now'in query or"mike you can sleep now"in query:
            speak("thanks sir , you can call me  anytime")
            speak("just say wake up ")
            break
         
        elif'close notepad'in query:
            speak("okay sir,closing notepad")
            os.system("taskkill/f /im notepad.exe")
        
        elif 'close command prompt' in query:
            speak("okay sir,closing CMD")
            os.system("taskkill/f /im  cmd")

        elif'set alarm'in query:
            speak("sir p please tell me the time to set alarm. for example, set alarm to 7:30 am")
            k=takeCommand()
            k=k.replace("set alarm to","")
            k=k.replace(".","")
            k=k.upper()
            import alrm
            alrm.alarm(k)

        elif'tell me a joke'in query:
            joke=pyjokes.get_joke(language='en',category='neutral')
            speak(joke)

        elif'shutdown'in query:
            os.system("shutdown  /s /t 5")

        elif'restart'in query:
            os.system("restart /r /t 5")

        elif'lock the system'in query:
            os.system("rundll32.exe powrprof.dll,SetSuspendstate 0,1,0")

        elif'switch the window'in query:
              pyautogui.keyDown("alt")
              pyautogui.press("tab")
              pyautogui.keyUp("alt") 

        elif"tell me news"in query:
            news()
        
        elif'stock market news'in query:
            speak("accessing information from... indian time express news")
            stockmrkt()

        elif'send file to email'in query:
            '''try:
                speak("What should I say?")
                content = takeCommand()
                to = "anujkshah2@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("i am not able to sent this mail at this moment")''' 
            speak('what would i say...')
            email='dummyonehunk@gmail.com'#your mail
            password='anujkshah'#your password
            send_to_email='anujkshah2@gmail.com'#whom your are sending the email
            speak("sir,what subject for this mail")
            query=takeCommand()
            subject=query #the message in the mail
            speak("and,what is the message for this mail")
            query=takeCommand()
            message=query
            speak("hi sir you need enter the path of the file into shell")
            file_location=input("enter the path here:\n")
            speak ("please wait... i am sending the mail")


            msg=MIMEMultipart()
            msg['from']=email
            msg['to']=send_to_email
            msg['subject']=subject

            msg.attach(MIMEText(message,'plain'))

            #attachment setup
            filename=os.path.basename(file_location)
            attachment=open(file_location,"rb")
            part=MIMEBase('application','octet-stream')
            part.set_payload(attachment.read())
            encoders.encode_base64(part)
            part.add_header('content-disposition',"attachment; filename=%s" % filename)

            #attachment to the MIMMutipart object
            msg.attach(part)
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(email,password)
            text=msg.as_string()
            server.sendmail(email,send_to_email,text)
            server.quit()#logout\
            speak("email has been sent to dummy")

        elif'send text email'in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "anujkshah2@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("i am not able to sent this mail at this moment")

        elif'where i am 'in query or'where we are'in query or "my location " in query:
            speak("wait sir,let me check")
            try:
                ipAdd=requests.get('https://api.ipify.org').text
                print(ipAdd)
                url='https://get.geojs.io/v1/ip/geo/'+ipAdd+'.json'
                geo_requests=requests.get(url)
                geo_data=geo_requests.json()
                #print(geo_data)
                city=geo_data["city"]
                #state=geo_data['state']
                country=geo_data['country']
                speak(f"sir not sure , but i think we are in {city} city of {country}country")
            except exception as e:
                speak("sorry sir , there is network issue i am not able to find where we are")
                pass
        
        elif"good morning mike"in query or'good morning'in query:
            time=datetime.now()
            speak(f"wake up sir it's {time}now ")
            print(time)
            speak("this song from my side for your morning would you like to play...")
            query=takeCommand()
            if "yes" in query or "play" in query:
                pywhatkit.playonyt("https://www.youtube.com/watch?v=2WuuCY9Wqwo")
            else:
                speak("allright sir ")
            
        elif"good evening mike"in query or "good evening" in query:
            time=datetime.now()
            print(time)
            speak("good evening sir, how did you spend today")
            lin=takeCommand()
            speak("i can't get your emotions.. sorry ,  but i am  glad.. you told me")

        elif"good afternoon mike"in query:
            time=datetime.now()
            speak("good afternoon sir, have some work for me")
            k=takeCommand()
            speak("tell me sir ")

        elif"good night mike"in query or "good night" in query:
            time=datetime.now()
            speak("good knight sir")
            speak("sir can i shutdown the system")
            query=takeCommand()
            if "yes" in query:
                speak("system shuting down in 10 second")
                os.system("shutdown  /s /t 10")
            else:
                speak("allright sir")
                speak("wait sir.. i have some music foryour sweet knight")
                pywhatkit.playonyt("https://www.youtube.com/results?search_query=arcade+bollywood+playlist")
            
        elif"hi mike can you help me"in query:
            speak("yes of course sir i'm here tell me anything")

        elif"hello"in query or"hi mike"in query:
            speak("hi sir")
   
        elif"how are you"in query:
            speak("i am not better good sir please improve my feature's , how are you ?")
            query=takeCommand()
            if 'I am good' in query or "I am fine" in query:
                speak("that's good  now tell me how may i help you")   
            else:
                speak("don't keep hope..sir")
                query=takeCommand()
                if'why'in query or 'what' in query or 'what did you say' in query:
                    speak('hope always hurts..')
                    query=takeCommand()
                elif'not always' in query or 'you are worng' in query or 'wrong'in query or 'no you are wrong' in query:
                    speak("yes sir some time but, we do not get so much happiness when hope is fulfilled as we get sorrow when it is broken.")
                    query=takeCommand()
                elif 'right'in query or 'you are right' in query:
                    speak("thanks sir")
                
        elif"read pdf"in query:
            pdf_reader()
        
        elif'thank you mike'in query or'thanks mike'in query or'thanks'in query:
            speak("it's my pleasure sir")

        elif'what is trending on youtube'in query or 'hi mike what is trending on youtube'in query:
            speak("searching .....these are video's trend on youtube")
            webbrowser.open("https://www.youtube.com/feed/explore")

        elif'what is trend on twitter'in query or'hi mike what is trend on twitter'in query or 'check twitter notification'in query:
            speak("searching......you can see on display")
            webbrowser.open('https://twitter.com/explore/tabs/trending')
            
        elif'hide all files' in query or'please hide this file' in query or 'make it visible this file for everyone'in query:
            speak("allright sir .... please tell you want hide this folder or make it visible for everyone")
            Conditionn=takeCommand()
            if'height'in Conditionn:
                os.system("attrib +h /s /d") #os module
                speak("sir .. all files in this folder are now hide")
            elif'visible'in Conditionn:
                os.system("attrib -h /s /d")
                speak('sir ... all file in this folder are now visible for everyone')
            elif'no thanks'in Conditionn:
                speak("it'my pleasure sir ")  

        elif'this is awesome'in query:
            speak ("yes sir...  thanks")
        elif 'thanks' in query or 'thank you' in query:
            speak("i am happy sir ..")
            
        elif'my files'in query:
            speak ("yes sir ... are you want it to hide this folder or visible for everon")
            query=takeCommand
            if 'height' in query:
                os.system("attrib E:\\New folder\\py3.pdf.pdf +h /s /d")
            elif'visible' in query:
                os.system("attrib E:\\New folder\\py3.pdf.pdf -h /s /d")
            elif'nothing' in query:
                speak("okkk sir")
 
        elif'thinking'in query:
            speak("ohhh .. sir may i know the topic or your mood you talking about")
            
            query=takeCommand()
            if 'yes'in query:
                speak("speak i am listening...")
            elif'love'in query or 'in love with' in query:
                speak("that's great sir ... , sir shall i say somtehing if don't mind")
                query=takeCommand()
                if 'yes' in query:
                    speak("Being in love is an amazing feeling to go through. The constant excitement, longing for each other, the occasional fights and then making up - all make love a bumpy yet pleasurable ride. Also, a romantic relationship takes a lot of effort, sacrifices, compromises, and understanding to make it a happy and fulfilling one. If you are in a relationship that you don't want to ever jeopardiz")
                    query=takeCommand()
                    if'right'in query or 'yes you are right'in query:
                        speak("yes sir,, It is very important to realize that everyone has a breaking point, and if their needs are not met or they don't feel seen by the other, they will more than likely find it somewhere else. Thus, it is important to make your partner feel appreciated and valued") 
                        query=takeCommand()  
                        if'you are genius'in query or"you are great" in query:
                          speak("it's not me...,it's you sir..")
                          speak("sir...would you like to hear song accodring to your mood")
                elif'no' in query:
                    speak("ok sir")
            elif'career'in query or 'future' in query or 'life' in query:
                speak("sir... it's all human race and and you have to choose that you have to run away or stop and watch")   
                speak("sir ... shall i say something if you don't mind") 
                query=takeCommand()
                if 'yes' in query:
                    speak("Procrastination is the easiest trap to fall into when you're working on your goals. You've set your calendar and you know what you need to do, but do you need to do it today? Yes! Those items are not going to check themselves off of your list, and the longer you wait, the longer it will take to reach your goals. Listen to the wisdom of these people and take it to heart....  Procrastination means postpone")   
                    query=takeCommand()
                    if'yes I know'in query or'yes you are right'in query:
                        speak("sir.. don't consider yourself as weak")
                        speak("now tell me sir how may i help you to get out of this... ")
                        
                    elif'repeat'in query or'what' in query:
                        speak("Procrastination means postpone")
                        query=takeCommand()
                        if"another." in query or "the other one" in query:
                            speak("you mean sir this line...Procrastination is the easiest trap to fall into when you're working on your goals. You've set your calendar and you know what you need to do, but do you need to do it today? Yes! Those items are not going to check themselves off of your list, and the longer you wait, the longer it will take to reach your goals. Listen to the wisdom of these people and take it to heart..")
                elif'no' in query:
                    speak("okk sir")
                elif"i don't know " in query or "i have no idea" in query:
                    speak("it's ok sir , sir Would you like to go to nearby dining area ")
                query=takeCommand()
                if" yes " in query:
                    pywhatkit.search("street food near me")
            elif"no" in query:
                speak("got it ")

        elif'calculation' in query:
            r = sr.Recognizer()
            with sr.Microphone() as source:
                speak('Say what you want to calculate, example: 0 minus 0')   
                print("Listening...")
                r.adjust_for_ambient_noise(source)
                r.pause_threshold = 1
                audio = r.listen(source)
            Num_string=r.recognize_google(audio)
            print(Num_string)
            def get_operator_fn(op):
                return{
                       
                    '+' : operator.add,
                    '-' : operator.sub,
                    '*' : operator.mul,
                    'divided': operator.__truediv__, 
                }[op]
            def binary_expr(op1,oper,op2):
                op1,op2=int(op1),int (op2)
                return get_operator_fn(oper)(op1,op2)
            speak("your resutl is")
            speak(binary_expr(*(Num_string.split())))

        elif "weather report"  in query:
            speak("Which place do you need weather information?")
            search=takeCommand()
            url=f"https://www.google.com/search?q={search}"
            r=requests.get(url)
            data=BeautifulSoup(r.text,"html.parser")
            temp=data.find("div",class_="BNeawe").text
            speak(temp)
            print(temp)

        elif"activate learning mode" in query or"how to do mode"in query:
            speak("learning mode is activated ")
            while True:
                speak("tell me what you want to learn")
                learn=takeCommand()
                try:
                    if "exit" in learn  or" close" in learn:
                        speak("allright sir .. learning mode is close")
                        break
                    else: 
                        max_results=1
                        learn_any=search_wikihow(learn,max_results)
                        assert len(learn_any) == 1
                        learn_any[0].print()
                        speak(learn_any[0].summary)
                except exception as e:
                    speak("sorry sir, i am not able to find this ")
        
        elif"how much power left"in query or "check power"in query or" battery" in query:
            import psutil
            battery = psutil.sensors_battery()
            percentage = battery.percent
            speak(f"sir our system have {percentage} percent battery")
            if percentage>75:
                speak("we have enough power to continue our system work")
            elif percentage>=40 and percentage<=75:
                speak("sir you should connect your system to charging point")
            elif percentage<=15 and percentage<30:
                speak("we don't have enough power to work for long hour, please connect to charging")  
            elif percentage<=15:
                speak("system will shutdown in few minuts please connect to charging")  
        
        elif"internet speed" in query:
            import speedtest
            st=speedtest.Speedtest()
            dl=st.download()
            up=st.upload()
            speak(f"sir we have {dl} bit per second downloading speed and {up} bit per second uploading speed ")

        elif"send sms"in query:
            speak("what should i say")   
            query=takeCommand()
            from twilio.rest import Client
            account_sid = os.environ['AC633ee9bb166970487034142a19614952']
            auth_token = os.environ['7cd2f77f38889019272c1dff8888a010']
            client = Client(account_sid, auth_token)
            message = client.messages \
                .create(
                    body='hello this messss',
                    from_='+14347223816',
                    to='+918368864957',)
            print(message.sid)

        elif"volume up" in query:
            pyautogui.press("volumeup")
        elif"volume down" in query:
            pyautogui.press ("volumedown")
        elif"volume mute" in query:
            pyautogui.press ("volumemute")
        elif"pause video" in query:
            pyautogui.press ("space")
        elif"who are you" in query:
            speak("I AM jaeger ,A virtual artificial assistant , who can help you with system work")
        elif"introduce yourself" in query:
            speak("now me to introduce myself, I AM jaeger , a Virtual artificial assistant, and i am here to assist you with variety of tasks is best i can")
        elif'you know who i am' in query or'who i am'in query:
            speak("i don't know sir but soon")
            speak("sir , are you popular?")
            query=takeCommand()
            if'yes'in query:
                speak("what's your name sir")
                query=takeCommand()
                speak('Searching Wikipedia...')
                query = query.replace("wikipedia", "")
                results = wikipedia.summary(query, sentences=1) 
                speak("According to Wikipedia")
                print(results) 
                speak(results)
        elif'who made you' in query or "who is you creator"in query:
            speak("Mr. Anuj shah ")
            speak("would you like to know more about them?")
            query=takeCommand()
            if "yes" in query:
                speak("none")
            elif'no'in query:
                speak("allright sir")
        elif'hey mike' in query:
            speak("yes sir")
            query=takeCommand()
            if 'can you remind me of that moment' in query:
                speak("what moment sir ")
                query=takeCommand()
                if 'nothing' in query:
                    speak("wait sir ... i have something that can make you nostalgic")
                    query=takeCommand()
                    speak("on screen")
                    os.startfile("E:\\play video.mp4")  
        elif'what can you do' in query or 'feature' in query:
            speak("sir i have many feature's like ,I can tell you the weather report, open some system app's ,learning mode, calculation, Email etc ")
        elif"search" in query or "find" in query:
            speak("say again what do you want t search")
            search=takeCommand()
            speak("searching......you can see the result  on display")
            pywhatkit.search(search)
        elif"anything" in query:
            speak("sir i can't show you anything untill you give me the command")


            

        
       
def wakeup():
    while  True:
        query=takeCommand()
        if 'wake up' in  query:
            speak("hello sir ")
            taskExecution()
        elif'mike' in query:
            speak("hello sir")
            taskExecution()
            break
        
            
        


            

            



