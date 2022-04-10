import pyttsx3
import speech_recognition as sr
import random
from webbrowser import open

#Function to take command from speaker
def take_commands():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening')
        r.pause_threshold = 0.7
        audio = r.listen(source)
        try:
            print("Recognizing")
            Query = r.recognize_google(audio)
            print("You: '", Query, "'")
        except Exception as ex:
            print(ex)
            print("Pardon")
            return "None"
    import time
    time.sleep(2)
    return Query

#voice_id for female voice assistant. Without voice id the default voice will be of a male.
voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"

#Function to speak
def Speak(audio):
    engine = pyttsx3.init()
    engine.setProperty("voice", voice_id)
    engine.setProperty("rate", 140)
    engine.say(audio)
    engine.runAndWait()

#function to locate hospitals using google map
def hospital():
    open("https://www.google.com/maps/search/Hospitals")
    Speak("The red markers show the Hospitals near you.......")
    exit()

#function to locate pharmacies using google map
def pharmacy():
    open("https://www.google.com/maps/search/Pharmacies")
    Speak("The red markers show the Pharmacies near you.......")
    exit()

#Function for medications
def medication():
    Speak("Please tell me your problem....")
    while True:
        command = take_commands()
        if "fever" in command:
            Speak(
                "You can take Paracetamol or Asprin... In case it doesnot work, please contact a doctor.")
        elif "headache" in command:
            Speak("I recommend you to take Disprin.")
        elif "cough and cold" in command or "cold and cough" in command or "cold" in command or "cough" in command:
            Speak("You can have Amoxicillin.")
        elif "diabetes" in command:
            Speak(
                "You can take Insulin Lispro but please contact a doctor for this.")
        elif "I am having stomach ache" in command:
            Speak(
                "You must have ate something unhealthy!! Don't worry, you can take Panadol.")
        elif "skin allergies" in command:
            Speak(
                "You can take Allegra... But please contact a skin expert as soon as possible.")
        elif "vomiting" in command:
            Speak("You can take Dolasetron.")
        elif "depression" in command or "depressed" in command:
            Speak("Lexapro will give you relief.")
        elif " chicken pox" in command:
            Speak(
                "You can take a bath with cold water added with baking soda...or you can also take Benadryl.")
        elif "arthritis" in command:
            Speak(
                "You can take Immunosupressive drug and analgesics and please contact a physician.")
        elif "asthma" in command:
            Speak("You can take Anti Anflammatory drugs..... and Please stay way from cigarettes and other smokers.")
        elif "bipolar disorder" in command:
            Speak("You can take any Antipsychotic drugs.")
        elif "chest pain" in command:
            Speak("You can take Nitroglycerine drugs.")
        elif "conjunctvitis" in command:
            Speak(
                "You should maintain hygeine and can self heal with cold compress.")
        elif "constipation" in command:
            Speak(
                "You are recommended to take Stool Softener and Fibre supplements.")
        elif "dehydration" in command or "dehydrated" in command:
            Speak(
                "You can take Oral Rehydration solution....and please drink a lot of water.")
        elif "food poison" in command or "food poisoining " in command:
            Speak("Please ensure Adequate Hydration and take rehydration solution and contact a doctor as early as posible.")
        elif "flu" in command:
            Speak(
                "I recommend you to take Antiviral drugs and to take good rest.")
        elif "indigestion" in command:
            Speak("You can take Antacids and Oral Suspension medicines.")
        elif "insomnia" in command:
            Speak("You can have Sedatives and Anti depressants.")
        elif "malaria" in command:
            Speak("You can take Anti Parasites and Antibiotics.")
        elif "malnutrition" in command:
            Speak(
                "You should take high protein diet and nutiritive suppliments.")
        elif "obesity" in command:
            Speak(
                "You should indulge in physical exercises and should take low fat diet.")
        elif "panic disorder" in command:
            Speak("You can take Anti Depressants.")
        elif "scabies" in command:
            Speak("You can take Anti Parasite drugs.")
        elif "yellow fever" in command:
            Speak(
                "You can take Oral Rehydration Therapy and in critical case please consult a doctor.")
        elif "acne" in command:
            Speak(
                "You can apply Aloe Vera and take Vitamin A derivatives.")
        elif "Hospitals" in command or "hospitals" in command or "hospital" in command:
            hospital()
        elif "Pharmacies" in command or "pharmacies" in command or "pharmacy" in command or "Pharmacy" in command:
            pharmacy()
        elif "thank you" in command or "Thank you" in command:
            num = random.randint(100, 10000)
            if num % 100 < 33 or num % 100 == 33:
                Speak(
                    "Please don't thank me for that....Have a good day.. Bye!")
                exit()
            elif num % 100 > 33 and num % 100 < 66:
                Speak("Your welcome!")
                exit()
            else:
                Speak("My pleasure as always....Bye")
                exit()
        elif "nothing" in command:
            Speak("Have a good day.. Bye!")
            exit()
        else:
            medication()
        Speak("How else can I help you??")

#Main Function
Speak("Hello user, How can I help you?")
command = take_commands()
if "who created you" in command or "Who created you" in command or "who made you" in command:
    Speak("I was Created by Aditya Yadav.")

if "give your introduction" in command or "who are you" in command:
    Speak("Hii, I am Lily. Your personal health assistant.")

if "what can you do" in command or "how can you help" in command:
    Speak("I was created with a purpose to give you some tips on your health. And I can also prescribe Medicines for You whenever needed. Just tell me the symptoms.")
if "medication" in command or "medicines" in command:
    medication()

if "Hospitals" in command or "hospitals" in command or "hospital" in command or "Hospital" in command:
    hospital()
if "Pharmacies" in command or "pharmacies" in command or "pharmacy" in command or "Pharmacy" in command:
    pharmacy()
else:
    Speak("How can I help you??")
    command = take_commands()
    if "who created you" in command or "Who created you" in command or "who made you" in command:
        Speak("I was Created by The team Bug Hunters.")

    if "give your introduction" in command or "who are you" in command:
        Speak("Hii, I am Lily. Your personal health assistant.")

    if "what can you do" in command or "how can you help" in command:
        Speak("I was created with a purpose to give you some tips on your health. And I can also prescribe Medicines for You whenever needed. Just tell me the symptoms.")
    if "medication" in command or "medicines" in command or "medicine" in command:
        medication()
    if "Hospitals" in command or "hospitals" in command or "hospital" in command or "Hospital" in command:
        hospital()
    if "Pharmacies" in command or "pharmacies" in command or "pharmacy" in command or "Pharmacy" in command:
        pharmacy()
