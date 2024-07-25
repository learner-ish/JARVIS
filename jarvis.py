import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)
import sys  # System-specific parameters and functions
import threading  # Threading support for concurrent execution
import time  # Time-related functions
from email import encoders  # Encoding utilities for email attachments
from email.mime.base import MIMEBase  # Base class for creating MIME objects
from email.mime.multipart import MIMEMultipart  # MIME multipart email message
import google  # Google API client library (not typically used directly, could be for authentication or API access)
import pygame  # Multimedia library for games and multimedia applications
import pyjokes  # Library to fetch random jokes
import pyttsx3  # Text-to-speech library
import requests  # HTTP library for making requests
import speech_recognition as sr  # Library for speech recognition
import datetime  # Basic date and time types
import os  # Miscellaneous operating system interfaces
import cv2  # OpenCV library for computer vision tasks (e.g., image and video processing)
import random  # Generate pseudo-random numbers
from requests import get  # Importing the get function from requests module for making HTTP GET requests
import wikipedia  # Library to interact with Wikipedia
import webbrowser  # Module provides a high-level interface to allow displaying Web-based documents
import pywhatkit as kit  # Library to perform various tasks using WhatsApp, YouTube, etc.
import smtplib  # Library for sending emails using SMTP
import pyautogui  # Module to control the mouse and keyboard to automate interactions with GUIs
from googletrans import Translator  # Library for Google Translate API
from gtts import gTTS  # Google Text-to-Speech API
import email  # Library for managing email messages, including MIME message structure
import base64  # Module providing functions to encode and decode base64-encoded strings
from google.auth.transport.requests import Request  # Google authentication library
from google_auth_oauthlib.flow import InstalledAppFlow  # Google OAuth library for installed applications flow
from google.oauth2.credentials import Credentials  # Google OAuth2 credentials
from googleapiclient.discovery import build  # Google API client library core building
from googleapiclient.errors import HttpError  # Error classes for Google API client library
from email.mime.text import MIMEText  # MIMEText class for creating plain text email content
from email.mime.multipart import MIMEMultipart  # MIME multipart email message
from email.mime.base import MIMEBase  # Base class for creating MIME objects
from selenium import webdriver  # Web automation and testing library
from selenium.webdriver.common.by import By  # Locating elements on a web page
from selenium.webdriver.chrome.service import Service  # ChromeDriver service
from selenium.webdriver.common.keys import Keys  # Sending keyboard keys to web elements
from selenium.webdriver.chrome.options import Options  # Chrome browser options
from selenium.webdriver.support.ui import WebDriverWait  # WebDriver's support classes for waiting
import webdriver_manager.chrome  # Library for managing the ChromeDriver
from webdriver_manager.chrome import ChromeDriverManager  # ChromeDriverManager for automatic driver management
from selenium.webdriver.support import expected_conditions as EC  # Expected conditions for WebDriver waits
import PyQt5  # Python bindings for the Qt application framework
from PyQt5 import QtWidgets, QtCore, QtGui  # PyQt5 modules for GUI development
from PyQt5.QtCore import QTimer, QTime, QDate, Qt  # PyQt5 core functionalities
from PyQt5.QtGui import QMovie  # Class for displaying animated GIFs in a QLabel widget
from PyQt5.QtCore import *  # Import all core components of PyQt5
from PyQt5.QtGui import *  # Import all graphical components of PyQt5
from PyQt5.QtWidgets import *  # Import all widgets components of PyQt5
from PyQt5.uic import loadUiType  # Load .ui files created using Qt Designer
from jarvisGui import Ui_jarvisGui  # Importing the GUI design from a .ui file
import numpy as np  # Numerical computing library for arrays and matrices
import pyautogui as p  # Module for GUI automation using mouse and keyboard
import operator  # Module providing functions corresponding to standard operators
from threading import Thread  # Threading support for concurrent execution
from bs4 import BeautifulSoup  # Library for pulling data out of HTML and XML files
from pywikihow import search_wikihow  # Library for fetching and parsing WikiHow articles
import psutil  # Library for system and process utilities
import speedtest  # Library for testing internet connection speed
import pyaudio  # PortAudio bindings for Python (audio I/O library)
import MyAlarm

engine = pyttsx3.init('sapi5')  # Initialize the pyttsx3 engine with the 'sapi5' driver (Windows Speech API).
voices = engine.getProperty('voices')  # Get the list of available voices.
print(voices[0].id)  # Print the ID of the first available voice.
engine.setProperty('voice', voices[0].id)  # Set the voice property of the engine to the first available voice.
engine.setProperty('rate', 220)  # Set the speech rate of the engine to 220 words per minute.


    
# Text to speech
def speak(audio):
    engine.say(audio)  # Queue the given text (audio) to be spoken by the speech engine.
    print(audio)  # Print the text (audio) to the console.
    engine.runAndWait()  # Block while processing all currently queued commands, including the speech.


def say(text):
    for chunk in text.split('. '):  # Split the text into smaller chunks at each period followed by a space.
        engine.say(chunk)  # Queue each chunk to be spoken by the speech engine.
        engine.runAndWait()  # Block while processing the current chunk, ensuring it is spoken before moving to the next.


# To wish
def wish():
    hour = int(datetime.datetime.now().hour)  # Get the current hour as an integer.
    tt = time.strftime("%I:%M %p")  # Get the current time formatted as HH:MM AM/PM.
    if hour >= 0 and hour <= 12:
        speak(f"Good Morning, its {tt}")
    elif hour > 12 and hour < 18:
        speak(f"Good Afternoon, its {tt}")
    else:
        speak(f"Good Evening, its {tt}")
    speak("I am Jarvis mam. Please tell me how can I help you")

camera_running = False
cap = None # Initialize the video capture object as None.

def open_camera():
    global camera_running, cap
    camera_running = True
    cap = cv2.VideoCapture(0) # Open the default camera (usually the webcam at index 0).
    while camera_running:
        ret, img = cap.read() # Capture a frame from the camera.
        cv2.imshow('webcam', img)  # Display the captured frame in a window named 'webcam'.
        if cv2.waitKey(1) & 0xFF == 27:  
            break # Exit the loop if the ESC key (ASCII code 27) is pressed.
    cap.release()
    cv2.destroyAllWindows() # Close all OpenCV windows.
    camera_running = False
    speak("Do you need any other help?")

def close_camera():
    global camera_running
    camera_running = False
    speak("Do you need any other help?")


def play_music():
    pygame.mixer.init() # Initialize the mixer module for sound playback.
    music_dir = "C:\\Users\\LENOVO\\Music"
    valid_extensions = ['.mp3', '.wav', '.flac', '.aac']
    try:
        songs = [f for f in os.listdir(music_dir) if os.path.splitext(f)[1].lower() in valid_extensions]  # List all valid music files in the directory.
        print("Songs found:", songs)
        if songs:  # Check if there are any valid songs.
            rd = random.choice(songs)
            song_path = os.path.join(music_dir, rd)
            print("Playing:", song_path)
            pygame.mixer.music.load(song_path) # Load the selected song.
            pygame.mixer.music.play()
        else:
            print("No valid songs found in the music directory.")
        speak("Do you need any other help?")
    except Exception as e:
        print(f"An error occurred: {e}")


def stop_music():
    pygame.mixer.music.stop()
    speak("Music stopped.")
    speak("Do you need any other help?")


def news():
    main_url = 'http://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=5e2c16199626483dbe968a96df6c74e9'  # URL for fetching top headlines from TechCrunch using the News API.
    main_page = requests.get(main_url).json() # Make a GET request to the URL and parse the response as JSON.
    #print(main_page)
    articles = main_page["articles"] # Extract the list of articles from the JSON response.
    #print(articles)
    head = [] # Initialize an empty list to store the headlines
    day = ["first", "second", "third", "fourth", "fifth", "sixth", "seventh", "eighth", "ninth", "tenth"]
    for ar in articles:
        head.append(ar["title"]) # Append the title of the article to the headlines list.
    for i in range(len(day)):
        speak(f"today's {day[i]} news is: {head[i]}") # Speak out the news headline with the corresponding ordinal.
        

SCOPES = ['https://www.googleapis.com/auth/gmail.send']  # Define the scope for Gmail API, specifically for sending emails.

def get_credentials():
    creds = None  # Initialize the credentials variable.
    if os.path.exists('token.json'):  # Check if the token file exists.
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)  # Load credentials from the token file.
    if not creds or not creds.valid:  # Check if the credentials are not available or not valid.
        if creds and creds.expired and creds.refresh_token:  # If credentials are expired and a refresh token is available.
            creds.refresh(Request())  # Refresh the credentials.
        else:
            flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)  # Create a flow for OAuth 2.0 authorization.
            creds = flow.run_local_server(port=0)  # Run the local server for user authorization.
        with open('token.json', 'w') as token:  # Save the new credentials to the token file.
            token.write(creds.to_json())
    return creds  # Return the credentials.


def send_email(to, subject, message_text, file_path=None):
    try:
        service = build('gmail', 'v1', credentials=get_credentials())  # Build the Gmail API service with the authorized credentials.

        if file_path:
            # Create a multipart message for email with attachment.
            message = MIMEMultipart()  # Create a multipart email message object.
            message['to'] = to  # Set the recipient email address.
            message['subject'] = subject  # Set the email subject.
            message.attach(MIMEText(message_text, 'plain'))  # Attach the plain text message body.

            # Attach the file
            filename = os.path.basename(file_path)  # Get the file name from the file path.
            with open(file_path, "rb") as attachment:  # Open the file to be attached in binary mode.
                part = MIMEBase("application", "octet-stream")  # Create a MIMEBase object for the file.
                part.set_payload(attachment.read())  # Read the file content into the MIMEBase object.

            encoders.encode_base64(part)  # Encode the file content to base64.
            part.add_header(
                "Content-Disposition",
                f"attachment; filename= {filename}",  # Add a header indicating the attachment's filename.
            )
            message.attach(part)  # Attach the encoded file to the email message.
        else:
            # Create a plain text message for email without attachment.
            message = MIMEText(message_text)  # Create a plain text email message object.
            message['to'] = to  # Set the recipient email address.
            message['subject'] = subject  # Set the email subject.

        # Encode the message
        raw_message = base64.urlsafe_b64encode(message.as_bytes()).decode()  # Encode the email message as base64.
        create_message = {'raw': raw_message}  # Create the message dictionary with the encoded message.

        # Send the message
        send_message = service.users().messages().send(userId="me", body=create_message).execute()  # Send the email message using the Gmail API.
        print(f'Message Id: {send_message["id"]}')  # Print the ID of the sent message.
        return send_message  # Return the sent message object.
    except HttpError as error:
        print(f'An error occurred: {error}')  # Print any HTTP errors that occur during the API request.
        return None  # Return None if an error occurred.


def tweet_post(tweet):
    def account_info():
        # Read account information from a file and return it
        with open('account_info.txt', 'r') as f:
            info = f.read().split() # Read and split the content into username, email, and password
            username = info[0]
            email_address = info[1]
            password = info[2]
        return username, email_address, password

    # Get account information
    username, email_address, password = account_info()

    # Set up Chrome options
    option = Options()
    option.add_argument("--start-maximized")  # Start maximized
    option.add_argument("--disable-extensions")  # Disable extensions
    option.add_argument("--disable-popup-blocking")  # Disable popup blocking
    option.add_argument("--disable-gpu")  # Disable GPU
    option.add_argument("--no-sandbox")  # No sandbox mode
    option.add_argument("--disable-dev-shm-usage")  # Disable /dev/shm usage
    driver = webdriver.Chrome(options=option)  # Initialize Chrome WebDriver with the options

    try:
        # Open Twitter login page
        driver.get("https://x.com/i/flow/login")
        print("Opened Twitter login page")
        time.sleep(3) # Wait for the page to load


        # Define XPaths for the username, email, password fields, and buttons
        username_xpath = '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[4]/label/div/div[2]/div/input'
        next_to_username_xpath = '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/button[2]/div'
        email_xpath = '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input'
        next_to_email_xpath = '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div/button/div'
        password_xpath = '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input'
        login_button_xpath = '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/button/div'
    
        # Wait for the username field and enter username
        username_field = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, username_xpath))
        )
        username_field.send_keys(username)
        print("Entered username")
    
        # Wait for the next button and click it
        next_to_username_button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, next_to_username_xpath))
        )
        next_to_username_button.click()
        print("Clicked next button after username")
    
        # Check if the email address field is present
        try:
            email_field = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, email_xpath))
            )
            email_field.send_keys(email_address)
            print("Entered email address")
        
            # Wait for the next button and click it
            next_to_email_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, next_to_email_xpath))
            )
            next_to_email_button.click()
            print("Clicked next button after email address")
        except Exception as e:
            print("Email address page did not appear")

        # Wait for the password field and enter password
        password_field = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, password_xpath))
        )
        password_field.send_keys(password)
        print("Entered password")
    
        # Wait for the login button and click it
        login_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, login_button_xpath))
        )
        login_button.click()
        print("Clicked login button")

        # Wait for the main page to load
        time.sleep(3)
    
        # Define XPaths for tweeting
        tweet_xpath = '//*[@id="react-root"]/div/div/div[2]/header/div/div/div/div[1]/div[3]/a/div'
        message_xpath = '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div[2]/div[1]/div/div/div/div[1]/div[2]/div/div/div/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div/div/div[2]/div/div/div/div'
        post_xpath = '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div[2]/div[1]/div/div/div/div[2]/div[2]/div/div/div/button[2]/div/span/span'
    
        time.sleep(4)

        # Click on the tweet button
        tweet_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, tweet_xpath))
        )
        tweet_button.click()
        print("Clicked tweet button")
    
        # Wait for the tweet text area to appear and enter tweet
        tweet_textarea = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, message_xpath))
        )
        tweet_textarea.send_keys(tweet)
        print("Entered tweet text")
    
        time.sleep(0.5)
    # Click on the tweet post button
        tweet_post_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, post_xpath))
        )
        tweet_post_button.click()
        print("Posted tweet")
        speak("Tweet posted successfully!")
        speak("Do you need any other help?")

    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        driver.quit()  # Quit the WebDriver session
# End of tweet_post function


class MainThread(QThread):
    def __init__(self):
        super(MainThread, self).__init__()  # Initialize the QThread base class


    # To convert voice into text
    def takecommand(self):
        r = sr.Recognizer()  # Initialize the speech recognizer
        with sr.Microphone() as source:  # Use microphone as audio source
            print("Listening...")  # Print message indicating listening
            r.pause_threshold = 2  # Set pause threshold for recognizer
            audio = r.listen(source, timeout=20, phrase_time_limit=10)  # Listen to microphone input

        try:
            print("Recognizing...")  # Print message indicating recognition in progress
            query = r.recognize_google(audio, language='en-in')  # Recognize speech using Google Speech Recognition API
            print(f"User said: {query}")  # Print recognized speech

        except sr.RequestError:
            speak("Sorry, I'm having trouble accessing the speech recognition service. Please try again later.")
            return "none"  # Handle request error, return "none"

        except sr.UnknownValueError:
            speak("I didn't hear anything. Say that again please!")
            return "none"  # Handle unknown value error, return "none"

        query = query.lower()  # Convert recognized speech to lowercase
        return query  # Return the recognized query


    def run(self):
        speak("Please say wakeup to continue")  # Speak initial prompt
        while True:
            self.query = self.takecommand()  # Get user's command/query
            # Check if wake up, are you there, or hello is in the query to start task execution
            if "wake up" in self.query or "are you there" in self.query or "hello" in self.query:
                self.TaskExecution()  # Call method to handle task execution


    def stop_music_on_youtube(self):
        if self.driver is not None:  # Check if self.driver is not None
            speak("Stopping music on YouTube...")  # Speak stopping music message
            self.driver.execute_script("document.querySelector('video').pause();")  # Execute JavaScript to pause video on YouTube
        else:
            speak("No music is currently being played on YouTube.")  # Speak message indicating no music is playing
        speak("Do you need any other help?")  # Speak prompt for further assistance


    def get_operator_fn(self, op):
        return {
            '+' : operator.add,  # Return operator.add function for '+'
            '-' : operator.sub,  # Return operator.sub function for '-'
            'x' : operator.mul,  # Return operator.mul function for 'x'
            '/' : operator.__truediv__,  # Return operator.__truediv__ function for '/'
        }[op]  # Return selected operator function based on input


    def eval_binary_expr(self, op1, oper, op2):
        try:
            op1, op2 = float(op1), float(op2)  # Convert op1 and op2 to float
            operator_fn = self.get_operator_fn(oper)  # Get operator function based on oper
            if operator_fn:
                return operator_fn(op1, op2)  # Execute operator function with op1 and op2
            else:
                return "Invalid operator"  # Return message for invalid operator
        except ZeroDivisionError:
            return "Division by zero is not allowed"  # Handle division by zero error
        except ValueError:
            return "Invalid input. Please provide numerical values."  # Handle value error for invalid input


    def game_play(self):
        speak("Lets Play ROCK PAPER SCISSORS !!")  # Speak message to start game
        print("LETS PLAYYYYYYYYYYYYYY")  # Print message indicating game start
        i = 0  # Initialize counter
        Me_score = 0  # Initialize player score
        Com_score = 0  # Initialize computer score
        while(i < 5):  # Loop for 5 rounds
            choose = ("rock", "paper", "scissors")  # Tuple of game options
            com_choose = random.choice(choose)  # Randomly choose computer's move
            self.query = self.takecommand().lower()  # Get player's move
            if (self.query == "rock"):  # If player chooses rock
                if (com_choose == "rock"):  # If computer chooses rock
                    speak("ROCK")  # Speak computer's choice
                    print(f"Score:- ME :- {Me_score} : COM :- {Com_score}")  # Print current score
                elif (com_choose == "paper"):  # If computer chooses paper
                    speak("paper")  # Speak computer's choice
                    Com_score += 1  # Increment computer's score
                    print(f"Score:- ME :- {Me_score} : COM :- {Com_score}")  # Print current score
                else:  # If computer chooses scissors
                    speak("Scissors")  # Speak computer's choice
                    Me_score += 1  # Increment player's score
                    print(f"Score:- ME :- {Me_score} : COM :- {Com_score}")  # Print current score

            elif (self.query == "paper" ):  # If player chooses paper
                if (com_choose == "rock"):  # If computer chooses rock
                    speak("ROCK")  # Speak computer's choice
                    Me_score += 1  # Increment player's score
                    print(f"Score:- ME :- {Me_score+1} : COM :- {Com_score}")  # Print current score

                elif (com_choose == "paper"):  # If computer chooses paper
                    speak("paper")  # Speak computer's choice
                    print(f"Score:- ME :- {Me_score} : COM :- {Com_score}")  # Print current score
                else:  # If computer chooses scissors
                    speak("Scissors")  # Speak computer's choice
                    Com_score += 1  # Increment computer's score
                    print(f"Score:- ME :- {Me_score} : COM :- {Com_score}")  # Print current score

            elif (self.query == "scissors" or self.query == "scissor"):  # If player chooses scissors
                if (com_choose == "rock"):  # If computer chooses rock
                    speak("ROCK")  # Speak computer's choice
                    Com_score += 1  # Increment computer's score
                    print(f"Score:- ME :- {Me_score} : COM :- {Com_score}")  # Print current score
                elif (com_choose == "paper"):  # If computer chooses paper
                    speak("paper")  # Speak computer's choice
                    Me_score += 1  # Increment player's score
                    print(f"Score:- ME :- {Me_score} : COM :- {Com_score}")  # Print current score
                else:  # If computer chooses scissors
                    speak("Scissors")  # Speak computer's choice
                    print(f"Score:- ME :- {Me_score} : COM :- {Com_score}")  # Print current score
            i += 1  # Increment round counter

        print(f"FINAL SCORE :- ME :- {Me_score} : COM :- {Com_score}")  # Print final scores
        if {Me_score} > {Com_score}:  # Check who won
            speak("Congratulations, you won, wohooo....")  # Speak winning message
        else:
            speak("Sorry, I won hahaha...")  # Speak losing message
        speak("Do you need any other help?")  # Ask for further assistance

    def TaskExecution(self):
        wish()  # Call function to greet user
        alarm_ringing = False  # Variable to track if alarm is ringing
        interrupt = False  # Variable to track interrupt status
        interrupt_time = 0  # Initialize interrupt time
        while True:  # Infinite loop for task execution
            self.query = self.takecommand().lower()  # Get user's command/query
            if self.query == "none":  # If query is none, continue loop
                continue

            if "jarvis don't interrupt" in self.query:  # If user asks not to interrupt
                speak("I am sorry mam. Please let me know when you are ready.")  # Speak apology message
                interrupt = True  # Set interrupt to True
                while interrupt:  # Loop until interrupt is resolved
                    time.sleep(10)  # Sleep for 10 seconds
                    speak("Are you ready now?")  # Ask if user is ready
                    self.query = self.takecommand().lower()  # Get user's response

                    if "jarvis you can listen now" in self.query:  # If user allows listening
                        speak("Great! How can I assist you?")  # Speak confirmation message
                        interrupt = False  # Exit interrupt loop
                        break  # Exit inner while loop
                    else:
                        speak("Okay, let me know when you are ready.")  # Speak message to wait
                        # The loop will continue and ask again after 10 seconds
                    continue  # Continue outer while loop

            elif "jarvis you can listen now" in self.query:  # If user allows listening
                speak("I am back, mam. How can I assist you?")  # Speak confirmation message
                self.query = self.takecommand().lower()  # Get user's command/query

            # Logic building for tasks

            elif "open notepad" in self.query:  # If user asks to open Notepad
                import os  # Required for os.startfile
                os.startfile("C:\\Windows\\notepad.exe")  # Open Notepad application
                speak("Do you need any other help?")  # Ask for further assistance
            
            elif "send email" in self.query:
                speak("What should I send?")  # Prompt user for email content
                self.query = self.takecommand().lower()  # Get user's response

                if "send a file" in self.query:
                    to = "ishikaaggarwal1619@gmail.com"  # Set recipient email address
                    speak("What is the subject for this email?")  # Prompt for email subject
                    self.subject = self.takecommand().lower()  # Get email subject
                    speak("What is the message for this email?")  # Prompt for email message
                    self.message_text = self.takecommand().lower()  # Get email message
                    speak("Mam, please enter the correct path of the file into the shell.")  # Prompt for file path
                    file_location = input("Please enter the path here: ")  # Get file location from user input
                    send_email(to, self.subject, self.message_text, file_location)  # Send email with file attachment
                    speak("Email has been sent successfully!")  # Confirm email sent

                else:
                    to = "ishikaaggarwal1619@gmail.com"  # Set recipient email address
                    speak("What is the subject for this email?")  # Prompt for email subject
                    self.subject = self.takecommand().lower()  # Get email subject
                    speak("What is the message for this email?")  # Prompt for email message
                    self.message_text = self.takecommand().lower()  # Get email message
                    send_email(to, self.subject, self.message_text)  # Send email without file attachment
                    speak("Email has been sent successfully!")  # Confirm email sent

                speak("Do you need any other help?")  # Ask if user needs further assistance
            
            elif "open adobe reader" in self.query:
                import os
                apath = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Adobe Reader X" #required for os.startfile
                try:
                  os.startfile(apath)
                  speak("Adobe Reader is now open. Do you need any other help?")
                except Exception as e:
                  speak(f"Sorry, I couldn't open Adobe Reader. {str(e)}")

            elif "close adobe reader" in self.query: #Required for os.systm
                speak("Okay mam, closing Adobe Reader")
                os.system("taskkill /f /im AcroRd32.exe")
                speak("Do you need any other help?")

            elif "open command prompt" in self.query:
                os.system("start cmd") #Required for os.system
                speak("Do you need any other help?")

            elif "close command prompt" in self.query: #required for os.system
                speak("Okay mam, closing Command Prompt")
                os.system("taskkill /f /im cmd.exe")
                speak("Do you need any other help?")

            elif "open camera" in self.query:
                if not camera_running:  # Check if camera is not already running
                    camera_thread = threading.Thread(target=open_camera)  # Start a new thread to open the camera
                    camera_thread.start()
                    speak("Camera is now open.")
                else:
                    speak("Camera is already running.")
                speak("Do you need any other help?")

            elif "close camera" in self.query:
                if camera_running:  # Check if camera is currently running
                    close_camera()  # Close the camera function
                    speak("Camera has been closed.")
                else:
                    speak("Camera is not running.")

            elif "play music" in self.query:
                play_music()  # Call the function to play music

            elif "stop music" in self.query:
                stop_music()  # Call the function to stop music

            elif "ip address" in self.query:
                ip = get('https://api.ipify.org').text  # Fetch the public IP address using ipify API
                speak(f"Your IP address is {ip}")
                speak("Do you need any other help?")

            elif "wikipedia" in self.query:
                speak("What would you like to search on Wikipedia?")
                self.query = self.takecommand().lower()  # Get user's voice input for Wikipedia search
                speak(f"Searching Wikipedia for {self.query}...")
                try:
                    results = wikipedia.summary(self.query, sentences=2)  # Search and summarize Wikipedia article
                    speak("According to Wikipedia")
                    speak(results)
                except wikipedia.exceptions.DisambiguationError as e:
                    speak(f"Multiple results found for {self.query}. Please be more specific.")
                except wikipedia.exceptions.PageError:
                    speak(f"No page found for {self.query}.")
                except Exception as e:
                    speak(f"An error occurred: {e}")
                speak("Do you need any other help?")

            elif "open youtube" in self.query:
                webbrowser.open("youtube.com")  # Open YouTube in default web browser
                speak("Do you need any other help?")

            elif "close youtube" in self.query:
                speak("Okay mam, closing YouTube")
                pyautogui.hotkey('ctrl', 'w')  # Close the current tab in web browser using hotkey
                speak("Do you need any other help?")

            elif "open facebook" in self.query:
                webbrowser.open("www.facebook.com")  # Open Facebook in default web browser
                speak("Do you need any other help?")

            elif "close facebook" in self.query:
                speak("Okay mam, closing Facebook")
                pyautogui.hotkey('ctrl', 'w')  # Close the current tab in web browser using hotkey
                speak("Do you need any other help?")

            elif "open stack overflow" in self.query:
                webbrowser.open("stackoverflow.com")  # Open Stack Overflow in default web browser
                speak("Do you need any other help?")

            elif "close stack overflow" in self.query:
                speak("Okay mam, closing Stack Overflow")
                pyautogui.hotkey('ctrl', 'w')  # Close the current tab in web browser using hotkey
                speak("Do you need any other help?")

            elif "open google" in self.query:
                speak("Mam, what should I search on Google?")
                self.cm = self.takecommand().lower()  # Get user's voice input for Google search
                webbrowser.open(f"https://www.google.com/search?q={self.cm}")  # Open Google search query in default web browser
                speak("Do you need any other help?")

            elif "close google" in self.query:
                speak("Okay mam, closing Google")
                pyautogui.hotkey('ctrl', 'w')  # Close the current tab in web browser using hotkey
                speak("Do you need any other help?")

            elif "send message" in self.query:
                speak("Mam, what is your message?")
                self.mss = self.takecommand().lower()  # Get user's voice input for message
                kit.sendwhatmsg("+918233831801", f"{self.mss}", 23, 19)  # Send WhatsApp message to specified number at specified time
                speak("Do you need any other help?")

            elif "play my favourite song" in self.query:
                kit.playonyt("bum bum bole")  # Play the specified song from YouTube using kit module
                speak("Do you need any other help?")

            elif "stop the music" in self.query:
                pyautogui.press('space')  # Pause the currently playing music using spacebar
                #pyautogui.hotkey('alt', 'f4') for closing browser window
                #pyautogui.hotkey('ctrl', 'w')  # For Windows/Linux
                speak("Do you need any other help?")

            elif "you can sleep" in self.query:
                speak("Thanks for using me mam. Have a good day! You can wake me up anytime you want.")
                sys.exit()  # Exit the program when user says "you can sleep"

            elif "close notepad" in self.query:
                speak("Okay mam, closing notepad")
                os.system("taskkill /f /im notepad.exe")  # Force close Notepad using taskkill command
                speak("Do you need any other help?")

            elif "rock paper scissor" in self.query:
                self.game_play()  # Call the function to play rock-paper-scissors game

            elif "set alarm" in self.query:
                speak("Mam, please tell me the time to set alarm. For example, set alarm to 5:30 P.M.")
                self.tt = self.takecommand().lower()  # Get user's voice input for alarm time
                self.tt = self.tt.replace("set alarm to ", "").replace(".", "").upper()  # Format the alarm time
                MyAlarm.alarm(self.tt, 'Bhajan.mp3')  # Set alarm with specified time and sound
                speak("Do you need any other help?")

            elif "tell me a joke" in self.query:
                try:
                    #print(f"Fetched joke: {joke}")  # Debug: Print the fetched joke
                    #translator = Translator()
                    #translated_joke = translator.translate(joke, src='en', dest='hi').text
                    #print(f"{translated_joke}")   #Debug: Print the translated joke
                    joke = pyjokes.get_joke()  # Fetch a random joke using pyjokes library
                    speak(joke)  # Speak the fetched joke
                except Exception as e:
                    speak("Sorry, I couldn't retrieve or translate a joke at the moment.")  # Handle error in fetching joke
                    print(f"Error: {e}")
                speak("Do you need any other help?")

            elif 'switch the window' in self.query:
                pyautogui.keyDown("alt")  # Hold down the Alt key
                pyautogui.press("tab")  # Press the Tab key to switch windows
                time.sleep(5)  # Wait for 5 seconds
                pyautogui.keyUp("alt")  # Release the Alt key
                speak("Do you need any other help?")

            elif "do some calculations" in self.query or "can you calculate" in self.query:
                while True:
                    r = sr.Recognizer()
                    with sr.Microphone() as source:
                        speak("Say what would you like to calculate, example: 3 multiply 4")
                        print("Listening...")
                        r.adjust_for_ambient_noise(source)
                        audio = r.listen(source)  # Listen to user's voice input
                    try:
                        print("Recognizing...")
                        my_string = r.recognize_google(audio)  # Recognize voice input using Google Speech Recognition
                        print(f"User said: {my_string}")
                        op1, oper, op2 = my_string.split()  # Split the input into operands and operator
                        result = self.eval_binary_expr(op1, oper, op2)  # Evaluate the expression
                        speak("Your result is")
                        speak(result)  # Speak the result
                    except sr.RequestError:
                        speak("Sorry, I'm having trouble accessing the speech recognition service. Please try again later.")
                    except sr.UnknownValueError:
                        speak("I didn't hear anything. Please say that again.")
                    except ValueError:
                        speak("Invalid input format. Please provide numbers and an operator.")
                    except Exception as e:
                        speak(f"An error occurred: {str(e)}")

                    speak("Would you like to perform another calculation?")
                    response = self.takecommand().lower()  # Get user's voice input for continuation
                    if "no" in response:
                        speak("Okay, moving on. Do you need any other help?")
                        break  # Exit the calculation loop if user says no

                    else:
                        speak("Sure, let's continue.")  # Continue calculation if user wants
                        continue

            elif "tell me news" in self.query:
                speak("Please wait mam, fetching the latest news")
                news()  # Fetch and speak the latest news using a function named news()
                speak("Do you need any other help?")

            elif "temperature" in self.query:
                speak("Which city's temperature?")
                city = self.takecommand().lower()  # Get user's voice input for city name
                url = f"https://www.google.com/search?q=temperature+in+{city}"  # Create search URL based on user input
                r = requests.get(url)  # Send GET request to Google search
                data = BeautifulSoup(r.text, "html.parser")  # Parse the HTML response using BeautifulSoup

                # Extract temperature data from the HTML
                try:
                    temp = data.find("div", class_="BNeawe iBp4i AP7Wnd").text
                    speak(f"Current temperature in {city} is {temp}")  # Speak the temperature
                except AttributeError:
                    speak("Sorry, I couldn't fetch the temperature. Please try again.")

                speak("Do you need any other help?")  # Prompt for further assistance
                
            elif "activate how to do mode" in self.query:
                speak("How to do mode is activated")
                while True:
                    speak("please tell me what do you want to know?")
                    how = self.takecommand()
                    try:
                        if "exit" in how or "close" in how:
                            speak("Okay mam, how to mode is closed.")
                            break
                        else:
                            max_results = 1
                            how_to = search_wikihow(how, max_results) # Search WikiHow for the query
                            assert len(how_to) == 1
                            how_to[0].print() # Print the steps from the first search result
                            speak(how_to[0].summary) # Speak a summary of the steps
                    except Exception as e:
                        speak("Sorry mam, I am not able to find this.")
                speak("Do you need any other help?")

            elif "hello jarvis" in self.query or "hey jarvis" in self.query:
                speak("Hello Mam")
                continue

            elif "how are you" in self.query or "whatsapp" in self.query or "how do you do" in self.query or "how are you doing" in self.query:
                speak("I am good mam, thanks for asking. Hope the same for you. Tell me how can I help you?")
                continue
                
            elif "open mobile camera" in self.query:
                import urllib.request
                URL = "http://10.87.151.128:8080/shot.jpg" # URL for the IP webcam stream
                while True:
                    img_arr = np.array(bytearray(urllib.request.urlopen(URL).read()),dtype=np.uint8) # Read image from URL
                    img = cv2.imdecode(img_arr,-1) # Decode image
                    cv2.imshow('IPWebcam', img) # Display image in a window named 'IPWebcam'
                    q = cv2.waitKey(1) # Wait for a key press (q to quit)
                    if q == ord("q"):
                        break # Exit the while loop and close the camera display

                cv2.destroyAllWindows()   # Close all OpenCV windows

                speak("Do you need any other help?")

            elif "how much power left" in self.query or "how much power we have" in self.query or "battery" in self.query:
                battery = psutil.sensors_battery() # Get battery information
                percentage = battery.percent #Get battery percentage
                speak(f"Mam our system have {percentage} percent battery")
                if percentage>=75:
                    speak("We have enough power to continue to work")
                elif percentage>=40 and percentage<=75:
                    speak("We should connect our system to charging point to charge our battery")
                elif percentage<=15 and percentage<=30:
                    speak("We don't have enough power to work, please connect to charging")
                else:
                    speak("We have very low power, please connect to charging, the system will shutdown very soon")
                speak("Do you need any other help?")

            elif "internet speed" in self.query:
                st = speedtest.Speedtest() # Create a Speedtest object
                dl = st.download() # Perform download speed test
                up = st.upload() # Perform upload speed test
                speak(f"Mam we have {dl} bit per second downloading speed and {up} bit per second uploading speed")
                speak("Do you need any other help?")

            elif "volume up" in self.query:
                pyautogui.press("volumeup")
                speak("Do you need any other help?")
                continue
            
            elif "volume down" in self.query:
                pyautogui.press("volumedown")
                speak("Do you need any other help?")
                continue
            
            elif "volume mute" in self.query:
                pyautogui.press("volumemute")
                speak("Do you need any other help?")
                continue

            elif "tweet" in self.query or "can you tweet" in self.query:
                speak("Mam, what should I tweet") # Prompt for tweet content
                self.cmm = self.takecommand().lower() # Get tweet content

                tweet = self.cmm
                tweet_post(tweet)  # Post the tweet

            elif "shut down the system" in self.query:
                os.system("shutdown /s /t 5")

            elif "restart the system" in self.query:
                os.system("shutdown /r /t 5")

            elif "sleep the system" in self.query:
                try:
                    speak("Putting the system to sleep.")
                    os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
                except Exception as e:
                    speak(f"An error occurred while trying to sleep the system: {e}")
            else:
                speak("I didn't understand that command. Can you please repeat?")

            #speak("Do you need any other help?")

startExecution = MainThread()

class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_jarvisGui()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.startTask)
        self.ui.pushButton_2.clicked.connect(self.close)

    def startTask(self):
        self.ui.movie = QtGui.QMovie("../Jarvis_background.jpg")
        self.ui.jarvisGui.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie("../Jarvis.gif")
        self.ui.label_2.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie("../Jarvis_Loading_Screen.gif")
        self.ui.label_5.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie("../Jarvis Circular.gif")
        self.ui.label_7.setMovie(self.ui.movie)
        self.ui.movie.start()
        timer = QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start(1000)
        startExecution.start()

    def showTime(self):
        current_time = QTime.currentTime()
        current_date = QDate.currentDate()
        label_time = current_time.toString('hh:mm:ss')
        label_date = current_date.toString(Qt.ISODate)
        self.ui.textBrowser.setText(label_date)
        self.ui.textBrowser_2.setText(label_time)

app = QApplication(sys.argv)
jarvis = Main()
jarvis.show()
exit(app.exec_())